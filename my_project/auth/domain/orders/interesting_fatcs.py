# roles.py
from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

# bus_driver = db.Table(
#     'driver_bus',
#     db.Column('bus_id', db.Integer, db.ForeignKey('bus.id')),
#     db.Column('driver_id', db.Integer, db.ForeignKey('driver.id')),
#     extend_existing=True
# )
# route_bus = db.Table(
#     'route_bus',
#     db.Column('route_id', db.Integer, db.ForeignKey('route.id')),
#     db.Column('bus_id', db.Integer, db.ForeignKey('bus.id')),
#     extend_existing=True
# )


class InterestingFatcs(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "interesting_fatcs"

    movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_decription: str = db.Column(db.String(255))

    movies_movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), nullable=False)
    movie = db.relationship('Movies', backref='movies', lazy=True)

    # Many-to-Many relationship with Driver
    # drivers = db.relationship('Driver', secondary=bus_driver,
    #                                      backref=db.backref('buses_associated', lazy='dynamic'))
    # routes = db.relationship('Route', secondary=route_bus, backref=db.backref('buses_association', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"Movie({self.movie_id}, {self.movie_decription},)"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "movie_id": self.movie_id,
            "movie_decription": self.movie_decription,
            "movie": self.movie.name_of_film if self.movies_movie_id is not None else "",

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> InterestingFatcs:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = InterestingFatcs(
            movie_decription=dto_dict.get("movie_decription"),
            movies_movie_id=dto_dict.get("movies_movie_id"),
        )
        return obj
