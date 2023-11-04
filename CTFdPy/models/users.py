from dataclasses import dataclass
from typing import Literal

from CTFdPy.constants import UserType
from CTFdPy.models.models import Model
from CTFdPy.types.users import UserDict, UserPayload


@dataclass
class User(Model[UserDict]):
    name: str
    type: Literal["admin", "user"] = UserType.user

    verified: bool = False
    banned: bool = False
    hidden: bool = False

    # Optional properties
    email: str | None = None # NOTE: This is optional as it is not returned by the server unless the user is requested directly
    password: str | None = None
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

    def to_payload(self) -> UserPayload:
        """Returns a dictionary representation of the user that
        can be used to create or modify a user
        """
        keys = (
            "name",
            "password",
            "email",
            "website",
            "country",
            "affiliation",
            "type",
            "hidden",
            "banned"
        )

        return {
            key: getattr(self, key)
            for key in keys
            if getattr(self, key) is not None
        }