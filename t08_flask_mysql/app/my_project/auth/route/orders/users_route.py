
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import users_controller
from my_project.auth.domain import Users

users_bp = Blueprint('users', __name__, url_prefix= '/users')


@users_bp.get('')
def get_all_users() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(users_controller.find_all()), HTTPStatus.OK)

@users_bp.post('')
def create_users() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    users = Users.create_from_dto(content)
    users_controller.create(users)
    return make_response(jsonify(users.put_into_dto()), HTTPStatus.CREATED)


@users_bp.get('/<int:user_id>')
def get_users(user_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(users_controller.find_by_id(user_id)), HTTPStatus.OK)


@users_bp.put('/<int:user_id>')
def update_users(user_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    users = Users.create_from_dto(content)
    users.update(user_id, users)
    return make_response("User updated", HTTPStatus.OK)


@users_bp.patch('/<int:user_id>')
def patch_users(user_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    users_controller.patch(user_id, content)
    return make_response("User updated", HTTPStatus.OK)


@users_bp.delete('/<int:user_id>')
def delete_users(user_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    users_controller.delete(user_id)
    return make_response("User deleted", HTTPStatus.OK)
