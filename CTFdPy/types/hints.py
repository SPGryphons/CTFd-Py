from __future__ import annotations

from typing import Literal, TypedDict


class HintRequirementsDict(TypedDict):
    prerequisites: list[int]


class PartialHintDict(TypedDict):
    id: int
    challenge_id: int
    challenge: int
    cost: int


class HintDict(TypedDict):
    id: int
    type: Literal["standard"]
    challenge_id: int
    challenge: int | None
    cost: int
    content: str
    requirements: HintRequirementsDict | None
    html: str | None # You can ignore this