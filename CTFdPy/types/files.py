from __future__ import annotations

from typing import TypedDict


class FileDict(TypedDict):
    id: int
    location: str
    type: str