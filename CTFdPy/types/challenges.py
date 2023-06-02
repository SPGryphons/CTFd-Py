from __future__ import annotations

from typing import TypedDict


class BaseChallenge(TypedDict):
    id: int | None
    name: str
    type: str
    value: int
    category: str


class ChallengePreviewPayload(BaseChallenge):
    solves: int
    solved_by_me: bool
    tags: list[str]
    template: str # You can ignore this
    script: str # You can ignore this


class PartialChallengePayload(TypedDict):
    description: str
    connection_info: str | None
    next_id: int | None
    state: str
    max_attempts: int
    type_data: dict[str, any] # You can ignore this


class PartialDynamicChallengePayload(PartialChallengePayload):
    initial: int
    minimum: int
    decay: int


class ChallengePayload(BaseChallenge):
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


class DynamicChallengePayload(ChallengePayload):
    initial: int
    minimum: int
    decay: int