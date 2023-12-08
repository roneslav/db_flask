
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import interesting_fatcs_controller
from my_project.auth.domain import InterestingFatcs

interesting_fatcs_bp = Blueprint('interesting_fatcs', __name__, url_prefix= '/interesting_fatcs')

@interesting_fatcs_bp.get('')
def get_all_interesting_fatcs() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(interesting_fatcs_controller.find_all()), HTTPStatus.OK)

@interesting_fatcs_bp.post('')
def create_interesting_fatcs() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    interesting_fatcs = InterestingFatcs.create_from_dto(content)
    interesting_fatcs_controller.create(interesting_fatcs)
    return make_response(jsonify(interesting_fatcs.put_into_dto()), HTTPStatus.CREATED)


@interesting_fatcs_bp.get('/<int:movie_id>')
def get_interesting_fatcs(movie_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(interesting_fatcs_controller.find_by_id(movie_id)), HTTPStatus.OK)


@interesting_fatcs_bp.put('/<int:movie_id>')
def update_interesting_fatcs(movie_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    interesting_fatcs = InterestingFatcs.create_from_dto(content)
    interesting_fatcs.update(movie_id, interesting_fatcs)
    return make_response("Interesting fact updated", HTTPStatus.OK)


@interesting_fatcs_bp.patch('/<int:movie_id>')
def patch_interesting_fatcs(movie_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    interesting_fatcs_controller.patch(movie_id, content)
    return make_response("Interesting fact updated", HTTPStatus.OK)


@interesting_fatcs_bp.delete('/<int:movie_id>')
def delete_interesting_fatcs(movie_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    interesting_fatcs_controller.delete(movie_id)
    return make_response("Interesting fact deleted", HTTPStatus.OK)
