

from my_project.auth.dao import movies_dao
from my_project.auth.service.general_service import GeneralService


class MoviesService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = movies_dao

    def find_actors(self, movie_id: int):
        return self._dao.find_actors(movie_id)
    # def find_routes(self, bus_id: int):
    #     return self._dao.find_routes(bus_id)