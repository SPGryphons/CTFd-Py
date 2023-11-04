from dataclasses import dataclass
from typing import Literal

from CTFdPy.models.models import Model
from CTFdPy.types.teams import TeamDict, TeamPayload


@dataclass
class Team(Model[TeamDict]):
    name: str = None
    password: str | None = None

    # Optional properties
    email: str | None = None
    affiliation: str | None = None
    website: str | None = None
    country: str | None = None
    banned: bool | None = None
    hidden: bool | None = None
    captain_id: int | None = None

    # Parameters only set by the server
    id: int | None = None
    members: list[int] | None = None
    created: str | None = None
    bracket: str | None = None
    secret: str | None = None
    oauth_id: str | None = None
    place: str | None = None
    score: int | None = None

    def to_payload(self) -> TeamPayload:
        """Returns a dictionary representation of the team that
        can be used to create or modify a team
        """
        keys = (
            "name",
            "password",
            "email",
            "affiliation",
            "website",
            "country",
            "hidden",
            "banned",
            "captain_id"
        )

        return {
            key: getattr(self, key)
            for key in keys
            if getattr(self, key) is not None
        }