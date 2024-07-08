from utils.session_manager import SessionRepository


class User:

    _user_pretty_name_to_user_password = {
        "standard user": ["standard_user", "secret_sauce"]
    }

    def __init__(self, user_pretty_name):
        self.session = SessionRepository()
        try:
            self.name = self._user_pretty_name_to_user_password[
                user_pretty_name][0]
            self.password = self._user_pretty_name_to_user_password[
                user_pretty_name][1]
        except KeyError:
            raise KeyError(
                f'User {user_pretty_name} does not exist.'
            )
