from datetime import datetime

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field


app = FastAPI(title="Library API")


class Book(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    year: int = Field(..., ge=0, le=datetime.now().year)
    available: bool = True


books: dict[int, Book] = {}
next_book_id = 1


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/books")
def list_books():
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    pass