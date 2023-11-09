from __future__ import annotations

import os
from io import BufferedIOBase
from typing import Any

from CTFdPy.api.api import API
from CTFdPy.models.files import File


class FilesAPI(API):
    def get(self, file_id: int) -> File:
        """Gets a file by id
        
        NOTE: This is accessible even to non-admins
        
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
  

    def get_all(self) -> list[File]:
        """Gets all files

        Returns
        -------
        list[File]
            A list of files

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._get("/api/v1/files")
            
        return [File.from_dict(file) for file in res["data"]]
    

    def create(self, challenge_id: int, *file: os.PathLike[Any] | BufferedIOBase) -> File:
        """Creates files for a challenge

        Parameters
        ----------
        challenge_id : int
            The id of the challenge to attach the file to
        *file : os.PathLike[Any] | BufferedIOBase
            The file to upload

        Returns
        -------
        File
            The created file

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        files = []
        for f in file:
            if isinstance(f, BufferedIOBase):
                if not f.readable():
                    raise ValueError("File must be readable")
                f.seek(0)
            elif isinstance(f, str):
                if os.path.isfile(f):
                    f = open(f, "rb")
                else:
                    raise FileNotFoundError(f"File {f} does not exist")
            else:
                raise ValueError("File must be a path or a readable")
            
            name = os.path.basename(f.name)

            files.append(("file", (name, f)))

        res = self._post_form("/api/v1/files", data={"challenge": challenge_id, "type": "challenge"}, files=files)
        return res["success"]
    

    def delete(self, file_id: int) -> bool:
        """Deletes a file

        Parameters
        ----------
        file_id : int
            The id of the file to delete

        Returns
        -------
        bool
            True if the file was deleted successfully

        Raises
        ------
        requests.HTTPError
            If the request fails

        """
        res = self._delete(f"/api/v1/files/{file_id}")
        return res["success"]