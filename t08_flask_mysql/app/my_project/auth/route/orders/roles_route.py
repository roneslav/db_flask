
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import roles_controller
from my_project.auth.domain import Roles

roles_bp = Blueprint('roles', __name__, url_prefix= '/roles')


@roles_bp.get('')
def get_all_roles() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(roles_controller.find_all()), HTTPStatus.OK)

@roles_bp.post('')
def create_roles() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    roles = Roles.create_from_dto(content)
    roles_controller.create(roles)
    return make_response(jsonify(roles.put_into_dto()), HTTPStatus.CREATED)


@roles_bp.get('/<int:role_id>')
def get_roles(role_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(roles_controller.find_by_id(role_id)), HTTPStatus.OK)


@roles_bp.put('/<int:role_id>')
def update_roles(role_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    roles = Roles.create_from_dto(content)
    roles.update(role_id, roles)
    return make_response("Role updated", HTTPStatus.OK)


@roles_bp.patch('/<int:role_id>')
def patch_roles(role_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    roles_controller.patch(role_id, content)
    return make_response("Role updated", HTTPStatus.OK)


@roles_bp.delete('/<int:role_id>')
def delete_roles(role_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    roles_controller.delete(role_id)
    return make_response("Role deleted", HTTPStatus.OK)
