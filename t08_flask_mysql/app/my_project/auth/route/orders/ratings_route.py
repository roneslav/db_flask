
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import ratings_controller
from my_project.auth.domain import Ratings

ratings_bp = Blueprint('ratings', __name__, url_prefix= '/ratings')

@ratings_bp.get('')
def get_all_ratings() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(ratings_controller.find_all()), HTTPStatus.OK)

@ratings_bp.post('')
def create_ratings() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    ratings = Ratings.create_from_dto(content)
    ratings_controller.create(ratings)
    return make_response(jsonify(ratings.put_into_dto()), HTTPStatus.CREATED)


@ratings_bp.get('/<int:rating_id>')
def get_ratings(rating_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(ratings_controller.find_by_id(rating_id)), HTTPStatus.OK)


@ratings_bp.put('/<int:rating_id>')
def update_ratings(rating_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    ratings = Ratings.create_from_dto(content)
    ratings.update(rating_id, ratings)
    return make_response("Rating updated", HTTPStatus.OK)


@ratings_bp.patch('/<int:rating_id>')
def patch_ratings(rating_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    ratings_controller.patch(rating_id, content)
    return make_response("Rating updated", HTTPStatus.OK)


@ratings_bp.delete('/<int:rating_id>')
def delete_ratings(rating_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    ratings_controller.delete(rating_id)
    return make_response("Rating deleted", HTTPStatus.OK)


@ratings_bp.get('/operation/<string:operation>')
def operation(operation) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    result = ratings_controller.operation(operation)
    return make_response(jsonify({
        f"{operation}": result
    }), HTTPStatus.OK)
