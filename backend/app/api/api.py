from fastapi import APIRouter

from .endpoints import author, order, book


api_router = APIRouter()

api_router.include_router(
    author.author_router, tags=["Author"]
)

api_router.include_router(
    order.order_router, prefix='/authors', tags=["Order"]
)


api_router.include_router(
    book.book_router, prefix='/books', tags=["Book"]
)
