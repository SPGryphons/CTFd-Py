from __future__ import annotations

from typing import overload

from CTFdPy.api.api import API
from CTFdPy.models.challenges import BaseChallenge
from CTFdPy.models.tags import Tag


class TagsAPI(API):
    def get(self, tag_id: int) -> Tag:
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


    def get_all(self) -> list[Tag]:
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


    def _create(self, tag: Tag) -> Tag:
        res = self._post("/api/v1/tags", tag.to_payload())
        return Tag.from_dict(res["data"])  
    
    
    def create(self, challenge_or_id: BaseChallenge | int, value: str) -> Tag:
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
        
        return self._create(Tag(challenge_id=challenge_id, value=value))
    

    def update(self, tag_id: int, value: str) -> Tag:
        """Updates a tag
        
        Parameters
        ----------
        tag_id : int
            The tag id
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
        
        res = self._patch(f"/api/v1/tags/{tag_id}", {"value": value})

        return Tag.from_dict(res["data"])
    

    def delete(self, tag_id: int) -> bool:
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