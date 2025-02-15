"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v1assetreeferresponse_reeferstats_alarms_1 import (
    V1AssetReeferResponseReeferStatsAlarms1,
    V1AssetReeferResponseReeferStatsAlarms1TypedDict,
)
from .v1assetreeferresponse_reeferstats_enginehours import (
    V1AssetReeferResponseReeferStatsEngineHours,
    V1AssetReeferResponseReeferStatsEngineHoursTypedDict,
)
from .v1assetreeferresponse_reeferstats_fuelpercentage import (
    V1AssetReeferResponseReeferStatsFuelPercentage,
    V1AssetReeferResponseReeferStatsFuelPercentageTypedDict,
)
from .v1assetreeferresponse_reeferstats_powerstatus import (
    V1AssetReeferResponseReeferStatsPowerStatus,
    V1AssetReeferResponseReeferStatsPowerStatusTypedDict,
)
from .v1assetreeferresponse_reeferstats_returnairtemp import (
    V1AssetReeferResponseReeferStatsReturnAirTemp,
    V1AssetReeferResponseReeferStatsReturnAirTempTypedDict,
)
from .v1assetreeferresponse_reeferstats_setpoint import (
    V1AssetReeferResponseReeferStatsSetPoint,
    V1AssetReeferResponseReeferStatsSetPointTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V1AssetReeferResponseReeferStatsTypedDict(TypedDict):
    alarms: NotRequired[List[V1AssetReeferResponseReeferStatsAlarms1TypedDict]]
    r"""Reefer alarms"""
    engine_hours: NotRequired[
        List[V1AssetReeferResponseReeferStatsEngineHoursTypedDict]
    ]
    r"""Engine hours of the reefer"""
    fuel_percentage: NotRequired[
        List[V1AssetReeferResponseReeferStatsFuelPercentageTypedDict]
    ]
    r"""Fuel percentage of the reefer"""
    power_status: NotRequired[
        List[V1AssetReeferResponseReeferStatsPowerStatusTypedDict]
    ]
    r"""Power status of the reefer"""
    return_air_temp: NotRequired[
        List[V1AssetReeferResponseReeferStatsReturnAirTempTypedDict]
    ]
    r"""Return air temperature of the reefer"""
    set_point: NotRequired[List[V1AssetReeferResponseReeferStatsSetPointTypedDict]]
    r"""Set point temperature of the reefer"""


class V1AssetReeferResponseReeferStats(BaseModel):
    alarms: Optional[List[V1AssetReeferResponseReeferStatsAlarms1]] = None
    r"""Reefer alarms"""

    engine_hours: Annotated[
        Optional[List[V1AssetReeferResponseReeferStatsEngineHours]],
        pydantic.Field(alias="engineHours"),
    ] = None
    r"""Engine hours of the reefer"""

    fuel_percentage: Annotated[
        Optional[List[V1AssetReeferResponseReeferStatsFuelPercentage]],
        pydantic.Field(alias="fuelPercentage"),
    ] = None
    r"""Fuel percentage of the reefer"""

    power_status: Annotated[
        Optional[List[V1AssetReeferResponseReeferStatsPowerStatus]],
        pydantic.Field(alias="powerStatus"),
    ] = None
    r"""Power status of the reefer"""

    return_air_temp: Annotated[
        Optional[List[V1AssetReeferResponseReeferStatsReturnAirTemp]],
        pydantic.Field(alias="returnAirTemp"),
    ] = None
    r"""Return air temperature of the reefer"""

    set_point: Annotated[
        Optional[List[V1AssetReeferResponseReeferStatsSetPoint]],
        pydantic.Field(alias="setPoint"),
    ] = None
    r"""Set point temperature of the reefer"""
