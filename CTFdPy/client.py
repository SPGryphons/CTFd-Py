from __future__ import annotations

import os

import requests

from CTFdPy.api import *


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

        self._challenges_api = ChallengesAPI(self)
        self._files_api = FilesAPI(self)
        self._flags_api = FlagsAPI(self)
        self._hints_api = HintsAPI(self)
        self._tags_api = TagsAPI(self)
        self._teams_api = TeamsAPI(self)
        self._topics_api = TopicsAPI(self)
        self._users_api = UsersAPI(self)


    @classmethod
    def from_env(cls) -> Client:
        """Creates a client from environment variables

        Returns
        -------
        Client
            The client

        Raises
        ------
        ValueError
            If neither token nor credentials are provided

        """
        return cls(
            url=os.environ.get("CTFDPY_URL", "http://localhost:8080"),
            token=os.environ.get("CTFDPY_TOKEN"),
            credentials=(os.environ.get("CTFDPY_USERNAME"), os.environ.get("CTFDPY_PASSWORD"))
        )


    @property
    def challenges(self) -> ChallengesAPI:
        return self._challenges_api


    @property
    def files(self) -> FilesAPI:
        return self._files_api
    

    @property
    def flags(self) -> FlagsAPI:
        return self._flags_api
    

    @property
    def hints(self) -> HintsAPI:
        return self._hints_api
    

    @property
    def tags(self) -> TagsAPI:
        return self._tags_api
    

    @property
    def teams(self) -> TeamsAPI:
        return self._teams_api


    @property
    def topics(self) -> TopicsAPI:
        return self._topics_api
    

    @property
    def users(self) -> UsersAPI:
        return self._users_api
    

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