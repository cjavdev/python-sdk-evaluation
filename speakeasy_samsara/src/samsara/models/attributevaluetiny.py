"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AttributeValueTinyTypedDict(TypedDict):
    r"""A minified attribute value"""

    id: NotRequired[str]
    r"""The samsara id of this value object."""
    string_value: NotRequired[str]
    r"""The human-readable string for this value."""


class AttributeValueTiny(BaseModel):
    r"""A minified attribute value"""

    id: Optional[str] = None
    r"""The samsara id of this value object."""

    string_value: Annotated[Optional[str], pydantic.Field(alias="stringValue")] = None
    r"""The human-readable string for this value."""
