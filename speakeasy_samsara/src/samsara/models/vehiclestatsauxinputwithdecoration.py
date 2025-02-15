"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .vehiclestatsdecorations import (
    VehicleStatsDecorations,
    VehicleStatsDecorationsTypedDict,
)
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class VehicleStatsAuxInputWithDecorationTypedDict(TypedDict):
    r"""Data for auxiliary digio equipment."""

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
    name: NotRequired[str]
    r"""The type of <a href=\"https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs\" target=\"_blank\">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. The value returned will match what is configured in the dashboard per vehicle."""
    time: NotRequired[str]
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""
    value: NotRequired[bool]
    r"""Boolean indicating the state of the auxiliary equipment."""


class VehicleStatsAuxInputWithDecoration(BaseModel):
    r"""Data for auxiliary digio equipment."""

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

    name: Optional[str] = None
    r"""The type of <a href=\"https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs\" target=\"_blank\">auxiliary input</a> configured for this Vehicle. Once configured, these inputs will generate dynamic, time-series data that will be available to view in the Samsara Dashboard. **By default**: empty. This can be set or updated through the Samsara Dashboard or the API at any time. Inputs 3-13 are only available on gateways with an attached aux expander. The value returned will match what is configured in the dashboard per vehicle."""

    time: Optional[str] = None
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[bool] = None
    r"""Boolean indicating the state of the auxiliary equipment."""
