

from my_project.auth.dao import interesting_fatcs_dao
from my_project.auth.service.general_service import GeneralService


class InterestingFatcsService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = interesting_fatcs_dao
    # def find_drivers(self, bus_id: int):
    #     return self._dao.find_drivers(bus_id)
    # def find_routes(self, bus_id: int):
    #     return self._dao.find_routes(bus_id)