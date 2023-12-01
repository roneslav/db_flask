

from .orders.actor_service import ActorService
from .orders.directors_service import DirectorsService
from .orders.genres_service import GenresService
from .orders.users_service import UsersService
from .orders.roles_service import RolesService
from .orders.movies_service import MoviesService
from .orders.ratings_service import RatingsService
from .orders.reviews_service import ReviewsService
from .orders.interesting_fatcs_service import InterestingFatcsService

actor_service = ActorService()
directors_service = DirectorsService()
genres_service = GenresService()
users_service = UsersService()
roles_service = RolesService()
movies_service = MoviesService()
ratings_service = RatingsService()
reviews_service = ReviewsService()
interesting_fatcs_service = InterestingFatcsService()
