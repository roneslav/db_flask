

from my_project.auth.dao import reviews_dao
from my_project.auth.service.general_service import GeneralService


class ReviewsService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = reviews_dao
