

from my_project.auth.dao import genres_dao
from my_project.auth.service.general_service import GeneralService


class GenresService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = genres_dao
