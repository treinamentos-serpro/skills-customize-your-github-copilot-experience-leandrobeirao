from pathlib import Path

import pandas as pd
from sqlalchemy import Boolean, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


DATABASE_PATH = Path("library.db")
CSV_PATH = Path("data.csv")


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    author: Mapped[str] = mapped_column(String(120))
    year: Mapped[int] = mapped_column(Integer)
    genre: Mapped[str] = mapped_column(String(80))
    available: Mapped[bool] = mapped_column(Boolean, default=True)


def create_database():
    """Cria o banco e as tabelas necessárias."""
    engine = create_engine(f"sqlite:///{DATABASE_PATH}")
    Base.metadata.create_all(engine)
    return engine


def load_books_from_csv(csv_path: Path = CSV_PATH) -> pd.DataFrame:
    """Carrega os livros do arquivo CSV."""
    return pd.read_csv(csv_path)


def import_books(engine, books_dataframe: pd.DataFrame) -> int:
    """Insere livros novos e retorna a quantidade adicionada."""
    # Implemente a carga usando uma Session e uma transacao.
    return 0


def get_available_books(engine) -> list[Book]:
    """Retorna os livros atualmente disponiveis."""
    with Session(engine) as session:
        statement = select(Book).where(Book.available.is_(True))
        return list(session.scalars(statement))


def books_to_dataframe(engine) -> pd.DataFrame:
    """Converte todos os registros do banco em um DataFrame."""
    # Leia os dados do SQLite, sem acessar o CSV nesta funcao.
    return pd.DataFrame()


def summarize_by_genre(books_dataframe: pd.DataFrame) -> pd.DataFrame:
    """Retorna a quantidade de livros por genero."""
    return books_dataframe.groupby("genre").size().reset_index(name="book_count")


def main():
    engine = create_database()
    books_dataframe = load_books_from_csv()
    imported_count = import_books(engine, books_dataframe)
    database_dataframe = books_to_dataframe(engine)
    genre_summary = summarize_by_genre(database_dataframe)

    genre_summary.to_csv("genre-summary.csv", index=False)
    print(f"Livros importados: {imported_count}")
    print(f"Total no banco: {len(database_dataframe)}")
    print(genre_summary)


if __name__ == "__main__":
    main()