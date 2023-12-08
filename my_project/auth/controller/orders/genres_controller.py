

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import genres_service


class GenresController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = genres_service

    def find_genres(self, genre_id: int):
        return self._service.find_genres(genre_id)

    def find_routes(self, genre_id: int):
        return self._service.find_routes(genre_id)
