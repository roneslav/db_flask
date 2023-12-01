# genres.py
from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Users(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login_of_user: str = db.Column(db.String(255))
    users_email: str = db.Column(db.String(255))
    parol: str = db.Column(db.String(255))

    # Many-to-Many relationship with Driver
    # drivers = db.relationship('Driver', secondary=bus_driver,
    #                                      backref=db.backref('buses_associated', lazy='dynamic'))
    # routes = db.relationship('Route', secondary=route_bus, backref=db.backref('buses_association', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"User({self.user_id}, {self.login_of_user}, {self.users_email}, {self.parol},)"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "user_id": self.user_id,
            "login_of_user": self.login_of_user,
            "users_email": self.users_email,
            "parol": self.parol,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Users:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Users(
            login_of_user=dto_dict.get("login_of_user"),
            users_email = dto_dict.get("users_email"),
            parol = dto_dict.get("parol"),
        )
        return obj
