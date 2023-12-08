# roles.py
from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class GenreBase(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "genre_base"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre_base_genre_id: int = db.Column(db.Integer)
    amount: int =db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"Genre base({self.id}, {self.genre_base_genre_id}, {self.amount},)"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "genre_base_genre_id": self.genre_base_genre_id,
            "amount": self.amount,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> GenreBase:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = GenreBase(
            genre_base_genre_id=dto_dict.get("genre_base_genre_id"),
            amount=dto_dict.get("amount"),
        )
        return obj
