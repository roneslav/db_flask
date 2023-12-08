

from typing import List

import sqlalchemy
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Ratings



class RatingsDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Ratings

    def operation(self, operation):
        try:
            result = self._session.execute(
                sqlalchemy.text("CALL database_labs.operation(:p1)"),
                {"p1": operation}
            )

            # Fetch the result from the result set
            result_set = result.fetchall()

            # Close the result set
            result.close()

            # Commit the transaction
            self._session.commit()

            # Return the extracted data
            return result_set[ 0 ][ 0 ] if result_set else None

        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None
