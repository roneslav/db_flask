

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import actor_service


class ActorController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = actor_service

    def find_movies(self, actor_id: int):
        return self._service.find_movies(actor_id)

    def insert_actors(self, actor_name, date_of_birth):
        return self._service.insert_actors(actor_name, date_of_birth)

    def insert_actors_and_movie_dependency(self, actor_name, movie_name):
        return self._service.insert_actors_and_movie_dependency(actor_name, movie_name)