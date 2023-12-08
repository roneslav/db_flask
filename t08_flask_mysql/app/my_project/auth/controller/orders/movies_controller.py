

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import movies_service


class MoviesController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = movies_service

    def find_actors(self, movie_id: int):
        return self._service.find_actors(movie_id)

    def create_dynamic_table_with_timestamp(self):
        return self._service.create_dynamic_table_with_timestamp()
