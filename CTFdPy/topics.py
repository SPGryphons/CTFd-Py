from __future__ import annotations

from dataclasses import dataclass

from CTFdPy.models import Model
from CTFdPy.types.topics import TopicDict, TopicCreateDict


@dataclass
class Topic(Model[TopicDict]):
    """Represents a topic"""
    id: int = None
    name: str = None


@dataclass
class TopicCreateResult(Model[TopicCreateDict]):
    """Represents the result of creating a topic"""
    id: int = None
    challenge_id: int = None
    topic_id: int = None