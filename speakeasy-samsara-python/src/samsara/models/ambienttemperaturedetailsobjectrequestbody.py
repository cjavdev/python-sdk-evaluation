"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AmbientTemperatureDetailsObjectRequestBodyOperation(str, Enum):
    r"""How to evaluate the threshold.  Valid values: `GREATER`, `INSIDE_RANGE`, `LESS`, `OUTSIDE_RANGE`"""

    GREATER = "GREATER"
    INSIDE_RANGE = "INSIDE_RANGE"
    LESS = "LESS"
    OUTSIDE_RANGE = "OUTSIDE_RANGE"


class AmbientTemperatureDetailsObjectRequestBodyTypedDict(TypedDict):
    r"""Details specific to Ambient Temperature."""

    min_duration_milliseconds: int
    r"""The number of milliseconds the trigger needs to stay active before alerting."""
    operation: AmbientTemperatureDetailsObjectRequestBodyOperation
    r"""How to evaluate the threshold.  Valid values: `GREATER`, `INSIDE_RANGE`, `LESS`, `OUTSIDE_RANGE`"""
    temperature_celcius: int
    r"""The temperature in Celcius threshold value."""
    cargo_is_full: NotRequired[bool]
    r"""Whether the cargo is full."""
    doors_are_closed: NotRequired[bool]
    r"""Whether the doors are closed."""


class AmbientTemperatureDetailsObjectRequestBody(BaseModel):
    r"""Details specific to Ambient Temperature."""

    min_duration_milliseconds: Annotated[
        int, pydantic.Field(alias="minDurationMilliseconds")
    ]
    r"""The number of milliseconds the trigger needs to stay active before alerting."""

    operation: AmbientTemperatureDetailsObjectRequestBodyOperation
    r"""How to evaluate the threshold.  Valid values: `GREATER`, `INSIDE_RANGE`, `LESS`, `OUTSIDE_RANGE`"""

    temperature_celcius: Annotated[int, pydantic.Field(alias="temperatureCelcius")]
    r"""The temperature in Celcius threshold value."""

    cargo_is_full: Annotated[Optional[bool], pydantic.Field(alias="cargoIsFull")] = None
    r"""Whether the cargo is full."""

    doors_are_closed: Annotated[
        Optional[bool], pydantic.Field(alias="doorsAreClosed")
    ] = None
    r"""Whether the doors are closed."""
