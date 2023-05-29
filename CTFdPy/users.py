from dataclasses import dataclass
import random
import string


@dataclass
class User:
    username: str
    email: str
    password: str | None = None

    # TODO: Add all parameters

    def __post_init__(self):
        self.password = self._generate_password()

    @staticmethod
    def _generate_password() -> str:
        return ''.join(random.choice(string.ascii_letters) for _ in range(10))

    def to_dict(self) -> dict[str, str]:
        """Returns a dictionary representation of the user"""
        return {
            "name": self.username,
            "email": self.email,
            "password": self.password,
            "type": "user",
            "verified": "true",
            "banned": "false",
            "hidden": "false"
        }