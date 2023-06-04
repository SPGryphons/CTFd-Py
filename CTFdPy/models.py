from __future__ import annotations

from dataclasses import dataclass

from typing import Generic, TypeVar


DictT = TypeVar("DictT", bound=dict[str, any])


class Model(Generic[DictT]):
    """The base model for all models"""
    _raw: DictT | None = None

    @classmethod
    def from_dict(cls, d: DictT) -> Model:
        """Creates a model from a dictionary, and ingnores any extra keys"""
        c = cls(
            **{
                k: v for k, v in d.items()
                if k in cls.__dataclass_fields__.keys()
            }
        )
        c._raw = d
    
    @property
    def _to_dict(self) -> DictT:
        """Returns a dictionary representation of the model 
        excluding private attributes
        """
        return {
            k: v for k, v in self.__dataclass_fields__.items()
            if not k.startswith("_")
        }

    @property
    def raw(self) -> DictT:
        """Returns the raw dictionary representation of the model"""
        return self._raw if self._raw is not None else self._to_dict