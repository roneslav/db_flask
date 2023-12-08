from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import roles_service


class RolesController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = roles_service

    def find_roles(self, role_id: int):
        return self._service.find_roles(role_id)

    def find_routes(self, user_id: int):
        return self._service.find_routes(user_id)
