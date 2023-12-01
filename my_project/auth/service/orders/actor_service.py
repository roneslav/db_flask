

from my_project.auth.dao import actor_dao
from my_project.auth.service.general_service import GeneralService


class ActorService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = actor_dao
    def find_movies(self, actor_id: int):
        return self._dao.find_movies(actor_id)
    # def find_routes(self, bus_id: int):
    #     return self._dao.find_routes(bus_id)