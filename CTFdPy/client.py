import requests
from typing import Any, Literal, TypedDict, overload

from CTFdPy.constants import ChallengeType, ChallengeState, FlagType
from CTFdPy.challenges import Challenge
from CTFdPy.flags import Flag
from CTFdPy.users import User


class APIResponse(TypedDict):
    success: bool
    data: Any | None
    errors: list[str] | None


class Client:
    def __init__(self, token: str, url: str = "http://localhost:8080"):
        self.token = token

        if url.endswith("/"):
            url = url[:-1]
        self.url = url

        self.headers = {"Authorization": f"Token {self.token}"}

        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def _get(self, endpoint: str) -> APIResponse:
        """Sends a GET request to the server"""
        return self.session.get(f"{self.url}/api/v1/{endpoint}", json="").json()
    
    def _post(self, endpoint: str, data: dict[str, str | int]) -> APIResponse:
        """Sends a POST request to the server"""
        return self.session.post(f"{self.url}/api/v1/{endpoint}", json=data).json()
    
    def _patch(self, endpoint: str, data: dict[str, str | int]) -> APIResponse:
        """Sends a PATCH request to the server"""
        return self.session.patch(f"{self.url}/api/v1/{endpoint}", json=data).json()
    
    def _delete(self, endpoint: str) -> APIResponse:
        """Sends a DELETE request to the server"""
        return self.session.delete(f"{self.url}/api/v1/{endpoint}", json="").json()
    

    # User related operations

    # NOTE: This currently will not work
    def get_user(self, user_id: int) -> User:
        """Gets a user by id"""
        res = self._get(f"users/{user_id}")
        if res["success"]:
            return User(**res["data"])
        
        raise Exception(res["errors"])
    

    # NOTE: This currently will not work
    def get_users(self) -> list[User]:
        """Gets all users"""
        res = self._get("users")
        if res["success"]:
            return [User(**user) for user in res["data"]]
        
        raise Exception(res["errors"])
    

    def _create_user(self, user: User) -> User:
        """Creates a user"""
        res = self._post("users", user.to_dict())
        if res["success"]:
            return user.to_dict()
            # Do this for now until I have time to fully implement users
            # return User(**res["data"])
        
        raise Exception(res["errors"])
    
    def create_user(self, username: str, email: str, password: str | None = None) -> User:
        """Creates a user"""
        return self._create_user(User(username, email, password))
    
    # TODO: Implement update_user, delete_user
    

    # Flag related operations
    
    def get_flag(self, flag_id: int) -> Flag:
        """Gets a flag by id"""
        res = self._get(f"flags/{flag_id}")
        if res["success"]:
            return Flag(**res["data"])
        
        raise Exception(res["errors"])
    

    def get_flags(self) -> list[Flag]:
        """Gets all flags"""
        res = self._get("flags")
        if res["success"]:
            return [Flag(**flag) for flag in res["data"]]
        
        raise Exception(res["errors"])
    

    def _create_flag(self, flag: Flag) -> Flag:
        """Creates a flag"""
        res = self._post("flags", flag.to_dict())
        if res["success"]:
            return Flag(**res["data"])
        
        raise Exception(res["errors"])
    
    # TODO: Fix this to take in challenge or challenge id

    def create_flag(
        self,
        flag: str,
        type: str = FlagType.static,
        case_insensitive: bool = False
    ) -> Flag:
        """Creates a flag
        
        Flag can either be a static flag or a regex flag
        """

        data = "case_insensitive" if case_insensitive else ""
        return self._create_flag(Flag(flag, data, type))
    

    @overload
    def update_flag(self, flag: Flag, /, **kwargs) -> Flag:
        ...

    @overload
    def update_flag(self, flag_id: int, /, **kwargs) -> Flag:
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
        """
        if isinstance(flag_or_id, Flag):
            flag = flag_or_id
            flag_id = flag.id
            kwargs = flag.to_dict()
            kwargs.update(kwargs)
        else:
            flag = None
            flag_id = flag_or_id
        
        res = self._patch(f"flags/{flag_id}", kwargs)
        if res["success"]:
            return Flag(**res["data"])
        
        raise Exception(res["errors"])
    
    def delete_flag(self, flag_id: int) -> bool:
        """Deletes a flag"""
        res = self._delete(f"flags/{flag_id}")
        if res["success"]:
            return True
        
        raise Exception(res["errors"])


    # Challenge related operations

    # TODO: Refactor this to use the new challenge data types

    # def get_challenge(self, challenge_id: int) -> Challenge:
    #     """Gets a challenge by id"""
    #     res = self._get(f"challenges/{challenge_id}")
    #     if res["success"]:
    #         return Challenge(**res["data"])
        
    #     raise Exception(res["errors"])
    
    
    # def get_challenges(self) -> list[Challenge]:
    #     """Gets all challenges"""
    #     res = self._get("challenges")
    #     if res["success"]:
    #         return [Challenge(**challenge) for challenge in res["data"]]
        
    #     raise Exception(res["errors"])
    

    # def _create_challenge(self, challenge: Challenge, flag: Flag) -> tuple[Challenge, Flag]:
    #     """Creates a challenge"""
    #     res = self._post("challenges", challenge.to_dict())
    #     if res["success"]:
    #         challenge = Challenge(**res["data"])

    #         # Create the flag
    #         flag.challenge_id = challenge.id
    #         flag = self._create_flag(flag)

    #         if res["success"]:
    #             return challenge, flag
        
    #     raise Exception(res["errors"])
    
    # @overload
    # def create_challenge(
    #     self,
    #     name: str,
    #     category: str,
    #     description: str,
    #     flag: str,
    #     type: str = ChallengeType.standard,
    #     flag_type: str = FlagType.static,
    #     case_insensitive: bool = False,
    #     *,
    #     value: int | None = None,
    #     state: str | None = None,
    #     connection_info: str | None = None,
    #     max_attempts: int | None = None,
    #     requirements: list[Challenge] | None = None
    # ) -> tuple[Challenge, Flag]:
    #     ...

    # @overload
    # def create_challenge(
    #     self,
    #     name: str,
    #     category: str,
    #     description: str,
    #     flag: str,
    #     type: str = ChallengeType.dynamic,
    #     flag_type: str = FlagType.static,
    #     case_insensitive: bool = False,
    #     *,
    #     initial: int | None = None,
    #     minimum: int | None = None,
    #     decay: int | None = None,
    #     state: str | None = None,
    #     connection_info: str | None = None,
    #     max_attempts: int | None = None,
    #     requirements: list[Challenge] | None = None
    # ) -> tuple[Challenge, Flag]:
    #     ...
    
    # def create_challenge(
    #     self,
    #     name: str,
    #     category: str,
    #     description: str,
    #     flag: str,
    #     type: str = ChallengeType.standard,
    #     flag_type: str = FlagType.static,
    #     case_insensitive: bool = False,
    #     *,
    #     value: int | None = None,
    #     initial: int | None = None,
    #     minimum: int | None = None,
    #     decay: int | None = None,
    #     state: str = ChallengeState.hidden,
    #     connection_info: str | None = None,
    #     max_attempts: int | None = None
    # ) -> tuple[Challenge, Flag]:
    #     """Creates a challenge
    #     Challenge can either be a standard challenge or a dynamic challenge

    #     Standard challenges require a value parameter
    #     Dynamic challenges require initial, minimum, and decay parameters

    #     Note that `value`, `initial`, `minimum`, `decay` are keyword-only arguments

    #     Flag can either be a static flag or a regex flag
    #     """
    #     if type == ChallengeType.standard:
    #         if value is None:
    #             raise ValueError("Standard challenges require a value parameter")
    #         if any([initial, minimum, decay]):
    #             raise ValueError("Standard challenges cannot have initial, minimum, or decay parameters")
            
    #         challenge = Challenge(name, category, description, type, value=value)

    #     elif type == ChallengeType.dynamic:
    #         if not all([initial, minimum, decay]):
    #             raise ValueError("Dynamic challenges require initial, minimum, and decay parameters")
    #         if value is not None:
    #             raise ValueError("Dynamic challenges cannot have a value parameter")

    #         challenge = Challenge(name, category, description, type, initial=initial, minimum=minimum, decay=decay)
    #     else:
    #         raise ValueError("Invalid challenge type")
        
    #     if flag is not None:
    #         flag = Flag(flag, "case_insensitive" if case_insensitive else "", flag_type)
        
    #     challenge, flag = self._create_challenge(challenge, flag)

    #     # Check if we need to make a PATCH request for the remaining parameters
    #     if any([state, connection_info, max_attempts]): # This should be fine
    #         # TODO: Implement requirements
    #         challenge = self.update_challenge(
    #             challenge.id,
    #             state=state,
    #             connection_info=connection_info,
    #             max_attempts=max_attempts
    #         )


    # def _update_challenge(self, challenge: Challenge) -> Challenge:
    #     """Updates a challenge"""
    #     res = self._patch(f"challenges/{challenge.id}", challenge.to_dict())
    #     if res["success"]:
    #         return Challenge(**res["data"])
        
    #     raise Exception(res["errors"])
    
    # @overload
    # def update_challenge(
    #     self,
    #     challenge: Challenge,
    #     /,
    #     name: str | None = None,
    #     category: str | None = None,
    #     description: str | None = None,
    #     type: str | None = None,
    #     value: int | None = None,
    #     initial: int | None = None,
    #     minimum: int | None = None,
    #     decay: int | None = None,
    #     state: str | None = None,
    #     connection_info: str | None = None,
    #     max_attempts: int | None = None,
    #     next_id: Challenge | None = None
    # ) -> Challenge:
    #     ...

    # @overload
    # def update_challenge(
    #     self,
    #     challenge_id: int,
    #     /,
    #     name: str | None = None,
    #     category: str | None = None,
    #     description: str | None = None,
    #     type: str | None = None,
    #     value: int | None = None,
    #     initial: int | None = None,
    #     minimum: int | None = None,
    #     decay: int | None = None,
    #     state: str | None = None,
    #     connection_info: str | None = None,
    #     max_attempts: int | None = None,
    #     requirements: list[Challenge] | None = None,
    #     anonymize: Literal[True] | None = None,
    #     next_id: Challenge | None = None
    # ) -> Challenge:
    #     ...
    
    # def update_challenge(self, challenge_or_id: Challenge | int, /, **kwargs) -> Challenge:
    #     """Updates a challenge
    #     You can pass either a challenge object or a challenge id
    #     """
    #     requirements = kwargs.pop("requirements", None)
    #     anonymize = kwargs.pop("anonymize", None)
    #     next_id = kwargs.pop("next_challenge", None)

    #     if isinstance(challenge_or_id, Challenge):
    #         if anonymize or requirements:
    #             raise ValueError("Anonymize and requirements cannot be set when passing a challenge object")

    #         challenge = challenge_or_id

    #         # TODO: Probably implement this better
    #         kwargs = challenge.to_dict()
    #         kwargs.update(kwargs)
    #         challenge = Challenge(**kwargs)
    #     else:
    #         if anonymize and requirements is None:
    #             raise ValueError("Anonymize requires requirements to be set")
    #         challenge = Challenge(**kwargs)
    #         challenge.set_requirements(requirements, anonymize)

    #     if next_id is not None:
    #         if not isinstance(next_id, Challenge):
    #             raise ValueError("Next challenge must be of type Challenge")
    #         if next_id.id is None:
    #             raise ValueError("Challenge must be created before it can be used as a next challenge")
    #         else:
    #             challenge.next_id = next_id.id
        
    #     return self._update_challenge(challenge)
    
    # # TODO: Implement delete_challenge
    # # Fully implement update_challenge