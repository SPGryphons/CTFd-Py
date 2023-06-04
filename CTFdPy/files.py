from __future__ import annotations

from dataclasses import dataclass

from CTFdPy.models import Model
from CTFdPy.types.files import FileDict


@dataclass
class File(Model[FileDict]):
    """Represents a file"""
    id: int = None
    location: str = None
    type: str = None