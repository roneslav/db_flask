

from my_project.auth.dao import actor_dao
from my_project.auth.service.general_service import GeneralService


class ActorService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = actor_dao

    def find_movies(self, actor_id: int):
        return self._dao.find_movies(actor_id)

    def insert_actors(self, actor_name, date_of_birth):
        return self._dao.insert_actors(actor_name, date_of_birth)

    def insert_actors_and_movie_dependency(self, actor_name, movie_name):
        return self._dao.insert_actors_and_movie_dependency(actor_name, movie_name)