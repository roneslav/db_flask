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


class Ratings(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rating: float = db.Column(db.Float(1))
    number_of_votes: int = db.Column(db.Integer)


    # Many-to-Many relationship with Driver
    # drivers = db.relationship('Driver', secondary=bus_driver,
    #                                      backref=db.backref('buses_associated', lazy='dynamic'))
    # routes = db.relationship('Route', secondary=route_bus, backref=db.backref('buses_association', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"Rating({self.rating_id}, {self.rating}, {self.number_of_votes},)"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "rating_id": self.rating_id,
            "rating": self.rating,
            "number_of_votes": self.number_of_votes,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Ratings:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Ratings(
            rating=dto_dict.get("rating"),
            number_of_votes = dto_dict.get("number_of_votes"),
        )
        return obj
