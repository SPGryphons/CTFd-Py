from __future__ import annotations

import secrets
import string
from typing import Literal, overload

from CTFdPy.api.api import API
from CTFdPy.models.teams import Team


class TeamsAPI(API):

    @staticmethod
    def _generate_password() -> str:
        return ''.join(secrets.choice(string.ascii_letters) for _ in range(10))
    

    def get(self, team_id: int) -> Team:
        """Gets a team by id
        
        NOTE: This is accessible even to non-admins
        
        Parameters
        ----------
        team_id : int
            The id of the team
            
        Returns
        -------
        Team
            The team

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get(f"/api/v1/teams/{team_id}")
            
        return Team.from_dict(res["data"])
    

    def get_visible(self) -> list[Team]:
        """Gets all visible teams

        NOTE: This is accessible even to non-admins

        Returns
        -------
        list[Team]
            A list of teams

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get("/api/v1/teams")

        return [Team.from_dict(team) for team in res["data"]]
    

    def get_all(self) -> list[Team]:
        """Gets all teams

        NOTE: This is only accessible to admins

        Returns
        -------
        list[Team]
            A list of teams

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get("/api/v1/teams?view=admin")

        return [Team.from_dict(team) for team in res["data"]]
    

    def _create(self, team: Team) -> Team:
        res = self._post("/api/v1/teams", json=team.to_payload())
        return Team.from_dict(res["data"])
    

    def create(
        self,
        name: str,
        password: str | None = None,
        hidden: bool = False,
        banned: bool = False,
        email: str | None = None,
        affiliation: str | None = None,
        website: str | None = None,
        country: str | None = None
    ) -> Team:
        """Creates a team
        
        Parameters
        ----------
        name : str
            The name of the team
        password : str, optional
            The password of the team, if it is not provided, a random password will be generated
        hidden : bool, optional
            Whether the team should be hidden, by default False
        banned : bool, optional
            Whether the team should be banned, by default False
        email : str, optional
            The email of the team, by default None
        affiliation : str, optional
            The affiliation of the team, by default None
        website : str, optional
            The website of the team, by default None
        country : str, optional
            The country of the team, by default None

        Returns
        -------
        Team
            The created team

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        if password is None:
            password = self._generate_password()
        
        return self._create(
            Team(
                name=name,
                password=password,
                hidden=hidden,
                banned=banned,
                email=email,
                affiliation=affiliation,
                website=website,
                country=country
            )
        )
    

    # TODO: Figure out how to update a team


    def delete(self, team_id: int) -> bool:
        """Deletes a team by id
        
        Parameters
        ----------
        team_id : int
            The id of the team

        Returns
        -------
        bool
            Whether the team was deleted successfully

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._delete(f"/api/v1/teams/{team_id}")
        return res["success"]


    def get_member_ids(self, team_id: int) -> list[int]:
        """Gets the ids of the members of a team
        
        Parameters
        ----------
        team_id : int
            The id of the team

        Returns
        -------
        list[int]
            The ids of the members of the team

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get(f"/api/v1/teams/{team_id}/members")
        return res["data"]
    

    def add_member(self, team_id: int, user_id: int) -> bool:
        """Adds a member to a team
        
        Parameters
        ----------
        team_id : int
            The id of the team
        user_id : int
            The id of the user

        Returns
        -------
        bool
            Whether the member was added successfully

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._post(
            f"/api/v1/teams/{team_id}/members",
            json={"user_id": user_id}
        )
        return res["success"]
    

    def remove_member(self, team_id: int, user_id: int) -> bool:
        """Removes a member from a team
        
        Parameters
        ----------
        team_id : int
            The id of the team
        user_id : int
            The id of the user

        Returns
        -------
        bool
            Whether the member was removed successfully

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._delete(
            f"/api/v1/teams/{team_id}/members",
            json={"user_id": str(user_id)} # For some reason CTFd takes a string here
        )
        return res["success"]
    

    def set_captain(self, team_id: int, user_id: int) -> bool:
        """Sets the captain of a team
        
        Parameters
        ----------
        team_id : int
            The id of the team
        user_id : int
            The id of the user

        Returns
        -------
        bool
            Whether the captain was set successfully

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._patch(
            f"/api/v1/teams/{team_id}",
            json={"captain_id": user_id}
        )
        return res["success"]