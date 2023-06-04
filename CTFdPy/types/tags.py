from __future__ import annotations

from typing import TypedDict


class TagDict(TypedDict, total=False):
    id: int
    challenge_id: int
    challenge: int | None
    value: str