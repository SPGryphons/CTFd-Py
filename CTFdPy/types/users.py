from __future__ import annotations

from typing import TypedDict


class UserDict(TypedDict):
    name: str
    email: str | None
    password: str | None
    type: str
    verified: bool
    banned: bool
    hidden: bool
    website: str | None
    country: str | None
    affiliation: str | None
    id: int | None
    team_id: int | None
    created: str | None
    place: int | None
    score: int | None


class UserPayload(TypedDict):
    name: str
    email: str
    password: str
    type: str
    verified: bool
    banned: bool
    hidden: bool
    website: str | None
    country: str | None
    affiliation: str | None