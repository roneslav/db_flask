

from typing import List

import sqlalchemy
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Directors



class DirectorsDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Directors

    def insert_data(self):
        try:
            result = self._session.execute(sqlalchemy.text("CALL database_labs.insert_directors()"))
            self._session.commit()
            return result.mappings()
        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None