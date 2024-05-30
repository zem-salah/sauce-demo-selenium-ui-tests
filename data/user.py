class UserData:

    _user_pretty_name_to_user_password = {
        "standard user": ["standard_user", "secret_sauce"]
    }

    @classmethod
    def get_user_password(cls, user_pretty_name):
        try:
            return cls._user_pretty_name_to_user_password[user_pretty_name][1]
        except KeyError:
            raise KeyError(
                f'User {user_pretty_name} does not exist.'
            )

    @classmethod
    def get_user_name(cls, user_pretty_name):
        try:
            return cls._user_pretty_name_to_user_password[user_pretty_name][0]
        except KeyError:
            raise KeyError(
                f'User {user_pretty_name} does not exist.'
            )
