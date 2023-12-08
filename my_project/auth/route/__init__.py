
from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.actor_route import actor_bp
    from .orders.directors_route import directors_bp
    from .orders.genres_route import genres_bp
    from .orders.users_route import users_bp
    from .orders.roles_route import roles_bp
    from .orders.movies_route import movies_bp
    from .orders.ratings_route import ratings_bp
    from .orders.review_route import reviews_bp
    from .orders.interesting_fatcs_route import interesting_fatcs_bp

    app.register_blueprint(actor_bp)
    app.register_blueprint(directors_bp)
    app.register_blueprint(genres_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(roles_bp)
    app.register_blueprint(movies_bp)
    app.register_blueprint(ratings_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(interesting_fatcs_bp)