import os
from io import BufferedIOBase
from typing import Any, Literal, TypedDict, overload

import requests

from CTFdPy.constants import (CASE_INSENSITIVE, CASE_SENSITIVE, ChallengeState,
                              ChallengeType, FlagType)
from CTFdPy.models.challenges import (BaseChallenge, Challenge,
                                      ChallengeCreateResult, ChallengePreview)
from CTFdPy.models.files import File
from CTFdPy.models.flags import Flag
from CTFdPy.models.hints import Hint, PartialHint
from CTFdPy.models.tags import Tag
from CTFdPy.models.topics import ChallengeTopic, Topic, TopicCreateResult
from CTFdPy.models.users import User


class APIResponse(TypedDict):
    success: bool
    data: Any | None
    errors: list[str] | None


class Client:
    def __init__(self, url: str = "http://localhost:8080", token: str | None = None, credentials: tuple[str, str] | None = None):
        self.token = token
        self.credentials = credentials

        if self.token is None and self.credentials is None:
            raise ValueError("Either token or credentials must be provided")

        self.url = url.rstrip("/")

        self.headers = {"Authorization": f"Token {self.token}"}

        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def _get(self, endpoint: str) -> APIResponse:
        """Sends a GET request to the server"""
        response = self.session.get(self.url + endpoint, json="")

        response.raise_for_status()
        response = response.json()
        if not response["success"]:
            raise Exception(response.get("errors") or response["message"])
        
        return response
    
    def _post(self, endpoint: str, json: dict[str, Any]) -> APIResponse:
        """Sends a POST request to the server"""
        response = self.session.post(self.url + endpoint, json=json)

        response.raise_for_status()
        response = response.json()
        if not response["success"]:
            raise Exception(response.get("errors") or response["message"])
        
        return response
    
    def _post_form(self, endpoint: str, **kwargs) -> APIResponse:
        """Sends a POST request to the server with form data"""
        if self.session.cookies.get("session") is None:
            # Auto login
            if self.credentials is None:
                raise ValueError("Unable to auto login as credentials are not provided")
            self.login(*self.credentials)

        response = self.session.post(self.url + endpoint, allow_redirects=False, **kwargs)
        
        # Error handling
        response.raise_for_status()
        response = response.json()
        if not response["success"]:
            raise Exception(response.get("errors") or response["message"])
        
        return response

    def _patch(self, endpoint: str, json: dict[str, Any]) -> APIResponse:
        """Sends a PATCH request to the server"""
        response = self.session.patch(self.url + endpoint, json=json)

        response.raise_for_status()
        response = response.json()
        if not response["success"]:
            raise Exception(response.get("errors") or response["message"])
        
        return response
    
    def _delete(self, endpoint: str) -> APIResponse:
        """Sends a DELETE request to the server"""
        response = self.session.delete(self.url + endpoint, json="")
        
        response.raise_for_status()
        response = response.json()
        if not response["success"]:
            raise Exception(response.get("errors") or response["message"])
        
        return response
    

    def login(self, username: str, password: str) -> None:
        """Logs in to the server

        This should only be used if you do not want to use a token,
        or before sending a POST request with form data.

        Parameters
        ----------
        username : str
            The username of the user
        password : str
            The password of the user

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        r = self.session.post(f"{self.url}/login", data={"name": username, "password": password})
        r.raise_for_status()



    # User related operations

    def get_user(self, user_id: int) -> User:
        """Gets a user by id
        
        NOTE: This is accessible even to non-admins
        
        Parameters
        ----------
        user_id : int
            The id of the user
            
        Returns
        -------
        User
            The user

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get(f"/api/v1/users/{user_id}")
            
        return User.from_dict(res["data"])
    

    def get_users(self) -> list[User]:
        """Gets all users

        Returns
        -------
        list[User]
            A list of users

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get("users")
            
        return [User.from_dict(user) for user in res["data"]]
    

    def _create_user(self, user: User) -> User:
        res = self._post("/api/v1/users", user.to_payload()) 
        return User.from_dict(res["data"])
    
    def create_user(self, username: str, email: str, password: str | None = None) -> User:
        """Creates a user
        
        Parameters
        ----------
        username : str
            The username of the user
        email : str
            The email of the user
        password : str, optional
            The password of the user, if it is not provided, a random password will be generated

        Returns
        -------
        User
            The created user

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        return self._create_user(User(username, email, password))
    
    # TODO: Implement update_user, delete_user
    

    # File related operations

    def get_file(self, file_id: int) -> File:
        """Gets a file by id
        
        Parameters
        ----------
        file_id : int
            The id of the file

        Returns
        -------
        File
            The file

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get(f"/api/v1/files/{file_id}")

        return File.from_dict(res["data"])


    def get_files(self) -> list[dict[str, Any]]:
        """Gets all files
        
        Returns
        -------
        list[dict[str, Any]]
            A list of files

        Raises
        ------
        requests.HTTPError
            If the request fails
    
        """
        res = self._get("/api/v1/files")

        return [File.from_dict(file) for file in res["data"]]

    def create_file(self, challenge_id: int, *file: os.PathLike[Any] | BufferedIOBase) -> bool:
        """Creates a file
        
        Parameters
        ----------
        challenge_id : int
            The id of the challenge
        file : os.PathLike[Any] | BufferedIOBase
            The files to upload. Can be a path or a file object

        Returns
        -------
        bool
            Whether the file was successfully uploaded

        Raises
        ------
        requests.HTTPError
            If the request fails
        ValueError
            If the file is not readable

        """

        files = []
        for f in file:
            if isinstance(f, BufferedIOBase):
                if not f.readable():
                    raise ValueError("File must be readable")
            elif os.path.isfile(f):
                f = open(f, "rb")
            else:
                raise ValueError("File must be a path or a readable")
            
            files.append(("file", (f.name, f)))

        print(files)
        
        res = self._post_form("/api/v1/files", data={"challenge_id": challenge_id, "type": "challenge"}, files=files)
        return res["success"]

    def delete_file(self, file_id: int) -> bool:
        """Deletes a file
        
        Parameters
        ----------
        file_id : int
            The id of the file

        Returns
        -------
        bool
            Whether the file was successfully deleted

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._delete(f"/api/v1/files/{file_id}")
        return res["success"]
    

    # Flag related operations
    
    def get_flag(self, flag_id: int) -> Flag:
        """Gets a flag by id
        
        Parameters
        ----------
        flag_id : int
            The id of the flag

        Returns
        -------
        Flag
            The flag

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get(f"/api/v1/flags/{flag_id}")
            
        return Flag.from_dict(res["data"])
    

    def get_flags(self) -> list[Flag]:
        """Gets all flags
        
        Returns
        -------
        list[Flag]
            A list of flags

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get("/api/v1/flags")
            
        return [Flag(**flag) for flag in res["data"]]
    

    def _create_flag(self, flag: Flag) -> Flag:
        res = self._post("/api/v1/flags", flag.to_payload())
        return Flag.from_dict(res["data"])
    
    # TODO: Allow this to take in a challenge or challenge id

    def create_flag(
        self,
        flag: str,
        challenge_id: int,
        type: str = FlagType.static,
        case_insensitive: bool = False
    ) -> Flag:
        """Creates a flag
        
        Flag can either be a static flag or a regex flag

        Parameters
        ----------
        flag : str
            The flag
        challenge_id : int
            The id of the challenge

        Returns
        -------
        Flag
            The created flag

        Raises
        ------
        requests.HTTPError
            If the request fails
        ValueError
            If the flag type is invalid

        """

        data = CASE_INSENSITIVE if case_insensitive else CASE_SENSITIVE
        return self._create_flag(Flag(flag, challenge_id, data, type))
    

    @overload
    def update_flag(
        self,
        flag: Flag,
        /,
        type: str | None = None,
        case_sensitive: bool | None = None,
        content: str | None = None
    ) -> Flag:
        ...

    @overload
    def update_flag(
        self,
        flag_id: int,
        /,
        type: str | None = None,
        case_sensitive: bool | None = None,
        content: str | None = None
    ) -> Flag:
        ...

    def update_flag(
        self,
        flag_or_id: Flag | int,
        /,
        **kwargs
    ) -> Flag:
        """Updates a flag
        You can pass either a flag object or a flag id
        It's recommended to pass a flag object as it's easier to work with at the moment

        Set an argument to None to not update it

        Parameters
        ----------
        flag_or_id : Flag | int
            The flag or flag id
        type : str, optional
            The type of the flag, by default None
        case_sensitive : bool, optional
            Whether the flag is case sensitive, by default None
        content : str, optional
            The flag, by default None

        Returns
        -------
        Flag
            The updated flag

        Raises
        ------
        requests.HTTPError
            If the request fails
        ValueError
            If the flag type is invalid

        """
        case_sensitive = kwargs.pop("case_sensitive", None)
        if case_sensitive is not None:
            kwargs["data"] = CASE_SENSITIVE if case_sensitive else CASE_INSENSITIVE

        if isinstance(flag_or_id, Flag):
            flag = flag_or_id
            flag_id = flag.id
            kwargs.update(flag.to_payload()) # TODO: Change this
        else:
            flag = None
            flag_id = flag_or_id
        
        res = self._patch(f"/api/v1/flags/{flag_id}", kwargs)
        
        return Flag(**res["data"])
    
    def delete_flag(self, flag_id: int) -> bool:
        """Deletes a flag
        
        Parameters
        ----------
        flag_id : int
            The id of the flag

        Returns
        -------
        bool
            Whether the flag was successfully deleted

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._delete(f"/api/v1/flags/{flag_id}")
        return res["success"]
    

    # Hint related operations

    def get_hint(self, hint_id: int) -> Hint:
        """Gets a hint by id
        
        Parameters
        ----------
        hint_id : int
            The id of the hint

        Returns
        -------
        Hint
            The hint

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get(f"/api/v1/hints/{hint_id}")

        return Hint.from_dict(res["data"])
    

    def get_hints(self) -> list[PartialHint]:
        """Gets all hints

        Note: This only returns partial hints

        Returns
        -------
        list[PartialHint]
            A list of partial hints
        """
        res = self._get("/api/v1/hints")

        return [PartialHint.from_dict(hint) for hint in res["data"]]
    

    def _create_hint(self, hint: Hint) -> Hint:
        res = self._post("/api/v1/hints", hint.to_payload())
        return Hint.from_dict(res["data"])
    
    def create_hint(
        self,
        challenge_or_id: Challenge | int,
        content: str,
        cost: int,
        requirements: list[Hint] | None = None
    ) -> Hint:
        """Creates a hint
        
        Parameters
        ----------
        challenge_or_id : Challenge | int
            The challenge or challenge id
        content : str
            The content of the hint
        cost : int
            The cost of the hint
        requirements : list[Hint], optional
            The hints required to unlock this hint, by default None

        Returns
        -------
        Hint
            The created hint
        """
        if isinstance(challenge_or_id, BaseChallenge):
            challenge_id = challenge_or_id.id

        hint = Hint(challenge_id, content, cost)

        if requirements is not None:
            hint.set_requirements(*requirements)

        return self._create_hint(hint)
    

    @overload
    def update_hint(
        self,
        hint: Hint,
        /,
        content: str | None = None,
        cost: int | None = None,
        requirements: list[Hint] | None = None
    ) -> Hint:
        ...

    @overload
    def update_hint(
        self,
        hint_id: int,
        /,
        content: str | None = None,
        cost: int | None = None,
        requirements: list[Hint] | None = None
    ) -> Hint:
        ...

    def update_hint(
        self,
        hint_or_id: Hint | int,
        /,
        **kwargs
    ) -> Hint:
        """Updates a hint
        You can pass either a hint object or a hint id
        It's recommended to pass a hint object as it's easier to work with at the moment

        Set an argument to None to not update it

        Parameters
        ----------
        hint_or_id : Hint | int 
            The hint or hint id
        content : str, optional
            The content of the hint, by default None
        cost : int, optional
            The cost of the hint, by default None
        requirements : list[Hint], optional
            The hints required to unlock this hint, by default None

        Returns
        -------
        Hint
            The updated hint

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        requirements: list[Hint] = kwargs.pop("requirements", None)

        if not isinstance(hint_or_id, Hint):
            hint = Hint(id=hint_or_id, **kwargs)
        else:
            hint = hint_or_id

        if requirements is not None:
            hint.add_requirements(*requirements)
        
        res = self._patch(f"/api/v1/hints/{hint.id}", hint.to_payload())
        
        return Hint.from_dict(res["data"])
    

    def delete_hint(self, hint_id: int) -> bool:
        """Deletes a hint
        
        Parameters
        ----------
        hint_id : int   
            The id of the hint

        Returns
        -------
        bool
            Whether the hint was successfully deleted

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._delete(f"/api/v1/hints/{hint_id}")
        return res["success"]
    

    # Tag related operations

    def get_tag(self, tag_id: int) -> Tag:
        """Gets a tag by id
        
        Parameters
        ----------
        tag_id : int
            The id of the tag

        Returns
        -------
        Tag
            The tag

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get(f"/api/v1/tags/{tag_id}")

        return Tag.from_dict(res["data"])


    def get_tags(self) -> list[Tag]:
        """Gets all tags
        
        Returns
        -------
        list[Tag]
            A list of tags

        Raises
        ------
        requests.HTTPError
            If the request fails
        """
        res = self._get("/api/v1/tags")

        return [Tag.from_dict(tag) for tag in res["data"]]


    def _create_tag(self, tag: Tag) -> Tag:
        res = self._post("/api/v1/tags", tag.to_payload())
        return Tag.from_dict(res["data"])  
    
    def create_tag(self, challenge_or_id: BaseChallenge | int, value: str) -> Tag:
        """Creates a tag
        
        Parameters
        ----------
        challenge_or_id : BaseChallenge | int
            The challenge or challenge id
        value : str
            The value of the tag

        Returns
        -------
        Tag
            The created tag

        """
        if isinstance(challenge_or_id, BaseChallenge):
            challenge_id = challenge_or_id.id
        else:
            challenge_id = challenge_or_id
        
        return self._create_tag(Tag(challenge_id, value))
    

    def update_tag(self, tag_or_id: Tag | int, value: str) -> Tag:
        """Updates a tag
        
        Parameters
        ----------
        tag_or_id : Tag | int
            The tag or tag id
        value : str
            The value of the tag

        Returns
        -------
        Tag
            The updated tag

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        if isinstance(tag_or_id, Tag):
            tag = tag_or_id
            tag.value = value
        else:
            tag = Tag(id=tag_or_id, value=value)
        
        res = self._patch(f"/api/v1/tags/{tag.id}", tag.to_payload())

        return Tag.from_dict(res["data"])
    

    def delete_tag(self, tag_id: int) -> bool:
        """Deletes a tag
        
        Parameters
        ----------
        tag_id : int
            The id of the tag
        
        Returns
        -------
        bool
            Whether the tag was successfully deleted

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._delete(f"/api/v1/tags/{tag_id}")
        return res["success"]
    

    # Topic related operations

    def get_topic(self, topic_id: int) -> Topic:
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
    

    def get_topics(self) -> list[Topic]:
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
    

    def _create_topic(self, topic: ChallengeTopic) -> TopicCreateResult:
        res = self._post("/api/v1/topics", topic.to_payload())
        return TopicCreateResult.from_dict(res["data"])
    
    def create_topic(self, challenge_or_id: BaseChallenge, value: str) -> TopicCreateResult:
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
        
        return self._create_topic(ChallengeTopic(challenge_id, value))
    

    def delete_topic(self, topic_id: int) -> bool:
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


    # Challenge related operations

    def get_challenge(self, challenge_id: int) -> Challenge:
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
    

    def get_visible_challenges(self) -> list[ChallengePreview]:
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
    

    def get_challenges(self) -> list[Challenge]:
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
    

    def _create_challenge(
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
                self._create_flag(flag)

            # Create hints
            last_hint = None
            if hints is not None:
                for hint in hints:
                    if hints_ordered:
                        if last_hint is not None:
                            hint.set_requirements(last_hint)
                    hint.challenge_id = challenge_result.id
                    hint = self._create_hint(hint)
                    last_hint = hint

            # Create tags
            if tags is not None:
                for tag in tags:
                    tag.challenge_id = challenge_result.id
                    self._create_tag(tag)

            # Create topics
            if topics is not None:
                for topic in topics:
                    topic.challenge_id = challenge_result.id
                    self._create_topic(topic)

            # Create files
            if files is not None:
                self.create_file(challenge_result.id, *files)

        except Exception as e:
            if delete_on_error:
                self.delete_challenge(challenge_result.id)
            raise e from e
        
        return challenge_result
    

    @overload
    def create_challenge(
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
    def create_challenge(
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

    def create_challenge(
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

        return self._create_challenge(
            challenge, flags, hints, tags, topics, files, hints_ordered=hints_ordered, delete_on_error=delete_on_error
        )
    

    def delete_challenge(self, challenge_id: int) -> bool:
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
    

