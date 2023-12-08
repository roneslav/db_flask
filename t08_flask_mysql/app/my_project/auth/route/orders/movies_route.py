
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import movies_controller
from my_project.auth.domain import Movies

movies_bp = Blueprint('movies', __name__, url_prefix= '/movies')

@movies_bp.get('')
def get_all_movies() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(movies_controller.find_all()), HTTPStatus.OK)

@movies_bp.get('/<int:movie_id>/actors')
def get_all_movies_from_actors(movie_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(movies_controller.find_actors(movie_id)), HTTPStatus.OK)


@movies_bp.post('')
def create_movies() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    movies = Movies.create_from_dto(content)
    movies_controller.create(movies)
    return make_response(jsonify(movies.put_into_dto()), HTTPStatus.CREATED)


@movies_bp.get('/<int:movie_id>')
def get_movies(movie_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(movies_controller.find_by_id(movie_id)), HTTPStatus.OK)


@movies_bp.put('/<int:movie_id>')
def update_movies(movie_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    movies = Movies.create_from_dto(content)
    movies.update(movie_id, movies)
    return make_response("Movie updated", HTTPStatus.OK)


@movies_bp.patch('/<int:movie_id>')
def patch_movies(movie_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    movies_controller.patch(movie_id, content)
    return make_response("Movie updated", HTTPStatus.OK)


@movies_bp.delete('/<int:movie_id>')
def delete_movies(movie_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    movies_controller.delete(movie_id)
    return make_response("Movie deleted", HTTPStatus.OK)


@movies_bp.post('/table')
def create_dynamic_table_with_timestamp() -> Response:
    result = movies_controller.create_dynamic_table_with_timestamp()
    response = {"result": f"{result}, Table created successfully"}
    return make_response(jsonify(response), HTTPStatus.CREATED)
