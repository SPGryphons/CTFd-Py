from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, TypedDict

from CTFdPy.constants import ChallengeType
from CTFdPy.models import Model
from CTFdPy.types.challenges import (BaseChallengeDict, ChallengeCreateDict,
                                     ChallengeDict, ChallengePreviewDict,
                                     DynamicChallengeCreateDict,
                                     DynamicChallengeDict)


class ChallengeRequirements(TypedDict):
    prerequisites: list[int]
    anonymize: Literal[True] | None


class BaseChallenge:
    """Represents a base challenge
    This should never be created, and is only meant for inheritance
    """
    id: int
    name: str
    category: str
    type: str
    value: int


@dataclass
class ChallengePreview(Model[ChallengePreviewDict], BaseChallenge):
    """Represents a challenge preview

    This should not be created manually
    """
    id: int
    name: str
    type: str
    value: int
    category: str
    solves: int
    solved_by_me: bool
    tags: list[str]


@dataclass
class ChallengeCreateResult(Model[ChallengeCreateDict | DynamicChallengeCreateDict], BaseChallenge):
    """Represents the result of creating a challenge"""

    name: str
    category: str
    description: str

    # Server will still give this parameter even if it's dynamic
    value: int
    
    type: str = ChallengeType.standard

    # Paremeters for dynamic challenges
    initial: int | None = None
    minimum: int | None = None
    decay: int | None = None

    # Parameters only set by the server
    # DO NOT manually set these if not bad things will happen
    id: int = None
    attempts: int = None
    solves: int = None
    solved_by_me: bool = None
    connection_info: str | None = None
    files: list[str] | None = None


@dataclass
class Challenge(Model[ChallengeDict | DynamicChallengeDict], BaseChallenge):
    """Represents a challenge"""
    name: str
    category: str
    description: str

    type: str
    state: str

    # Server will still give this parameter even if it's dynamic
    value: int = None

    # Paremeters for dynamic challenges
    initial: int | None = None
    minimum: int | None = None
    decay: int | None = None

    # Optional parameters
    connection_info: str | None = None                   # Optional connection info for the challenge
    max_attempts: int | None = None                      # Maximum number of attempts for the challenge
    requirements: ChallengeRequirements | None = None    # Challenge requirements
    next_id: int | None = None                           # ID of the next challenge to solve

    # Parameters only set by the server
    # DO NOT manually set these if not bad things will happen
    id: int = None
    attempts: int = None
    solves: int = None
    solved_by_me: bool = None
    files: list[str] = None
    tags: list[str] = None
    hints: list[dict[str, int]] = None

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
            
        
    def to_payload(self) -> ChallengeDict | DynamicChallengeDict:
        """Returns a dictionary representation of the challenge that
        can be used to create or modify a challenge
        """

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