from dataclasses import dataclass

from CTFdPy.constants import FlagType, CASE_SENSITIVE, CASE_INSENSITIVE
from CTFdPy.models import Model
from CTFdPy.types.flags import FlagDict


@dataclass
class Flag(Model[FlagDict]):
    content: str
    
    data: str = CASE_SENSITIVE
    type: str = FlagType.static
    challenge_id: int = None

    # Parameters only set by the server
    # DO NOT manually set these if not bad things will happen
    id: int | None = None

    
    @property
    def flag(self) -> str:
        """Returns the flag"""
        return self.content
    
    @flag.setter
    def flag(self, value: str):
        """Sets the flag"""
        self.content = value
    
    @property
    def case_insensitive(self) -> bool:
        """Returns whether the flag is case insensitive"""
        return self.data == CASE_INSENSITIVE
    
    @case_insensitive.setter
    def case_insensitive(self, value: bool):
        """Sets whether the flag is case insensitive"""
        if value:
            self.data = CASE_INSENSITIVE
        else:
            self.data = CASE_SENSITIVE
        
    def to_payload(self) -> FlagDict:
        """Returns a dictionary representation of the flag that
        can be used to create or modify a flag
        """
        return {
            "challenge_id": self.challenge_id,
            "content": self.content,
            "type": self.type,
            "data": self.data
        }