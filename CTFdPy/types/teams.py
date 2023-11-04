from __future__ import annotations

from typing import TypedDict


class TeamDict(TypedDict):
    id: int
    name: str
    email: str | None
    affiliation: str | None
    website: str | None
    country: str | None
    bracket: str | None
    website: str | None
    members: list[int]
    captain_id: int | None
    secret: str | None
    oauth_id: str | None
    created: str
    banned: bool
    hidden: bool
    place: str | None
    score: int | None


class TeamPayload(TeamDict):
    name: str
    password: str | None
    email: str | None
    affiliation: str | None
    website: str | None
    country: str | None
    hidden: bool | None
    banned: bool | None
    captain_id: int | None
