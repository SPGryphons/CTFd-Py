from __future__ import annotations

from typing import TypedDict


class TopicPayload(TypedDict):
    id: int
    value: str


class TopicCreatePayload(TypedDict):
    id: int
    challenge: int
    challenge_id: int
    topic: int
    topic_id: int