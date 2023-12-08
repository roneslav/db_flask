# roles.py
from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Reviews(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text_of_review: str = db.Column(db.String(255))
    rate: int = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    user = db.relationship('Users', backref='users', lazy=True)

    def __repr__(self) -> str:
        return f"Reviews({self.review_id}, {self.text_of_review}, {self.rate})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "review_id": self.review_id,
            "text_of_review": self.text_of_review,
            "rate": self.rate,
            "user": self.user.login_of_user if self.user_id is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Reviews:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Reviews(
            text_of_review=dto_dict.get("text_of_review"),
            rate = dto_dict.get("rate"),
            user_id = dto_dict.get("user_id"),
        )
        return obj
