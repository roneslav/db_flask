# roles.py
from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

from my_project.auth.domain.orders.actor import movies_has_actors


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


class Movies(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_of_film: str = db.Column(db.String(255))
    year_expire: int = db.Column(db.Integer)
    duration: int = db.Column(db.Integer)
    rating_MPAA: float = db.Column(db.Float(1))

    genres_genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)
    genre = db.relationship('Genres', backref='genres', lazy=True)

    ratings_rating_id = db.Column(db.Integer, db.ForeignKey('ratings.rating_id'), nullable = False)
    rating = db.relationship('Ratings', backref = 'ratings', lazy = True)

    directors_director_id1 = db.Column(db.Integer, db.ForeignKey('directors.director_id'), nullable = False)
    director = db.relationship('Directors', backref = 'directors', lazy = True)

    roles_role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'), nullable = False)
    role = db.relationship('Roles', backref = 'roles', lazy = True)

    # Many-to-Many relationship with Driver
    actors = db.relationship('Actor', secondary = movies_has_actors,
                             backref = db.backref('movies_associated', lazy = 'dynamic'))
    # routes = db.relationship('Route', secondary=route_bus, backref=db.backref('buses_association', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"Movie({self.movie_id}, {self.name_of_film}, {self.year_expire}, {self.duration}, {self.rating_MPAA},)"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "movie_id": self.movie_id,
            "name_of_film": self.name_of_film,
            "year_expire": self.year_expire,
            "duration": self.duration,
            "rating_MPAA": self.rating_MPAA,
            "genre": self.genre.name_of_genre if self.genres_genre_id is not None else "",
            "rating": self.rating.rating if self.ratings_rating_id is not None else "",
            "director": self.director.name_of_director if self.directors_director_id1 is not None else "",
            "role": self.role.name_of_role if self.roles_role_id is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Movies:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Movies(
            name_of_film=dto_dict.get("name_of_film"),
            year_expire = dto_dict.get("year_expire"),
            duration = dto_dict.get("duration"),
            rating_MPAA = dto_dict.get("rating_MPAA"),
            genres_genre_id = dto_dict.get("genres_genre_id"),
            ratings_rating_id = dto_dict.get("ratings_rating_id"),
            directors_director_id1 = dto_dict.get("directors_director_id1"),
            roles_role_id = dto_dict.get("roles_role_id"),
        )
        return obj
