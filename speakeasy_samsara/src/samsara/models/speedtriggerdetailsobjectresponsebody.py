"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class SpeedTriggerDetailsObjectResponseBodyOperation(str, Enum):
    r"""How to evaluate the threshold.  Valid values: `GREATER`, `LESS`"""

    GREATER = "GREATER"
    LESS = "LESS"


class SpeedTriggerDetailsObjectResponseBodyTypedDict(TypedDict):
    r"""Details specific to Speed"""

    min_duration_milliseconds: int
    r"""The number of milliseconds the trigger needs to stay active before alerting."""
    operation: SpeedTriggerDetailsObjectResponseBodyOperation
    r"""How to evaluate the threshold.  Valid values: `GREATER`, `LESS`"""
    speed_kilometers_per_hour: int
    r"""The speed threshold value."""


class SpeedTriggerDetailsObjectResponseBody(BaseModel):
    r"""Details specific to Speed"""

    min_duration_milliseconds: Annotated[
        int, pydantic.Field(alias="minDurationMilliseconds")
    ]
    r"""The number of milliseconds the trigger needs to stay active before alerting."""

    operation: SpeedTriggerDetailsObjectResponseBodyOperation
    r"""How to evaluate the threshold.  Valid values: `GREATER`, `LESS`"""

    speed_kilometers_per_hour: Annotated[
        int, pydantic.Field(alias="speedKilometersPerHour")
    ]
    r"""The speed threshold value."""
