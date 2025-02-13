"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GoaAttributeTinyRequestBodyTypedDict(TypedDict):
    r"""Attribute properties."""

    id: NotRequired[str]
    r"""Id of the attribute"""
    name: NotRequired[str]
    r"""Name of the attribute"""
    number_values: NotRequired[List[float]]
    r"""List of number values associated with the attribute"""
    string_values: NotRequired[List[str]]
    r"""List of string values associated with the attribute."""


class GoaAttributeTinyRequestBody(BaseModel):
    r"""Attribute properties."""

    id: Optional[str] = None
    r"""Id of the attribute"""

    name: Optional[str] = None
    r"""Name of the attribute"""

    number_values: Annotated[
        Optional[List[float]], pydantic.Field(alias="numberValues")
    ] = None
    r"""List of number values associated with the attribute"""

    string_values: Annotated[
        Optional[List[str]], pydantic.Field(alias="stringValues")
    ] = None
    r"""List of string values associated with the attribute."""
