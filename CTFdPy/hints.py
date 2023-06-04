from __future__ import annotations

from dataclasses import dataclass

from CTFdPy.models import Model
from CTFdPy.types.hints import PartialHintDict, HintDict, HintRequirementsDict


@dataclass
class PartialHint(Model[PartialHintDict]):
    """Represents a partial hint"""
    id: int = None
    challenge_id: int = None
    cost: int = None


@dataclass
class Hint(Model[HintDict]):
    """Represents a hint"""
    id: int = None
    type: str = None
    challenge_id: int = None
    cost: int = None
    content: str = None
    requirements: HintRequirementsDict = None