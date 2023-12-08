

from my_project.auth.dao import interesting_fatcs_dao
from my_project.auth.service.general_service import GeneralService


class InterestingFatcsService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = interesting_fatcs_dao
