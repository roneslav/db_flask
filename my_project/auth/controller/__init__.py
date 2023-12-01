
from .orders.actor_controller import ActorController
from .orders.directors_controller import DirectorsController
from .orders.genres_controller import GenresController
from .orders.users_controller import UsersController
from .orders.roles_controller import RolesController
from .orders.movies_controller import MoviesController
from .orders.ratings_controller import RatingsController
from .orders.reviews_controller import ReviewsController
from .orders.interesting_fatcs_controller import InterestingFatcsController

actor_controller = ActorController()
directors_controller = DirectorsController()
genres_controller = GenresController()
users_controller = UsersController()
roles_controller = RolesController()
movies_controller = MoviesController()
ratings_controller = RatingsController()
reviews_controller = ReviewsController()
interesting_fatcs_controller = InterestingFatcsController()
