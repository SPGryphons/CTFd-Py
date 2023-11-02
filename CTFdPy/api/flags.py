from __future__ import annotations

from typing import overload

from CTFdPy.api.api import API
from CTFdPy.constants import CASE_INSENSITIVE, CASE_SENSITIVE, FlagType
from CTFdPy.models.flags import Flag


class FlagsAPI(API):
    def get(self, flag_id: int) -> Flag:
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
    

    def get_all(self) -> list[Flag]:
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

        return [Flag.from_dict(flag) for flag in res["data"]]
    

    def _create(self, flag: Flag) -> Flag:
        res = self._post("/api/v1/flags", flag.to_payload())
        return Flag.from_dict(res["data"])
    

    def create(
        self,
        flag: str,
        challenge_id: int,
        type: str = FlagType.static,
        case_insensitive: bool = False
    ) -> Flag:
        """Creates a flag for a challenge
        
        Flag can either be a static flag or regex flag

        Parameters
        ----------
        flag : str
            The flag
        challenge_id : int
            The id of the challenge to attach the flag to

        Returns
        -------
        requests.HTTPError
            If the request fails
        ValueError
            If the flag type is invalid

        """

        data = CASE_INSENSITIVE if case_insensitive else CASE_SENSITIVE
        return self._create(Flag(flag=flag, challenge_id=challenge_id, type=type, data=data))
    

    @overload
    def update(
        self,
        flag: Flag,
        /,
        type: str | None = None,
        case_sensitive: bool | None = None,
        content: str | None = None
    ) -> Flag:
        ...

    @overload
    def update(
        self,
        flag_id: int,
        /,
        type: str | None = None,
        case_sensitive: bool | None = None,
        content: str | None = None
    ) -> Flag:
        ...

    def update(
        self,
        flag_or_id: Flag | int,
        /,
        **kwargs
    ) -> Flag:
        """Updates a flag
        You can pass either a flag object or a flag id
        It's recommended to pass a flag object

        If a flag object is passed, and parameters are passed in kwargs,
        the flag object will be updated with the parameters in kwargs

        Leave an argument as None to not update it

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
            flag_id = flag_or_id.id
            payload = flag_or_id.to_payload()
            payload.update(kwargs)
        else:
            flag_id = flag_or_id
            payload = kwargs
        
        res = self._patch(f"/api/v1/flags/{flag_id}", payload)
        
        return Flag.from_dict(**res["data"])
    
    def delete(self, flag_id: int) -> bool:
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