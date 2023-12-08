

from my_project.auth.dao import directors_dao
from my_project.auth.service.general_service import GeneralService


class DirectorsService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = directors_dao

    def insert_data(self):
        return self._dao.insert_data()