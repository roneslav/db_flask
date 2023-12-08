
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import directors_controller
from my_project.auth.domain import Directors

directors_bp = Blueprint('directors', __name__, url_prefix= '/directors')


@directors_bp.get('')
def get_all_directors() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(directors_controller.find_all()), HTTPStatus.OK)

@directors_bp.post('')
def create_directors() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    directors = Directors.create_from_dto(content)
    directors_controller.create(directors)
    return make_response(jsonify(directors.put_into_dto()), HTTPStatus.CREATED)


@directors_bp.get('/<int:directors_id>')
def get_directors(directors_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(directors_controller.find_by_id(directors_id)), HTTPStatus.OK)


@directors_bp.put('/<int:directors_id>')
def update_directors(directors_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    directors = Directors.create_from_dto(content)
    directors_controller.update(directors_id, directors)
    return make_response("Director updated", HTTPStatus.OK)


@directors_bp.patch('/<int:directors_id>')
def patch_directors(directors_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    directors_controller.patch(directors_id, content)
    return make_response("Director updated", HTTPStatus.OK)


@directors_bp.delete('/<int:directors_id>')
def delete_directors(directors_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    directors_controller.delete(directors_id)
    return make_response("Directors deleted", HTTPStatus.OK)

@directors_bp.post('/data')
def insert_data() -> Response:
    directors_controller.insert_data()
    return make_response("Directors inserted successfully")