# actor.py
from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


movies_has_actors = db.Table(
    'movies_has_actors',
    db.Column('movies_movie_id', db.Integer, db.ForeignKey('movies.movie_id')),
    db.Column('actors_actor_id', db.Integer, db.ForeignKey('actors.actor_id')),
    extend_existing=True
)


class Actor(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "actors"

    actor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    actors_name: str = db.Column(db.String(255))
    date_of_birth: str = db.Column(db.String(255))



    # Many-to-Many relationship with Driver
    movies = db.relationship('Movies', secondary=movies_has_actors,
                                         backref=db.backref('actors_associated', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"Actor({self.actor_id}, {self.actors_name}, {self.date_of_birth})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "actor_id": self.actor_id,
            "actors_name": self.actors_name,
            "date_of_birth": self.date_of_birth,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Actor:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Actor(
            actors_name=dto_dict.get("actors_name"),
            date_of_birth=dto_dict.get("date_of_birth"),
        )
        return obj
