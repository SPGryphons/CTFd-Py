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
    cost: int
    content: str
    challenge_id: int = None
    id: int = None
    type: str = None
    requirements: HintRequirementsDict = None

    # TODO: support IDs as a requirement

    def set_requirements(self, *hints: Hint | PartialHint):
        """Sets the requirements of the hint"""
        for h in hints:
            if not isinstance(h, (Hint, PartialHint)):
                raise TypeError(
                    f"Expected Hint or PartialHint, got {type(h)}"
                )
            if h.id is None:
                raise ValueError(
                    f"Hint {h} must be created before it can be used as a requirement"
                )
            
        self.requirements = {
            "prerequisites": [h.id for h in hints],
        }

        return self.requirements

    def add_requirements(self, *hints: Hint | PartialHint):
        """Adds requirements to the hint"""
        if self.requirements is None:
            return self.set_requirements(*hints)
        else:
            for h in hints:
                if not isinstance(h, (Hint, PartialHint)):
                    raise TypeError(
                        f"Expected Hint or PartialHint, got {type(h)}"
                    )
                if h.id is None:
                    raise ValueError(
                        f"Hint {h} must be created before it can be used as a requirement"
                    )
                if h.id not in self.requirements["prerequisites"]:
                    self.requirements["prerequisites"].append(h.id)

        return self.requirements
                
    def remove_requirements(self, *hints: Hint | PartialHint):
        """Removes requirements from the hint"""
        if self.requirements is None:
            raise ValueError(
                f"Hint {self} does not have any requirements"
            )
        else:
            for h in hints:
                if not isinstance(h, (Hint, PartialHint)):
                    raise TypeError(
                        f"Expected Hint or PartialHint, got {type(h)}"
                    )
                if h.id not in self.requirements["prerequisites"]:
                    raise ValueError(
                        f"Hint {self} does not have requirement {h}"
                    )
                self.requirements["prerequisites"].remove(h.id)

        return self.requirements

    def to_payload(self) -> HintDict:
        """Returns a dictionary representation of the hint that
        can be used to create or modify a hint
        """
        return {
            "challenge_id": self.challenge_id,
            "cost": self.cost,
            "content": self.content,
            "requirements": self.requirements
        }