

from my_project.auth.dao import roles_dao
from my_project.auth.service.general_service import GeneralService


class RolesService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = roles_dao
