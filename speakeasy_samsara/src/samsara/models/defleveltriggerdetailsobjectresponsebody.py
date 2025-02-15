"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class DefLevelTriggerDetailsObjectResponseBodyOperation(str, Enum):
    r"""How to evaluate the threshold.  Valid values: `GREATER`, `LESS`"""

    GREATER = "GREATER"
    LESS = "LESS"


class DefLevelTriggerDetailsObjectResponseBodyTypedDict(TypedDict):
    r"""Details specific to DEF Level"""

    def_level_percent: int
    r"""The DEF percentage threshold value."""
    min_duration_milliseconds: int
    r"""The number of milliseconds the trigger needs to stay active before alerting."""
    operation: DefLevelTriggerDetailsObjectResponseBodyOperation
    r"""How to evaluate the threshold.  Valid values: `GREATER`, `LESS`"""


class DefLevelTriggerDetailsObjectResponseBody(BaseModel):
    r"""Details specific to DEF Level"""

    def_level_percent: Annotated[int, pydantic.Field(alias="defLevelPercent")]
    r"""The DEF percentage threshold value."""

    min_duration_milliseconds: Annotated[
        int, pydantic.Field(alias="minDurationMilliseconds")
    ]
    r"""The number of milliseconds the trigger needs to stay active before alerting."""

    operation: DefLevelTriggerDetailsObjectResponseBodyOperation
    r"""How to evaluate the threshold.  Valid values: `GREATER`, `LESS`"""
