"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .locationresponseresponsebody import (
    LocationResponseResponseBody,
    LocationResponseResponseBodyTypedDict,
)
from .tripassetresponsebody import TripAssetResponseBody, TripAssetResponseBodyTypedDict
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CompletionStatus(str, Enum):
    r"""Trip completion status  Valid values: `inProgress`, `completed`"""

    IN_PROGRESS = "inProgress"
    COMPLETED = "completed"


class TripResponseBodyTypedDict(TypedDict):
    r"""Trip"""

    asset: TripAssetResponseBodyTypedDict
    r"""Asset that the location readings are tied to"""
    completion_status: CompletionStatus
    r"""Trip completion status  Valid values: `inProgress`, `completed`"""
    created_at_time: str
    r"""[RFC 3339] Time the trip was created in Samsara in UTC."""
    start_location: LocationResponseResponseBodyTypedDict
    r"""Location object."""
    trip_start_time: str
    r"""[RFC 3339] Time the trip started in UTC."""
    updated_at_time: str
    r"""[RFC 3339] Time the trip was updated in Samsara in UTC. Valid updates are when `endTime` populates or `completionStatus` changes values."""
    end_location: NotRequired[LocationResponseResponseBodyTypedDict]
    r"""Location object."""
    trip_end_time: NotRequired[str]
    r"""[RFC 3339] Time the trip ended in UTC."""


class TripResponseBody(BaseModel):
    r"""Trip"""

    asset: TripAssetResponseBody
    r"""Asset that the location readings are tied to"""

    completion_status: Annotated[
        CompletionStatus, pydantic.Field(alias="completionStatus")
    ]
    r"""Trip completion status  Valid values: `inProgress`, `completed`"""

    created_at_time: Annotated[str, pydantic.Field(alias="createdAtTime")]
    r"""[RFC 3339] Time the trip was created in Samsara in UTC."""

    start_location: Annotated[
        LocationResponseResponseBody, pydantic.Field(alias="startLocation")
    ]
    r"""Location object."""

    trip_start_time: Annotated[str, pydantic.Field(alias="tripStartTime")]
    r"""[RFC 3339] Time the trip started in UTC."""

    updated_at_time: Annotated[str, pydantic.Field(alias="updatedAtTime")]
    r"""[RFC 3339] Time the trip was updated in Samsara in UTC. Valid updates are when `endTime` populates or `completionStatus` changes values."""

    end_location: Annotated[
        Optional[LocationResponseResponseBody], pydantic.Field(alias="endLocation")
    ] = None
    r"""Location object."""

    trip_end_time: Annotated[Optional[str], pydantic.Field(alias="tripEndTime")] = None
    r"""[RFC 3339] Time the trip ended in UTC."""
