from dataclasses import dataclass

from CTFdPy.constants import FlagType


@dataclass
class Flag:
    content: str
    data: str
    type: str = FlagType.static

    # Parameters only set by the server
    # DO NOT manually set these if not bad things will happen
    id: int | None = None

    # Challenge id shenanigans
    # For some reason, when a challenge is created, we need to send the challenge id as a string
    # But when we're adding a flag, we need to send the challenge id as an int
    # So what we do here is create two parameters, if one is used, we know which one to use
    challenge_id: int | None = None
    challenge: int | None = None
    
        
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
        return self.data == "case_insensitive"
    
    @case_insensitive.setter
    def case_insensitive(self, value: bool):
        """Sets whether the flag is case insensitive"""
        if value:
            self.data = "case_insensitive"
        else:
            self.data = ""
        
    def to_dict(self) -> dict[str, str | int]:
        """Returns a dictionary representation of the flag"""

        if self.challenge_id is None and self.challenge is None:
            raise ValueError("Flag must have a challenge id")
        
        d = {
            "content": self.content,
            "type": self.type,
            "data": self.data
        }

        # NOTE: This means that if both challenge_id and challenge are set, challenge will be used
        # We have to do this because the server returns both challenge and challenge_id in the response... for some reason
        if self.challenge is not None:
            d["challenge"] = self.challenge
        else:
            d["challenge_id"] = str(self.challenge_id)
        return d