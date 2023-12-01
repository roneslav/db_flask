

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import actor_service


class ActorController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = actor_service

    def find_movies(self, actor_id: int):
        return self._service.find_movies(actor_id)

