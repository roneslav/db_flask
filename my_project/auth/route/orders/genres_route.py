
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import genres_controller
from my_project.auth.domain import Genres

genres_bp = Blueprint('genres', __name__, url_prefix= '/genres')


@genres_bp.get('')
def get_all_genres() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(genres_controller.find_all()), HTTPStatus.OK)

# @actor_bp.get('/<int:actor_id>/actors')
# def get_all_buses_from_drivers(actor_id) -> Response:
#     """
#     Gets all objects from table using Service layer.
#     :return: Response object
#     """
#     return make_response(jsonify(actor_controller.find_drivers(actor_id)), HTTPStatus.OK)

# @bus_bp.get('/<int:actor_id>/routes')
# def get_all_buses_from_routes(bus_id) -> Response:
#     """
#     Gets all objects from table using Service layer.
#     :return: Response object
#     """
#     return make_response(jsonify(bus_controller.find_routes(bus_id)), HTTPStatus.OK)

@genres_bp.post('')
def create_genres() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    genres = Genres.create_from_dto(content)
    genres_controller.create(genres)
    return make_response(jsonify(genres.put_into_dto()), HTTPStatus.CREATED)


@genres_bp.get('/<int:genres_id>')
def get_genres(genres_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(genres_controller.find_by_id(genres_id)), HTTPStatus.OK)


@genres_bp.put('/<int:genres_id>')
def update_genres(genres_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    genres = Genres.create_from_dto(content)
    genres.update(genres_id, genres)
    return make_response("Genre updated", HTTPStatus.OK)


@genres_bp.patch('/<int:genres_id>')
def patch_genres(genres_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    genres_controller.patch(genres_id, content)
    return make_response("Genre updated", HTTPStatus.OK)


@genres_bp.delete('/<int:genres_id>')
def delete_genres(genres_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    genres_controller.delete(genres_id)
    return make_response("Genre deleted", HTTPStatus.OK)
