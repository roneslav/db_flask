
# orders DB
from .orders.actor_dao import ActorDAO
from .orders.directors_dao import DirectorsDAO
from .orders.genres_dao import GenresDAO
from .orders.users_dao import UsersDAO
from .orders.roles_dao import RolesDAO
from .orders.movies_dao import MoviesDAO
from .orders.ratings_dao import RatingsDAO
from .orders.reviews_dao import ReviewsDAO
from .orders.interesting_fatcs_dao import InterestingFatcsDAO
from .orders.genre_base_dao import GenreBaseDAO

actor_dao = ActorDAO()
directors_dao = DirectorsDAO()
genres_dao = GenresDAO()
users_dao = UsersDAO()
roles_dao = RolesDAO()
movies_dao = MoviesDAO()
ratings_dao = RatingsDAO()
reviews_dao = ReviewsDAO()
interesting_fatcs_dao = InterestingFatcsDAO()
genre_base_dao = GenreBaseDAO()
