from fastapi import APIRouter
from models import Book, BookResponse

router = APIRouter()


@router.post("/book")
async def create_book(book: Book):
    return book


@router.get("/allbook", response_model=list[BookResponse])
async def read_all_book():
    return [
        {"id": 1, "title": "Shetty ka Mal", "author": "Kritharth", "year": 2002},
        {"id": 2, "title": "Bihari ka kadhal", "author": "Krrish Raj", "year": 2002},
    ]