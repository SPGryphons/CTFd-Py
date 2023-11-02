from __future__ import annotations

from typing import overload

from CTFdPy.api.api import API
from CTFdPy.models.challenges import BaseChallenge, Challenge
from CTFdPy.models.hints import Hint, PartialHint


class HintsAPI(API):
    def get(self, hint_id: int) -> Hint:
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
    

    def get(self) -> list[PartialHint]:
        """Gets all hints

        Returns
        -------
        list[Hint]
            A list of hints

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get("/api/v1/hints")

        return [PartialHint.from_dict(hint) for hint in res["data"]]
    

    def _create(self, hint: Hint) -> Hint:
        res = self._post("/api/v1/hints", hint.to_payload())
        return Hint.from_dict(res["data"])
    

    def create(
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

        return self._create(hint)
    

    @overload
    def update(
        self,
        hint: Hint,
        /,
        content: str | None = None,
        cost: int | None = None,
        requirements: list[Hint] | None = None
    ) -> Hint:
        ...

    @overload
    def update(
        self,
        hint_id: int,
        /,
        content: str | None = None,
        cost: int | None = None,
        requirements: list[Hint] | None = None
    ) -> Hint:
        ...

    def update(
        self,
        hint_or_id: Hint | int,
        /,
        **kwargs
    ) -> Hint:
        """Updates a hint
        You can pass either a hint object or a hint id
        It's recommended to pass a hint object as it's easier to work with at the moment

        Leave an argument as None to not update it

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
            hint = Hint(id=hint_or_id, content=kwargs.pop("content", None), **kwargs)
        else:
            hint = hint_or_id

        if requirements is not None:
            hint.add_requirements(*requirements)
        
        res = self._patch(f"/api/v1/hints/{hint.id}", hint.to_payload())
        
        return Hint.from_dict(res["data"])
    

    def delete(self, hint_id: int) -> bool:
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