# actor.py
from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

class Directors(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "directors"

    director_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_of_director: str = db.Column(db.String(255))

    def __repr__(self) -> str:
        return f"Director({self.director_id}, {self.name_of_director})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "director_id": self.director_id,
            "name_of_director": self.name_of_director,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Directors:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Directors(
            name_of_director=dto_dict.get("name_of_director"),
        )
        return obj


