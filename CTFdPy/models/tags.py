from __future__ import annotations

from dataclasses import dataclass

from CTFdPy.models import Model
from CTFdPy.types.tags import TagDict


@dataclass
class Tag(Model[TagDict]):
    """Represents a tag"""
    value: str
    challenge_id: int = None
    id: int = None

    def to_payload(self) -> TagDict:
        """Returns a dictionary representation of the tag that
        can be used to create or modify a tag
        """
        return {
            "challenge_id": self.challenge_id,
            "value": self.value
        }
    
    def __str__(self) -> str:
        return self.value
    
    def __repr__(self) -> str:
        return f"<Tag challenge={self.challenge_id} value={self.value} id={self.id}>"