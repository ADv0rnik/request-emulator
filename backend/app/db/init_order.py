import logging
from sqlalchemy.orm import Session

from app.core.config import Settings
from app.schemas.order import OrderCreateModel

from app.crud.book import get_book_by_id
from app.crud.order import create_init_order
from app.core.exceptions import OrderException

logger = logging.getLogger('bookshelf')
settings = Settings()


def init_ord(db: Session):
    create_first_order(db)


def create_first_order(db: Session):
    order = settings.INIT_ORDER
    try:
        if book := get_book_by_id(db, order['book_id']):
            db_order = OrderCreateModel(
                description=order['description']
            )
            create_init_order(db, db_order, book.id, order.get('user_id', 1))
        else:
            logger.warning(f"Book with id={order['book_id']} wasn't found")
    except OrderException as err:
        logger.error(f"{err}")
