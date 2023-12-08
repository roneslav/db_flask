# genres.py
from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto



class Genres(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "genres"

    genre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_of_genre: str = db.Column(db.String(255))

    def __repr__(self) -> str:
        return f"Genre({self.genre_id}, {self.name_of_genre})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "genre_id": self.genre_id,
            "name_of_genre": self.name_of_genre,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Genres:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Genres(
            name_of_genre=dto_dict.get("name_of_genre"),
        )
        return obj
