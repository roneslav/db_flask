

from typing import List

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
        Find buses associated with a specific driver=movie.
        :param bus=actor_id: ID of the driver
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

    #     # Extract bus IDs from the result
        movie_ids = [movie_id for (movie_id,) in movie_ids]

        # Query the Bus table to get the Bus objects associated with the bus IDs
        movies = session.query(Movies).filter(Movies.movie_id.in_(movie_ids)).all()

        return [movie.put_into_dto() for movie in movies]

    # def find_routes(self, bus_id: int):
    #     """
    #     Find buses associated with a specific driver.
    #     :param bus_id: ID of the driver
    #     :return: List of Bus objects associated with the driver
    #     """
    #     # Assuming that you have a session object, replace it with your actual SQLAlchemy session
    #     session = self.get_session()
    #
    #     # Query the association table to get the bus IDs associated with the driver
    #     route_ids = (
    #         session.query(route_bus.c.route_id)
    #         .filter(route_bus.c.bus_id == bus_id)
    #         .all()
    #     )
    #
    #     # Extract bus IDs from the result
    #     route_ids = [route_id for (route_id,) in route_ids]
    #
    #     # Query the Bus table to get the Bus objects associated with the bus IDs
    #     routes = session.query(Route).filter(Route.id.in_(route_ids)).all()
    #
    #     return [route.put_into_dto() for route in routes]
