

from typing import List

import sqlalchemy
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Actor
from my_project.auth.domain.orders.actor import movies_has_actors
from ...domain.orders.movies import Movies


class ActorDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Actor
    def find_movies(self, actors_actor_id: int) :
        """
        Find buses associated with a specific -movie.
        :param actor_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the bus IDs associated with the driver
        movie_ids = (
            session.query(movies_has_actors.c.movies_movie_id)
            .filter(movies_has_actors.c.actors_actor_id == actors_actor_id)
            .all()
        )

         # Extract movie IDs from the result
        movie_ids = [movie_id for (movie_id,) in movie_ids]

        # Query the Movie table to get the Bus objects associated with the bus IDs
        movies = session.query(Movies).filter(Movies.movie_id.in_(movie_ids)).all()

        return [movie.put_into_dto() for movie in movies]

    def insert_actors(self, actor_name, date_of_birth):
        try:
            result = self._session.execute(sqlalchemy.text("CALL database_labs.insert_actors(:p1, :p2)"),
                                           {"p1": actor_name, "p2": date_of_birth})
            self._session.commit()
            return result.mappings()
        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None


    def insert_actors_and_movie_dependency(self, actor_name, movie_name):
        try:
            result = self._session.execute(
                sqlalchemy.text("CALL database_labs.insert_actors_and_movie_dependency(:p1, :p2)"),
                {"p1": actor_name, "p2": movie_name})
            self._session.commit()
            return result.mappings()
        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None

