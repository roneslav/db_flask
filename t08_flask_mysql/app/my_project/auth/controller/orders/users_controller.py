

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import users_service


class UsersController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = users_service

    def find_users(self, user_id: int):
        return self._service.find_users(user_id)

    def find_routes(self, user_id: int):
        return self._service.find_routes(user_id)
