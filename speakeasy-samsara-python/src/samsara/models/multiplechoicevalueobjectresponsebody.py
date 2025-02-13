"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class MultipleChoiceValueObjectResponseBodyTypedDict(TypedDict):
    selected: NotRequired[bool]
    r"""Boolean representing if the choice has been selected."""
    value: NotRequired[str]
    r"""Description of the choice."""


class MultipleChoiceValueObjectResponseBody(BaseModel):
    selected: Optional[bool] = None
    r"""Boolean representing if the choice has been selected."""

    value: Optional[str] = None
    r"""Description of the choice."""
