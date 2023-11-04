from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal, TypedDict

if TYPE_CHECKING:
  from CTFdPy.client import Client


class APIResponse(TypedDict):
    success: bool
    data: Any | None
    errors: list[str] | None


class API:
    def __init__(self, client: Client):
        self.client = client
        self.url = client.url
        self.session = client.session


    def _get(self, endpoint: str) -> APIResponse:
        response = self.session.get(self.url + endpoint, json="")

        response.raise_for_status()
        response = response.json()
        if not response["success"]:
            raise Exception(response.get("errors") or response["message"])
        
        return response
    
    
    def _post(self, endpoint: str, json: dict[str, Any]) -> APIResponse:
        response = self.session.post(self.url + endpoint, json=json)

        response.raise_for_status()
        response = response.json()
        if not response["success"]:
            raise Exception(response.get("errors") or response["message"])
        
        return response
    

    def _patch(self, endpoint: str, json: dict[str, Any]) -> APIResponse:
        response = self.session.patch(self.url + endpoint, json=json)

        response.raise_for_status()
        response = response.json()
        if not response["success"]:
            raise Exception(response.get("errors") or response["message"])
        
        return response
    

    def _delete(self, endpoint: str, json: dict[str, Any] | Literal[""] = "") -> APIResponse:
        response = self.session.delete(self.url + endpoint, json=json)

        response.raise_for_status()
        response = response.json()
        if not response["success"]:
            raise Exception(response.get("errors") or response["message"])
        
        return response
    

    def _post_form(self, endpoint: str, **kwargs) -> APIResponse:
        if self.session.cookies.get("session") is None:
            if self.client.credentials is None:
                raise ValueError("Unable to auto login as credentials are not provided")
            self.login(*self.client.credentials)

        response = self.session.post(self.url + endpoint, allow_redirects=False, **kwargs)

        response.raise_for_status()
        response = response.json()
        if not response["success"]:
            raise Exception(response.get("errors") or response["message"])
        
        return response