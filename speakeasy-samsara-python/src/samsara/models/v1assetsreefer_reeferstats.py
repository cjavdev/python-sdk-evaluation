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
from .v1assetreeferresponse_reeferstats_returnairtemp import (
    V1AssetReeferResponseReeferStatsReturnAirTemp,
    V1AssetReeferResponseReeferStatsReturnAirTempTypedDict,
)
from .v1assetreeferresponse_reeferstats_setpoint import (
    V1AssetReeferResponseReeferStatsSetPoint,
    V1AssetReeferResponseReeferStatsSetPointTypedDict,
)
from .v1assetsreefer_reeferstats_ambientairtemperature import (
    V1AssetsReeferReeferStatsAmbientAirTemperature,
    V1AssetsReeferReeferStatsAmbientAirTemperatureTypedDict,
)
from .v1assetsreefer_reeferstats_dischargeairtemperature import (
    V1AssetsReeferReeferStatsDischargeAirTemperature,
    V1AssetsReeferReeferStatsDischargeAirTemperatureTypedDict,
)
from .v1assetsreefer_reeferstats_powerstatus import (
    V1AssetsReeferReeferStatsPowerStatus,
    V1AssetsReeferReeferStatsPowerStatusTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V1AssetsReeferReeferStatsTypedDict(TypedDict):
    r"""Contains all the state changes of the reefer for the included stat types. Each state change is recorded independently, so the number of records in each array may differ depending on when that stat changed state. Stat types with a continuous value (such as temperature) will be recorded at different rates depending on the reefer, but generally readings have a frequency on the order of seconds."""

    ambient_air_temperature: NotRequired[
        List[V1AssetsReeferReeferStatsAmbientAirTemperatureTypedDict]
    ]
    r"""Ambient temperature of the reefer. This is the temperature of the air around the Samsara Asset Gateway."""
    discharge_air_temperature: NotRequired[
        List[V1AssetsReeferReeferStatsDischargeAirTemperatureTypedDict]
    ]
    r"""Discharge air temperature of the reefer. This is the temperature of the air as it leaves the cooling unit."""
    engine_hours: NotRequired[
        List[V1AssetReeferResponseReeferStatsEngineHoursTypedDict]
    ]
    r"""Engine hours of the reefer"""
    fuel_percentage: NotRequired[
        List[V1AssetReeferResponseReeferStatsFuelPercentageTypedDict]
    ]
    r"""Fuel percentage of the reefer"""
    power_status: NotRequired[List[V1AssetsReeferReeferStatsPowerStatusTypedDict]]
    r"""Power status of the reefer"""
    reefer_alarms: NotRequired[List[V1AssetReeferResponseReeferStatsAlarms1TypedDict]]
    r"""Reefer alarms"""
    return_air_temperature: NotRequired[
        List[V1AssetReeferResponseReeferStatsReturnAirTempTypedDict]
    ]
    r"""Return air temperature of the reefer. This is the temperature read by the reefer module (Carrier, Thermo King) that shows the temperature of the air as it enters the system."""
    set_point: NotRequired[List[V1AssetReeferResponseReeferStatsSetPointTypedDict]]
    r"""Set point temperature of the reefer"""


class V1AssetsReeferReeferStats(BaseModel):
    r"""Contains all the state changes of the reefer for the included stat types. Each state change is recorded independently, so the number of records in each array may differ depending on when that stat changed state. Stat types with a continuous value (such as temperature) will be recorded at different rates depending on the reefer, but generally readings have a frequency on the order of seconds."""

    ambient_air_temperature: Annotated[
        Optional[List[V1AssetsReeferReeferStatsAmbientAirTemperature]],
        pydantic.Field(alias="ambientAirTemperature"),
    ] = None
    r"""Ambient temperature of the reefer. This is the temperature of the air around the Samsara Asset Gateway."""

    discharge_air_temperature: Annotated[
        Optional[List[V1AssetsReeferReeferStatsDischargeAirTemperature]],
        pydantic.Field(alias="dischargeAirTemperature"),
    ] = None
    r"""Discharge air temperature of the reefer. This is the temperature of the air as it leaves the cooling unit."""

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
        Optional[List[V1AssetsReeferReeferStatsPowerStatus]],
        pydantic.Field(alias="powerStatus"),
    ] = None
    r"""Power status of the reefer"""

    reefer_alarms: Annotated[
        Optional[List[V1AssetReeferResponseReeferStatsAlarms1]],
        pydantic.Field(alias="reeferAlarms"),
    ] = None
    r"""Reefer alarms"""

    return_air_temperature: Annotated[
        Optional[List[V1AssetReeferResponseReeferStatsReturnAirTemp]],
        pydantic.Field(alias="returnAirTemperature"),
    ] = None
    r"""Return air temperature of the reefer. This is the temperature read by the reefer module (Carrier, Thermo King) that shows the temperature of the air as it enters the system."""

    set_point: Annotated[
        Optional[List[V1AssetReeferResponseReeferStatsSetPoint]],
        pydantic.Field(alias="setPoint"),
    ] = None
    r"""Set point temperature of the reefer"""
