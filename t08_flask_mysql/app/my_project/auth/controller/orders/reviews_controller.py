

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import reviews_service


class ReviewsController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = reviews_service

    def find_reviews(self, review_id: int):
        return self._service.find_reviews(review_id)

    def find_routes(self, review_id: int):
        return self._service.find_routes(review_id)
