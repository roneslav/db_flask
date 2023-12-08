

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import ratings_service


class RatingsController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = ratings_service

    def find_ratings(self, rating_id: int):
        return self._service.find_ratings(rating_id)

    def find_routes(self, rating_id: int):
        return self._service.find_routes(rating_id)

    def operation(self, operation):
        return self._service.operation(operation)
