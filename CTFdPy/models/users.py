from dataclasses import dataclass
import random
import string

from CTFdPy.models.models import Model


@dataclass
class User(Model[dict[str, str]]):
    username: str
    email: str
    password: str | None = None

    # TODO: Add all parameters

    def __post_init__(self):
        if self.password is None or self.password == "":
            self.password = self._generate_password()

    @staticmethod
    def _generate_password() -> str:
        return ''.join(random.choice(string.ascii_letters) for _ in range(10))

    def to_payload(self) -> dict[str, str]:
        """Returns a dictionary representation of the user that
        can be used to create or modify a user
        """
        return {
            "name": self.username,
            "email": self.email,
            "password": self.password,
            "type": "user",
            "verified": "true",
            "banned": "false",
            "hidden": "false"
        }