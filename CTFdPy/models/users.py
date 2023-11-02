from dataclasses import dataclass
import random
import string
from typing import Literal

from CTFdPy.constants import UserType
from CTFdPy.models.models import Model


# TODO: Add support for teams

@dataclass
class User(Model[dict[str, str]]):
    name: str
    email: str
    password: str | None = None
    type: Literal["admin", "user"] = UserType.user

    verified: bool = False
    banned: bool = False
    hidden: bool = False

    # Optional properties
    website: str | None = None
    country: str | None = None
    affiliation: str | None = None

    # Parameters only set by the server
    id: int | None = None
    team_id: int | None = None
    created: str | None = None
    place: int | None = None
    score: int | None = None

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
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "verified": self.verified,
            "banned": self.banned,
            "hidden": self.hidden,
            "website": self.website,
            "country": self.country,
            "affiliation": self.affiliation,
            "created": self.created,
            "place": self.place,
            "score": self.score,
            "type": self.type
        }