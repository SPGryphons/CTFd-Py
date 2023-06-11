from __future__ import annotations

from typing import TypedDict


class TopicDict(TypedDict):
    id: int
    value: str


class ChallengeTopicDict(TopicDict):
    challenge_id: int
    topic_id: int


class TopicCreateDict(TypedDict):
    id: int
    challenge: int | None
    challenge_id: int
    topic: int
    topic_id: int