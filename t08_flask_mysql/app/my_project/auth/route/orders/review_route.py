
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import reviews_controller
from my_project.auth.domain import Reviews

reviews_bp = Blueprint('reviews', __name__, url_prefix= '/reviews')

@reviews_bp.get('')
def get_all_reviews() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(reviews_controller.find_all()), HTTPStatus.OK)

@reviews_bp.post('')
def create_reviews() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    reviews = Reviews.create_from_dto(content)
    reviews_controller.create(reviews)
    return make_response(jsonify(reviews.put_into_dto()), HTTPStatus.CREATED)


@reviews_bp.get('/<int:review_id>')
def get_reviews(review_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(reviews_controller.find_by_id(review_id)), HTTPStatus.OK)


@reviews_bp.put('/<int:review_id>')
def update_reviews(review_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    reviews = Reviews.create_from_dto(content)
    reviews.update(review_id, reviews)
    return make_response("Review updated", HTTPStatus.OK)


@reviews_bp.patch('/<int:review_id>')
def patch_reviews(review_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    reviews = request.get_json()
    reviews_controller.patch(review_id, reviews)
    return make_response("Review updated", HTTPStatus.OK)


@reviews_bp.delete('/<int:review_id>')
def delete_reviews(review_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    reviews_controller.delete(review_id)
    return make_response("Review deleted", HTTPStatus.OK)
