"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class SignatoryUserObjectResponseBodyTypedDict(TypedDict):
    r"""The user who signed the DVIR."""

    id: str
    r"""ID of the user."""


class SignatoryUserObjectResponseBody(BaseModel):
    r"""The user who signed the DVIR."""

    id: str
    r"""ID of the user."""
