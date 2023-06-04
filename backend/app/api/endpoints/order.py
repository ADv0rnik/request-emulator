import logging

from fastapi import APIRouter, Depends, HTTPException, Security
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.crud.order import create_order, get_order_by_id, update_order, close_order
from app.schemas.order import OrderModel, OrderCreateModel, OrderUpdateModel
from app.api.dependencies import get_current_user

order_router = APIRouter()
logger = logging.getLogger('bookshelf')


@order_router.post('/order', response_model=OrderModel)
async def make_order(
        book_id: int,
        order: OrderCreateModel,
        db: Session = Depends(get_db),
        auth=Security(get_current_user)
):
    if db_order := create_order(db, order, book_id, auth.id):
        return db_order
    else:
        return HTTPException(status_code=400, detail="Error while creating order")


@order_router.put('/order/{order_id}', response_model=OrderModel)
async def add_to_order(
        order_id: int,
        book_id: int,
        db: Session = Depends(get_db),
        _=Security(get_current_user)
):
    if db_order := await get_order_by_id(db, order_id):
        if db_order.status == "pending":
            return await update_order(db, db_order, book_id)
        else:
            logger.info(f"The order with id={order_id} has been closed")
            return HTTPException(status_code=200, detail=f"The order with id={order_id} has been closed")
    else:
        return HTTPException(status_code=404, detail=f"The order with id={order_id} not found")


@order_router.put('/order/{order_id}/complete', response_model=dict)
async def finalize_order(order_id: int, db: Session = Depends(get_db)):
    if db_order := await get_order_by_id(db, order_id):
        if db_order.status == "pending":
            return await close_order(db, db_order)
        else:
            logger.info(f"The order with id={order_id} has been closed")
            return HTTPException(status_code=200, detail=f"The order with id={order_id} has been closed")
    else:
        return HTTPException(status_code=404, detail=f"The order with id={order_id} not found")

