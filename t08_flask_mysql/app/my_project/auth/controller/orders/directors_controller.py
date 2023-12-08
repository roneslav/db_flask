

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import directors_service


class DirectorsController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = directors_service

    def find_directors(self, director_id: int):
        return self._service.find_directors(director_id)

    def find_routes(self, director_id: int):
        return self._service.find_routes(director_id)

    def insert_data(self):
        return self._service.insert_data()
