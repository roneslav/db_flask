

from my_project.auth.dao import ratings_dao
from my_project.auth.service.general_service import GeneralService


class RatingsService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = ratings_dao

    def operation(self, operation):
        return self._dao.operation(operation)