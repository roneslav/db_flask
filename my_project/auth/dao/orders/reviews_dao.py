

from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Reviews



class ReviewsDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Reviews
