from __future__ import annotations

from typing import TypedDict


class FlagDict(TypedDict):
    id: int
    challenge_id: int
    challenge: int
    content: str
    type: str
    data: str