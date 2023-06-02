from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict, Literal

from CTFdPy.constants import ChallengeType
from CTFdPy.models import Model
from CTFdPy.types.challenges import (
    ChallengePreviewPayload,
    ChallengePayload,
    DynamicChallengePayload,
    PartialChallengePayload,
    PartialDynamicChallengePayload
)

class ChallengeRequirements(TypedDict):
    prerequisites: list[int]
    anonymize: Literal[True] | None


@dataclass
class ChallengePreview(Model[ChallengePreviewPayload]):
    """Represents a challenge preview

    This should not be created manually
    """
    id: int = None
    name: str = None
    type: str = None
    value: int = None
    category: str = None
    solves: int = None
    solved_by_me: bool = None
    tags: list[str] = None


@dataclass
class PartialChallenge(Model[PartialChallengePayload | PartialDynamicChallengePayload]):
    """Represents a partial challenge

    Note that this may not contain all parameters of a challenge
    """
    name: str = None
    category: str = None
    description: str = None
    connection_info: str | None = None
    type: str = ChallengeType.standard

    # Server will still give this parameter even if it's dynamic
    value: int | None = None

    # Paremeters for dynamic challenges
    initial: int | None = None
    minimum: int | None = None
    decay: int | None = None

    # Parameters only set by the server
    # DO NOT manually set these if not bad things will happen
    id: int | None = None
    attempts: int | None = None
    solves: int | None = None
    solved_by_me: bool | None = None

    files: list[str] | None = None


@dataclass
class Challenge(Model[ChallengePayload | DynamicChallengePayload]):
    """Represents a challenge"""
    name: str = None
    category: str = None
    description: str = None
    type: str = ChallengeType.standard

    # Server will still give this parameter even if it's dynamic
    value: int | None = None

    # Paremeters for dynamic challenges
    initial: int | None = None
    minimum: int | None = None
    decay: int | None = None

    # Parameters only set by the server
    # DO NOT manually set these if not bad things will happen
    id: int | None = None
    attempts: int | None = None
    solves: int | None = None
    solved_by_me: bool | None = None

    files: list[str] | None = None # Not implemented by us yet
    tags: list[str] | None = None # Not implemented by us yet
    hints: list[dict[str, str]] | None = None # Not implemented by us yet

    # Parameters that can only be set with PATCH requests
    # Hence over here they will be read-only
    state: str | None = None                             # If the challenge is hidden or visible
    connection_info: str | None = None                   # Optional connection info for the challenge
    max_attempts: int | None = None                      # Maximum number of attempts for the challenge
    requirements: ChallengeRequirements | None = None    # Challenge requirements
    next_id: int | None = None                           # ID of the next challenge to solve

    def __post_init__(self):
        if self.type == ChallengeType.dynamic:
            if not all([self.initial, self.minimum, self.decay]):
                raise ValueError("Dynamic challenges require initial, minimum, and decay parameters")
        elif self.type == ChallengeType.standard:
            if self.value is None:
                raise ValueError("Standard challenges require a value parameter")
            if any([self.initial, self.minimum, self.decay]):
                raise ValueError("Standard challenges cannot have initial, minimum, or decay parameters")
        else:
            raise ValueError("Invalid challenge type")
        

    def set_requirements(self, prerequisites: list[Challenge], anonymize: Literal[True] | None = None):
        requirements = {"prerequisites": []}
        for prerequisite in prerequisites:
            if not isinstance(prerequisite, Challenge):
                raise ValueError("Prerequisites must be of type Challenge")
            if prerequisite.id is None:
                raise ValueError("Challenge must be created before it can be used as a prerequisite")
            requirements["prerequisites"].append(prerequisite.id)
        if anonymize is not None:
            requirements["anonymize"] = anonymize
        self.requirements = requirements
            
        
    def to_dict(self) -> dict[str, str]:
        """Returns a dictionary representation of the challenge"""
        if self.type == ChallengeType.standard:
            d = {
                "name": self.name,
                "category": self.category,
                "description": self.description,
                "value": str(self.value),
                "type": self.type
            }   
        elif self.type == ChallengeType.dynamic:
            d = {
                "name": self.name,
                "category": self.category,
                "description": self.description,
                "type": self.type,
                "initial": str(self.initial),
                "minimum": str(self.minimum),
                "decay": str(self.decay)
            }
        
        # Add optional parameters
        if self.state is not None:
            d["state"] = self.state
        if self.connection_info is not None:
            d["connection_info"] = self.connection_info
        if self.max_attempts is not None:
            d["max_attempts"] = str(self.max_attempts)
        if self.requirements is not None:
            d["requirements"] = self.requirements
        if self.next_id is not None:
            d["next_id"] = str(self.next_id)

        return d