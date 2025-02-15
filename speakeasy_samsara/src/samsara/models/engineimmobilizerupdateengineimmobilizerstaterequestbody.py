"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .updateengineimmobilizerrelaystaterequestbodyrequestbody import (
    UpdateEngineImmobilizerRelayStateRequestBodyRequestBody,
    UpdateEngineImmobilizerRelayStateRequestBodyRequestBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import List
from typing_extensions import Annotated, TypedDict


class EngineImmobilizerUpdateEngineImmobilizerStateRequestBodyTypedDict(TypedDict):
    r"""A request body to update the engine immobilizer state."""

    relay_states: List[UpdateEngineImmobilizerRelayStateRequestBodyRequestBodyTypedDict]
    r"""A list of relay states. If a relay is omitted, its state won't be updated. If the list is empty, a 400 bad request status code will be returned. If there are multiple states for the same relay, a 400 bad request status code will be returned."""


class EngineImmobilizerUpdateEngineImmobilizerStateRequestBody(BaseModel):
    r"""A request body to update the engine immobilizer state."""

    relay_states: Annotated[
        List[UpdateEngineImmobilizerRelayStateRequestBodyRequestBody],
        pydantic.Field(alias="relayStates"),
    ]
    r"""A list of relay states. If a relay is omitted, its state won't be updated. If the list is empty, a 400 bad request status code will be returned. If there are multiple states for the same relay, a 400 bad request status code will be returned."""
