from __future__ import annotations
import secrets
import string
from typing import Literal

from CTFdPy.api.api import API
from CTFdPy.constants import UserType
from CTFdPy.models.users import User


class UsersAPI(API):
    
    @staticmethod
    def _generate_password() -> str:
        return ''.join(secrets.choice(string.ascii_letters) for _ in range(10))

    def get(self, user_id: int) -> User:
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
    

    def get_visible(self) -> list[User]:
        """Gets all visible users

        NOTE: This is accessible even to non-admins

        Returns
        -------
        list[User]
            A list of users

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get("/api/v1/users")

        # NOTE:
        # Data returned from this endpoint does not contain all the fields
        # key fields such as email is missing.
        # In order to get the full user data, you need to access each user individually

        # TODO: Maybe create a `PartialUser` class that contains only the fields returned by this endpoint
            
        return [User.from_dict(user) for user in res["data"]]
    

    def get_all(self) -> list[User]:
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
        res = self._get("/api/v1/users?view=admin")

        # NOTE:
        # Refer to the note in `get_visible`
            
        return [User.from_dict(user) for user in res["data"]]
    

    def _create(self, user: User, notify: bool) -> User:
        endpoint = "/api/v1/users"
        if notify:
            endpoint += "?notify=true"
        res = self._post(endpoint, user.to_payload())
        return User.from_dict(res["data"])
    

    def create(
        self,
        name: str,
        email: str,
        password: str | None = None,
        type: Literal["admin", "user"] = UserType.user,
        verified: bool = False,
        banned: bool = False,
        hidden: bool = False,
        website: str | None = None,
        country: str | None = None,
        affiliation: str | None = None,
        notify: bool = False
    ) -> User:
        """Creates a user
        
        Parameters
        ----------
        name : str
            The name of the user
        email : str
            The email of the user
        password : str, optional
            The password of the user, if it is not provided, a random password will be generated
        type : Literal["admin", "user"], optional
            The type of the user, by default UserType.user
        verified : bool, optional
            Whether the user is verified, by default False
        banned : bool, optional
            Whether the user is banned, by default False
        hidden : bool, optional
            Whether the user is hidden, by default False
        website : str, optional
            The website of the user, by default None
        country : str, optional
            The country of the user, by default None
        affiliation : str, optional
            The affiliation of the user, by default None
        notify : bool, optional
            Whether to notify the user of their account creation, by default False

        Returns
        -------
        User
            The created user

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        if password is None or password == "":
            password = self._generate_password()

        return self._create(
            User(name, email, password, type, verified, banned, hidden, website, country, affiliation),
            notify
        )
    
    # TODO: Implement update_user, delete_user