"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AlertObjectMachineInputResponseBodyTypedDict(TypedDict):
    r"""A machine input associated with the alert"""

    id: str
    r"""The ID of the machine input associated with the alert."""
    name: NotRequired[str]
    r"""The name of the machine input."""


class AlertObjectMachineInputResponseBody(BaseModel):
    r"""A machine input associated with the alert"""

    id: str
    r"""The ID of the machine input associated with the alert."""

    name: Optional[str] = None
    r"""The name of the machine input."""
