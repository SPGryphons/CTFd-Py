from __future__ import annotations

from dataclasses import dataclass

from CTFdPy.models import Model
from CTFdPy.types.tags import TagDict


@dataclass
class Tag(Model[TagDict]):
    """Represents a tag"""
    id: int = None
    challenge_id: int = None
    value: str = None