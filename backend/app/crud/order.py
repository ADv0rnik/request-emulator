import datetime
import logging
from fastapi import HTTPException

from sqlalchemy.orm import Session, joinedload
from sqlalchemy.orm.exc import UnmappedInstanceError

from app.models.order import Order
from app.models.order_book import OrderBook
from app.crud.book import get_book_by_id

logger = logging.getLogger('bookshelf')


def commit_changes(db: Session, obj):
    db.add(obj)
    db.commit()
    db.refresh(obj)
    logger.info(f"DB updated {obj}")


def return_cost(db: Session, book_id: int):
    if book := get_book_by_id(db, book_id):
        logger.info(f"Return {book.price} for {book.title}")
        return book.price
    else:
        return HTTPException(status_code=404, detail=f"Book with id={book_id} wasn't found")


def create_order_book(db: Session, order_id: int, book_id: int):
    db_order_book = OrderBook(
        order_id=order_id,
        book_id=book_id
    )
    commit_changes(db, db_order_book)


def create_init_order(db: Session, order: Order, book_id: int, user_id: int) -> Order:
    if cost := return_cost(db, book_id=book_id):
        db_order = Order(
            description=order.description,
            cost=cost,
            user_id=user_id
        )
        commit_changes(db, db_order)

        db_order_book = OrderBook(
            order_id=db_order.id,
            book_id=book_id
        )
        commit_changes(db, db_order_book)
        logger.info(f"Order {db_order} created")
        return db_order


def create_order(db: Session, order: Order, book_id: int, user_id: int) -> Order:
    if cost := return_cost(db, book_id=book_id):
        db_order = Order(
            **order.dict(),
            user_id=user_id,
            cost=cost
        )
        commit_changes(db, db_order)

        db_order_book = OrderBook(
            order_id=db_order.id,
            book_id=book_id
        )
        commit_changes(db, db_order_book)
        logger.info(f"Order {db_order.id} created")
        return db_order


async def get_order_by_id(db: Session, order_id: int) -> Order:
    return db.query(Order).options(joinedload(Order.books)).where(Order.id == order_id).first()


async def update_order(db: Session, order: Order, book_id: int) -> Order:
    book_cost = return_cost(db, book_id)
    order.cost += book_cost
    order.update_at = datetime.datetime.now()
    try:
        db.commit()
        db.refresh(order)

        book_ids = [book.book_id for book in order.books]
        if book_id not in book_ids:
            create_order_book(db, order.id, book_id)
        else:
            for book_ in order.books:
                if book_.book_id == book_id:
                    book_.amount = book_.amount + 1
                    db.commit()
                    db.refresh(book_)
                    logger.info(f"Order {order.id} updated: {book_}")

        return order
    except TypeError as err:
        return {"status": 500, "message": f"{err}"}
    except UnmappedInstanceError as err:
        return {"status": 500, "message": f"{err}"}


async def close_order(db: Session, order: Order):
    order.status = "processing"
    db.commit()
    db.refresh(order)
    return {"result": "success"}
