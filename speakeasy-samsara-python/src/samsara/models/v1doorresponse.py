"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v1doorresponse_sensors import (
    V1DoorResponseSensors,
    V1DoorResponseSensorsTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V1DoorResponseTypedDict(TypedDict):
    r"""Contains the current door status of a sensor."""

    group_id: NotRequired[int]
    r"""Deprecated."""
    sensors: NotRequired[List[V1DoorResponseSensorsTypedDict]]


class V1DoorResponse(BaseModel):
    r"""Contains the current door status of a sensor."""

    group_id: Annotated[Optional[int], pydantic.Field(alias="groupId")] = None
    r"""Deprecated."""

    sensors: Optional[List[V1DoorResponseSensors]] = None
