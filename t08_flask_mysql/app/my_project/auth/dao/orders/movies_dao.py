

from typing import List

import sqlalchemy
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Movies

from my_project.auth.domain.orders.actor import movies_has_actors
from my_project.auth.domain import Actor



class MoviesDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Movies

    def find_actors(self, movies_movie_id: int) :
        """
        Find buses associated with a specific driver=movie.
        :param bus=actor_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the bus IDs associated with the driver
        actor_ids = (
            session.query(movies_has_actors.c.actors_actor_id)
            .filter(movies_has_actors.c.movies_movie_id == movies_movie_id)
            .all()
        )

    #     # Extract bus IDs from the result
        actor_ids = [actor_id for (actor_id,) in actor_ids]

        # Query the Bus table to get the Bus objects associated with the bus IDs
        actors = session.query(Actor).filter(Actor.actor_id.in_(actor_ids)).all()

        return [actor.put_into_dto() for actor in actors]

    def create_dynamic_table_with_timestamp(self):
        result = self._session.execute(sqlalchemy.text("CALL database_labs.create_dynamic_table_with_timestamp()"))
        self._session.commit()
        return result.mappings()
