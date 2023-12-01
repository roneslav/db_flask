

from my_project.auth.dao import roles_dao
from my_project.auth.service.general_service import GeneralService


class RolesService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = roles_dao
    # def find_drivers(self, bus_id: int):
    #     return self._dao.find_drivers(bus_id)
    # def find_routes(self, bus_id: int):
    #     return self._dao.find_routes(bus_id)