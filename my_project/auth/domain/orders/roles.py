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


class Roles(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "roles"

    role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_of_role: str = db.Column(db.String(255))

    actors_actor_id1 = db.Column(db.Integer, db.ForeignKey('actors.actor_id'), nullable = False)
    actor = db.relationship('Actor', backref = 'roles', lazy = True)

    # Many-to-Many relationship with Driver
    # drivers = db.relationship('Driver', secondary=bus_driver,
    #                                      backref=db.backref('buses_associated', lazy='dynamic'))
    # routes = db.relationship('Route', secondary=route_bus, backref=db.backref('buses_association', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"Role({self.role_id}, {self.name_of_role},)"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "role_id": self.role_id,
            "name_of_role": self.name_of_role,
            "actor": self.actor.actors_name if self.actors_actor_id1 is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Roles:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Roles(
            name_of_role=dto_dict.get("name_of_role"),
            actors_actor_id1=dto_dict.get("actors_actor_id1"),
        )
        return obj
