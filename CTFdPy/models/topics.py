from __future__ import annotations

from dataclasses import dataclass

from CTFdPy.models import Model
from CTFdPy.types.topics import ChallengeTopicDict, TopicCreateDict, TopicDict


@dataclass
class Topic(Model[TopicDict]):
    """Represents a topic"""
    id: int = None
    value: str = None


@dataclass
class ChallengeTopic(Model[ChallengeTopicDict]):
    """Represents a topic for a challenge"""
    value: str
    challenge_id: int = None
    id: int = None
    topic_id: int = None

    def to_payload(self) -> ChallengeTopicDict:
        """Returns a dictionary representation of the topic that
        can be used to create or modify a topic
        """
        return {
            "challenge_id": self.challenge_id,
            "topic_id": self.topic_id,
            "value": self.value
        }


@dataclass
class TopicCreateResult(Model[TopicCreateDict]):
    """Represents the result of creating a topic"""
    id: int
    challenge_id: int
    topic_id: int