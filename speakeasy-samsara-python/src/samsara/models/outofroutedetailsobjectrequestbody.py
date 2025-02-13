"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class OutOfRouteDetailsObjectRequestBodyTypedDict(TypedDict):
    r"""Details specific to Out Of Route"""

    max_off_route_meters: int
    r"""The minimum distance in meters a vehicle has to be from its active route path to be considered out of its route."""
    min_duration_milliseconds: int
    r"""The number of milliseconds the trigger needs to stay active before alerting."""


class OutOfRouteDetailsObjectRequestBody(BaseModel):
    r"""Details specific to Out Of Route"""

    max_off_route_meters: Annotated[int, pydantic.Field(alias="maxOffRouteMeters")]
    r"""The minimum distance in meters a vehicle has to be from its active route path to be considered out of its route."""

    min_duration_milliseconds: Annotated[
        int, pydantic.Field(alias="minDurationMilliseconds")
    ]
    r"""The number of milliseconds the trigger needs to stay active before alerting."""
