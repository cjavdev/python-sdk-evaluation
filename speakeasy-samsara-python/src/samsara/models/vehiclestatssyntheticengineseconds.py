"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .vehiclestatsdecorations import (
    VehicleStatsDecorations,
    VehicleStatsDecorationsTypedDict,
)
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class VehicleStatsSyntheticEngineSecondsTypedDict(TypedDict):
    r"""Data for the synthetic engine seconds for the vehicle"""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""
    value: int
    r"""Stats for the number of seconds the vehicle's engine has been on, calculated based on a manually-specified engine seconds reading and the number of seconds the vehicle has been on according to the engine state changes reported to the vehicle gateway since that reading was set. This stat will not be present for any vehicle that does not have the engine seconds reading set. The engine seconds reading can be set from the UI on the vehicle details page."""
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


class VehicleStatsSyntheticEngineSeconds(BaseModel):
    r"""Data for the synthetic engine seconds for the vehicle"""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    r"""Stats for the number of seconds the vehicle's engine has been on, calculated based on a manually-specified engine seconds reading and the number of seconds the vehicle has been on according to the engine state changes reported to the vehicle gateway since that reading was set. This stat will not be present for any vehicle that does not have the engine seconds reading set. The engine seconds reading can be set from the UI on the vehicle details page."""

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
