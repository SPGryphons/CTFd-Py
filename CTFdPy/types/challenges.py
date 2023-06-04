from __future__ import annotations

from typing import TypedDict


class BaseChallengeDict(TypedDict):
    id: int
    name: str
    type: str
    value: int
    category: str


class ChallengePreviewDict(BaseChallengeDict):
    solves: int
    solved_by_me: bool
    tags: list[str]
    template: str # You can ignore this
    script: str # You can ignore this


class PartialChallengeDict(TypedDict):
    description: str
    connection_info: str | None
    next_id: int | None
    state: str
    max_attempts: int
    type_data: dict[str, any] # You can ignore this


class PartialDynamicChallengeDict(PartialChallengeDict):
    initial: int
    minimum: int
    decay: int


class ChallengeDict(BaseChallengeDict):
    description: str
    connection_info: str | None
    next_id: int | None
    state: str
    max_attempts: int
    type_data: dict[str, any] # You can ignore this
    solves: int
    solved_by_me: bool
    attempts: int
    files: list[str]
    tags: list[str]
    hints: list[dict[str, str]]
    view: str # You can ignore this


class DynamicChallengeDict(ChallengeDict):
    initial: int
    minimum: int
    decay: int