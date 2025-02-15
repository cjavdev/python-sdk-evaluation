"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class ID(str, Enum):
    r"""The ID of the relay  Valid values: `relay1`, `relay2`"""

    RELAY1 = "relay1"
    RELAY2 = "relay2"


class UpdateEngineImmobilizerRelayStateRequestBodyRequestBodyTypedDict(TypedDict):
    r"""A request object to update a relay state."""

    id: ID
    r"""The ID of the relay  Valid values: `relay1`, `relay2`"""
    is_open: bool
    r"""The desired state of the relay. Provide `true` to open the relay, or `false` to close the relay."""


class UpdateEngineImmobilizerRelayStateRequestBodyRequestBody(BaseModel):
    r"""A request object to update a relay state."""

    id: ID
    r"""The ID of the relay  Valid values: `relay1`, `relay2`"""

    is_open: Annotated[bool, pydantic.Field(alias="isOpen")]
    r"""The desired state of the relay. Provide `true` to open the relay, or `false` to close the relay."""
