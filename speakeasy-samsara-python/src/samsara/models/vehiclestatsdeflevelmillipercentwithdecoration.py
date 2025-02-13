"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .vehiclestatsdecorations import (
    VehicleStatsDecorations,
    VehicleStatsDecorationsTypedDict,
)
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class VehicleStatsDefLevelMilliPercentWithDecorationTypedDict(TypedDict):
    r"""The Diesel Exhaust Fluid (DEF) milli percentage reading."""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""
    value: int
    r"""The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g. `99001`, `49999`, etc)."""
    decorations: NotRequired[VehicleStatsDecorationsTypedDict]
    r"""Optional decorations to the primary stat event. See [here](doc:decorations) for more details. The example shows the response if you were to submit `decorations=engineStates&obdEngineSeconds` to the query parameter:

    ```json
    \"decorations\":{
    \"engineStates\": {
    \"value\": \"Off\" 
    },
    \"obdEngineSeconds\": {
    \"value\": 9723103
    }
    }
    ```
    """


class VehicleStatsDefLevelMilliPercentWithDecoration(BaseModel):
    r"""The Diesel Exhaust Fluid (DEF) milli percentage reading."""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    r"""The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g. `99001`, `49999`, etc)."""

    decorations: Optional[VehicleStatsDecorations] = None
    r"""Optional decorations to the primary stat event. See [here](doc:decorations) for more details. The example shows the response if you were to submit `decorations=engineStates&obdEngineSeconds` to the query parameter:

    ```json
    \"decorations\":{
    \"engineStates\": {
    \"value\": \"Off\" 
    },
    \"obdEngineSeconds\": {
    \"value\": 9723103
    }
    }
    ```
    """
