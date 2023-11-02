from __future__ import annotations

from CTFdPy.api.api import API
from CTFdPy.models.challenges import BaseChallenge
from CTFdPy.models.topics import ChallengeTopic, Topic, TopicCreateResult


class TopicsAPI(API):
    def get(self, topic_id: int) -> Topic:
        """Gets a topic by id
        
        Parameters
        ----------
        topic_id : int
            The id of the topic

        Returns
        -------
        Topic
            The topic

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get(f"/api/v1/topics/{topic_id}")

        return Topic.from_dict(res["data"])
    

    def get_all(self) -> list[Topic]:
        """Gets all topics
        
        Returns
        -------
        list[Topic]
            A list of topics

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get("/api/v1/topics")

        return [Topic.from_dict(topic) for topic in res["data"]]
    

    def _create(self, topic: ChallengeTopic) -> TopicCreateResult:
        res = self._post("/api/v1/topics", topic.to_payload())
        return TopicCreateResult.from_dict(res["data"])
    
    def create(self, challenge_or_id: BaseChallenge, value: str) -> TopicCreateResult:
        """Creates a topic
        
        Parameters
        ----------
        challenge_or_id : BaseChallenge
            The challenge or challenge id
        value : str
            The value of the topic

        Returns
        -------
        TopicCreateResult
            The created topic

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        if isinstance(challenge_or_id, BaseChallenge):
            challenge_id = challenge_or_id.id
        else:
            challenge_id = challenge_or_id
        
        return self._create(ChallengeTopic(challenge_id, value))
    

    def delete(self, topic_id: int) -> bool:
        """Deletes a topic
        
        Parameters
        ----------
        topic_id : int
            The id of the topic

        Returns
        -------
        bool
            Whether the topic was successfully deleted

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._delete(f"/api/v1/topics/{topic_id}")
        return res["success"]