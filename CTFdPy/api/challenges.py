from __future__ import annotations

import os
from io import BufferedIOBase
from typing import Any, overload

from CTFdPy.api.api import API
from CTFdPy.constants import (CASE_INSENSITIVE, CASE_SENSITIVE, ChallengeState,
                              ChallengeType, FlagType)
from CTFdPy.models.challenges import (BaseChallenge, Challenge,
                                      ChallengeCreateResult, ChallengePreview)
from CTFdPy.models.flags import Flag
from CTFdPy.models.hints import Hint
from CTFdPy.models.tags import Tag
from CTFdPy.models.topics import ChallengeTopic


class ChallengesAPI(API):
    def get(self, challenge_id: int) -> Challenge:
        """Gets a challenge by id
        
        Parameters
        ----------
        challenge_id : int
            The id of the challenge

        Returns
        -------
        Challenge
            The challenge

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get(f"/api/v1/challenges/{challenge_id}")

        return Challenge.from_dict(res["data"])
    

    def get_visible(self) -> list[ChallengePreview]:
        """Gets all visible challenges
        
        NOTE: This is accessible even to non-admins
        
        Returns
        -------
        list[ChallengePreview]
            A list of challenge previews

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get("/api/v1/challenges")

        return [ChallengePreview.from_dict(challenge) for challenge in res["data"]]
    

    def get_all(self) -> list[Challenge]:
        """Gets all challenges
        
        Parameters
        ----------
        view : str, optional
            The view of the challenges, by default "admin"

        Returns
        -------
        list[Challenge]
            A list of challenges

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get("/api/v1/challenges?view=admin")

        return [ChallengePreview.from_dict(challenge) for challenge in res["data"]]
    

    def _create(
        self,
        challenge: Challenge,
        flags: list[Flag],
        hints: list[Hint] | None = None,
        tags: list[Tag] | None = None,
        topics: list[ChallengeTopic] | None = None,
        files: list[os.PathLike | BufferedIOBase] | None = None,
        *,
        hints_ordered: bool = True,
        delete_on_error: bool = True
    ) -> ChallengeCreateResult:

        # Create challenge first
        res = self._post("/api/v1/challenges", challenge.to_payload())

        challenge_result = ChallengeCreateResult.from_dict(res["data"])

        try:
            # Create flags
            for flag in flags:
                flag.challenge_id = challenge_result.id
                self.client._flags_api._create(flag)

            # Create hints
            last_hint = None
            if hints is not None:
                for hint in hints:
                    if hints_ordered:
                        if last_hint is not None:
                            hint.set_requirements(last_hint)
                    hint.challenge_id = challenge_result.id
                    hint = self.client._hints_api._create(hint)
                    last_hint = hint

            # Create tags
            if tags is not None:
                for tag in tags:
                    tag.challenge_id = challenge_result.id
                    self.client._tags_api._create(tag)

            # Create topics
            if topics is not None:
                for topic in topics:
                    topic.challenge_id = challenge_result.id
                    self.client._topics_api._create(topic)

            # Create files
            if files is not None:
                self.client._files_api.create(challenge_result.id, *files)

        except Exception as e:
            if delete_on_error:
                self.delete(challenge_result.id)
            raise e from e
        
        return challenge_result
    

    @overload
    def create(
        self,
        name: str,
        category: str,
        description: str,
        type: str = ChallengeType.standard,
        state: str = ChallengeState.visible,
        flag: str | None = None,
        flag_type = FlagType.static,
        case_insensitive: bool = False,
        flags: list[tuple[str, str, bool]] | None = None, # [(flag, type, case_insensitive)]
        *,
        value: int | None = None,
        connection_info: str | None = None,
        max_attempts: int | None = None,
        hints: list[tuple[str, int]] | None = None, # [(content, cost)]
        hints_ordered: bool = True, # Whether hints require previous hints, from top to bottom
        tags: list[str] | None = None,
        topics: list[str] | None = None,
        files: list[os.PathLike[Any] | BufferedIOBase] | None = None,
        requirements: list[BaseChallenge] | None = None,
        delete_on_error: bool = True # Whether to delete the challenge if an error occurs
    ) -> ChallengeCreateResult:
        ...

    @overload
    def create(
        self,
        name: str,
        category: str,
        description: str,
        type: str = ChallengeType.dynamic,
        state: str = ChallengeState.visible,
        flag: str | None = None,
        flag_type = FlagType.static,
        case_insensitive: bool = False,
        flags: list[tuple[str, str, bool]] | None = None, # [(flag, type, case_insensitive)]
        *,
        initial: int | None = None,
        minimum: int | None = None,
        decay: int | None = None,
        connection_info: str | None = None,
        max_attempts: int | None = None,
        hints: list[tuple[str, int]] | None = None, # [(content, cost)]
        hints_ordered: bool = True, # Whether hints require previous hints, from top to bottom
        tags: list[str] | None = None,
        topics: list[str] | None = None,
        files: list[os.PathLike[Any] | BufferedIOBase] | None = None,
        requirements: list[BaseChallenge] | None = None,
        delete_on_error: bool = True # Whether to delete the challenge if an error occurs
    ) -> ChallengeCreateResult:
        ...

    def create(
        self,
        name: str,
        category: str,
        description: str,
        type: str = ChallengeType.standard,
        state: str = ChallengeState.visible,
        flag: str | None = None,
        flag_type = FlagType.static,
        case_insensitive: bool = False,
        flags: list[tuple[str, str, bool]] | None = None, # [(flag, type, case_insensitive)]
        *,
        value: int | None = None,
        initial: int | None = None,
        minimum: int | None = None,
        decay: int | None = None,
        connection_info: str | None = None,
        max_attempts: int | None = None,
        hints: list[tuple[str, int]] | None = None, # [(content, cost)]
        hints_ordered: bool = True, # Whether hints require previous hints, from top to bottom
        tags: list[str] | None = None,
        topics: list[str] | None = None,
        files: list[os.PathLike[Any] | BufferedIOBase] | None = None,
        requirements: list[BaseChallenge] | None = None,
        delete_on_error: bool = True # Whether to delete the challenge if an error occurs
    ) -> ChallengeCreateResult:
        """Creates a challenge
        
        Parameters
        ----------
        name : str
            The name of the challenge
        category : str
            The category of the challenge
        description : str
            The description of the challenge
        type : str, optional
            The type of the challenge, by default ChallengeType.standard
        state : str, optional
            The state of the challenge, by default ChallengeState.visible
        flag : str, optional
            The flag of the challenge, by default None
        flag_type : str, optional
            The type of the flag, by default FlagType.static
        case_insensitive : bool, optional
            Whether the flag is case insensitive, by default False
        flags : list[tuple[str, str, bool]], optional
            A list of flags, by default None
        value : int, optional
            The value of the challenge, by default None
        initial : int, optional
            The initial value of the challenge, by default None
        minimum : int, optional
            The minimum value of the challenge, by default None
        decay : int, optional
            The decay of the challenge, by default None
        connection_info : str, optional
            The connection info of the challenge, by default None
        max_attempts : int, optional
            The max attempts of the challenge, by default None
        hints : list[tuple[str, int]], optional
            A list of hints, by default None
        hints_ordered : bool, optional
            Whether hints require previous hints, by default True
        tags : list[str], optional
            A list of tags, by default None
        topics : list[str], optional
            A list of topics, by default None
        files : list[os.PathLike[Any] | BufferedIOBase], optional
            A list of files, by default None
        requirements : list[BaseChallenge], optional
            A list of requirements, by default None
        delete_on_error : bool, optional
            Whether to delete the challenge if an error occurs, by default True

        Returns
        -------
        ChallengeCreateResult
            The created challenge

        Raises
        ------
        requests.HTTPError
            If the request fails
        ValueError
            If both flag and flags are specified or neither flag nor flags are specified

        """
            
        # Create challenge
        challenge = Challenge(
            name,
            category,
            description,
            type,
            state,
            value,
            initial,
            minimum,
            decay,
            connection_info,
            max_attempts
        )

        # Create flags
        if flag is not None and flags is not None:
            raise ValueError("Cannot specify both flag and flags")
        
        if flag is not None:
            flags = [(flag, flag_type, case_insensitive)]
        elif flags is not None:
            flags = []
        else:
            raise ValueError("Must specify either flag or flags")
        flags = [Flag(flag, CASE_INSENSITIVE if case_insensitive else CASE_SENSITIVE, flag_type) for flag, flag_type, case_insensitive in flags]

        # Create hints
        if hints is not None:
            hints = [Hint(None, content, cost) for content, cost in hints]

        # Create tags
        if tags is not None:
            tags = [Tag(None, tag) for tag in tags]

        # Create topics
        if topics is not None:
            topics = [ChallengeTopic(None, topic) for topic in topics]

        # Create requirements
        if requirements is not None:
            requirements = [Hint(challenge.id) for challenge in requirements]

        return self._create(
            challenge, flags, hints, tags, topics, files, hints_ordered=hints_ordered, delete_on_error=delete_on_error
        )
    

    @overload
    def update(
        self,
        challenge: Challenge,
        /,
        name: str | None = None,
        category: str | None = None,
        description: str | None = None,
        value: int | None = None,
        connection_info: str | None = None,
        max_attempts: int | None = None,
        state: str | None = None
    ) -> ChallengeCreateResult:
        ...

    @overload
    def update(
        self,
        challenge: Challenge,
        /,
        name: str | None = None,
        category: str | None = None,
        description: str | None = None,
        initial: int | None = None,
        minimum: int | None = None,
        decay: int | None = None,
        connection_info: str | None = None,
        max_attempts: int | None = None,
        state: str | None = None
    ) -> ChallengeCreateResult:
        ...

    @overload
    def update(
        self,
        challenge_id: int,
        /,
        name: str | None = None,
        category: str | None = None,
        description: str | None = None,
        value: int | None = None,
        connection_info: str | None = None,
        max_attempts: int | None = None,
        state: str | None = None
    ) -> ChallengeCreateResult:
        ...

    @overload
    def update(
        self,
        challenge_id: int,
        /,
        name: str | None = None,
        category: str | None = None,
        description: str | None = None,
        initial: int | None = None,
        minimum: int | None = None,
        decay: int | None = None,
        connection_info: str | None = None,
        max_attempts: int | None = None,
        state: str | None = None
    ) -> ChallengeCreateResult:
        ...


    def update(self, challenge_or_id: Challenge | int, **kwargs) -> ChallengeCreateResult:
        """Updates a challenge

        You can pass either a challenge object or a challenge id

        If a challenge object is passed, and parameters are passed in kwargs,
        the challenge object will be updated with the parameters in kwargs
        
        Parameters
        ----------
        challenge_or_id : Challenge | int
            The challenge or challenge id
        name : str, optional
            The name of the challenge, by default None
        category : str, optional
            The category of the challenge, by default None
        description : str, optional
            The description of the challenge, by default None
        value : int, optional
            The value of the challenge, by default None
        initial : int, optional
            The initial value of the challenge, by default None
        minimum : int, optional
            The minimum value of the challenge, by default None
        decay : int, optional
            The decay of the challenge, by default None
        connection_info : str, optional
            The connection info of the challenge, by default None
        max_attempts : int, optional
            The max attempts of the challenge, by default None
        state : str, optional
            The state of the challenge, by default None

        Returns
        -------
        ChallengeCreateResult
            The updated challenge

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        if isinstance(challenge_or_id, Challenge):
            id = challenge_or_id.id
            payload = challenge_or_id.to_payload()
            payload.update(kwargs)
        else:
            id = challenge_or_id
            payload = kwargs

        res = self._patch(f"/api/v1/challenges/{id}", payload)

        return ChallengeCreateResult.from_dict(res["data"])
    

    def delete(self, challenge_id: int) -> bool:
        """Deletes a challenge
        
        Parameters
        ----------
        challenge_id : int
            The id of the challenge

        Returns
        -------
        bool
            Whether the challenge was successfully deleted

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._delete(f"/api/v1/challenges/{challenge_id}")
        return res["success"]