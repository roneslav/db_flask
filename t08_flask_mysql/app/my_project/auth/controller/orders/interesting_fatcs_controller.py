

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import interesting_fatcs_service


class InterestingFatcsController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = interesting_fatcs_service

    def find_interesting_fatcs(self, movie_id: int):
        return self._service.find_interesting_fatcs(movie_id)

    def find_routes(self, movie_id: int):
        return self._service.find_routes(movie_id)
