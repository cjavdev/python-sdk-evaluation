"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .trailerstatgpsodometermeterstyperesponsebody import (
    TrailerStatGpsOdometerMetersTypeResponseBody,
    TrailerStatGpsOdometerMetersTypeResponseBodyTypedDict,
)
from .trailerstatgpstyperesponsebody import (
    TrailerStatGpsTypeResponseBody,
    TrailerStatGpsTypeResponseBodyTypedDict,
)
from .trailerstatreeferalarmtyperesponsebody import (
    TrailerStatReeferAlarmTypeResponseBody,
    TrailerStatReeferAlarmTypeResponseBodyTypedDict,
)
from .trailerstatreeferambientairtemperaturemillictyperesponsebody import (
    TrailerStatReeferAmbientAirTemperatureMilliCTypeResponseBody,
    TrailerStatReeferAmbientAirTemperatureMilliCTypeResponseBodyTypedDict,
)
from .trailerstatreeferdoorstatezone1typeresponsebody import (
    TrailerStatReeferDoorStateZone1TypeResponseBody,
    TrailerStatReeferDoorStateZone1TypeResponseBodyTypedDict,
)
from .trailerstatreeferdoorstatezone2typeresponsebody import (
    TrailerStatReeferDoorStateZone2TypeResponseBody,
    TrailerStatReeferDoorStateZone2TypeResponseBodyTypedDict,
)
from .trailerstatreeferdoorstatezone3typeresponsebody import (
    TrailerStatReeferDoorStateZone3TypeResponseBody,
    TrailerStatReeferDoorStateZone3TypeResponseBodyTypedDict,
)
from .trailerstatreeferfuelpercenttyperesponsebody import (
    TrailerStatReeferFuelPercentTypeResponseBody,
    TrailerStatReeferFuelPercentTypeResponseBodyTypedDict,
)
from .trailerstatreeferobdenginesecondstyperesponsebody import (
    TrailerStatReeferObdEngineSecondsTypeResponseBody,
    TrailerStatReeferObdEngineSecondsTypeResponseBodyTypedDict,
)
from .trailerstatreeferreturnairtemperaturemilliczone1typeresponsebody import (
    TrailerStatReeferReturnAirTemperatureMilliCZone1TypeResponseBody,
    TrailerStatReeferReturnAirTemperatureMilliCZone1TypeResponseBodyTypedDict,
)
from .trailerstatreeferreturnairtemperaturemilliczone2typeresponsebody import (
    TrailerStatReeferReturnAirTemperatureMilliCZone2TypeResponseBody,
    TrailerStatReeferReturnAirTemperatureMilliCZone2TypeResponseBodyTypedDict,
)
from .trailerstatreeferreturnairtemperaturemilliczone3typeresponsebody import (
    TrailerStatReeferReturnAirTemperatureMilliCZone3TypeResponseBody,
    TrailerStatReeferReturnAirTemperatureMilliCZone3TypeResponseBodyTypedDict,
)
from .trailerstatreeferrunmodetyperesponsebody import (
    TrailerStatReeferRunModeTypeResponseBody,
    TrailerStatReeferRunModeTypeResponseBodyTypedDict,
)
from .trailerstatreefersetpointtemperaturemilliczone1typeresponsebody import (
    TrailerStatReeferSetPointTemperatureMilliCZone1TypeResponseBody,
    TrailerStatReeferSetPointTemperatureMilliCZone1TypeResponseBodyTypedDict,
)
from .trailerstatreefersetpointtemperaturemilliczone2typeresponsebody import (
    TrailerStatReeferSetPointTemperatureMilliCZone2TypeResponseBody,
    TrailerStatReeferSetPointTemperatureMilliCZone2TypeResponseBodyTypedDict,
)
from .trailerstatreefersetpointtemperaturemilliczone3typeresponsebody import (
    TrailerStatReeferSetPointTemperatureMilliCZone3TypeResponseBody,
    TrailerStatReeferSetPointTemperatureMilliCZone3TypeResponseBodyTypedDict,
)
from .trailerstatreeferstatetyperesponsebody import (
    TrailerStatReeferStateTypeResponseBody,
    TrailerStatReeferStateTypeResponseBodyTypedDict,
)
from .trailerstatreeferstatezone1typeresponsebody import (
    TrailerStatReeferStateZone1TypeResponseBody,
    TrailerStatReeferStateZone1TypeResponseBodyTypedDict,
)
from .trailerstatreeferstatezone2typeresponsebody import (
    TrailerStatReeferStateZone2TypeResponseBody,
    TrailerStatReeferStateZone2TypeResponseBodyTypedDict,
)
from .trailerstatreeferstatezone3typeresponsebody import (
    TrailerStatReeferStateZone3TypeResponseBody,
    TrailerStatReeferStateZone3TypeResponseBodyTypedDict,
)
from .trailerstatreefersupplyairtemperaturemilliczone1typeresponsebody import (
    TrailerStatReeferSupplyAirTemperatureMilliCZone1TypeResponseBody,
    TrailerStatReeferSupplyAirTemperatureMilliCZone1TypeResponseBodyTypedDict,
)
from .trailerstatreefersupplyairtemperaturemilliczone2typeresponsebody import (
    TrailerStatReeferSupplyAirTemperatureMilliCZone2TypeResponseBody,
    TrailerStatReeferSupplyAirTemperatureMilliCZone2TypeResponseBodyTypedDict,
)
from .trailerstatreefersupplyairtemperaturemilliczone3typeresponsebody import (
    TrailerStatReeferSupplyAirTemperatureMilliCZone3TypeResponseBody,
    TrailerStatReeferSupplyAirTemperatureMilliCZone3TypeResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TrailerStatDecorationResponseBodyTypedDict(TypedDict):
    r"""Decorated values for the primary trailer stat datapoints."""

    carrier_reefer_state: NotRequired[TrailerStatReeferStateTypeResponseBodyTypedDict]
    r"""Reefer state event."""
    gps: NotRequired[TrailerStatGpsTypeResponseBodyTypedDict]
    r"""GPS location data for the trailer."""
    gps_odometer_meters: NotRequired[
        TrailerStatGpsOdometerMetersTypeResponseBodyTypedDict
    ]
    r"""Trailer GPS odometer event."""
    reefer_alarms: NotRequired[TrailerStatReeferAlarmTypeResponseBodyTypedDict]
    r"""Alarms that have been emitted by the reefer."""
    reefer_ambient_air_temperature_milli_c: NotRequired[
        TrailerStatReeferAmbientAirTemperatureMilliCTypeResponseBodyTypedDict
    ]
    r"""Reefer ambient air temperature reading."""
    reefer_door_state_zone1: NotRequired[
        TrailerStatReeferDoorStateZone1TypeResponseBodyTypedDict
    ]
    r"""The door state of the reefer."""
    reefer_door_state_zone2: NotRequired[
        TrailerStatReeferDoorStateZone2TypeResponseBodyTypedDict
    ]
    r"""The door state of the reefer."""
    reefer_door_state_zone3: NotRequired[
        TrailerStatReeferDoorStateZone3TypeResponseBodyTypedDict
    ]
    r"""The door state of the reefer."""
    reefer_fuel_percent: NotRequired[
        TrailerStatReeferFuelPercentTypeResponseBodyTypedDict
    ]
    r"""The fuel percentage of the reefer."""
    reefer_obd_engine_seconds: NotRequired[
        TrailerStatReeferObdEngineSecondsTypeResponseBodyTypedDict
    ]
    r"""Reefer onboard engine seconds reading."""
    reefer_return_air_temperature_milli_c_zone1: NotRequired[
        TrailerStatReeferReturnAirTemperatureMilliCZone1TypeResponseBodyTypedDict
    ]
    r"""Return air temperature of zone 1 of the reefer. This is the temperature of the air as it enters the cooling unit."""
    reefer_return_air_temperature_milli_c_zone2: NotRequired[
        TrailerStatReeferReturnAirTemperatureMilliCZone2TypeResponseBodyTypedDict
    ]
    r"""Return air temperature of zone 2 of the reefer. This is the temperature of the air as it enters the cooling unit."""
    reefer_return_air_temperature_milli_c_zone3: NotRequired[
        TrailerStatReeferReturnAirTemperatureMilliCZone3TypeResponseBodyTypedDict
    ]
    r"""Return air temperature of zone 3 of the reefer. This is the temperature of the air as it enters the cooling unit."""
    reefer_run_mode: NotRequired[TrailerStatReeferRunModeTypeResponseBodyTypedDict]
    r"""The run mode of the reefer."""
    reefer_set_point_temperature_milli_c_zone1: NotRequired[
        TrailerStatReeferSetPointTemperatureMilliCZone1TypeResponseBodyTypedDict
    ]
    r"""Set point temperature of zone 1 of the reefer."""
    reefer_set_point_temperature_milli_c_zone2: NotRequired[
        TrailerStatReeferSetPointTemperatureMilliCZone2TypeResponseBodyTypedDict
    ]
    r"""Set point temperature of zone 2 of the reefer."""
    reefer_set_point_temperature_milli_c_zone3: NotRequired[
        TrailerStatReeferSetPointTemperatureMilliCZone3TypeResponseBodyTypedDict
    ]
    r"""Set point temperature of zone 3 of the reefer."""
    reefer_state_zone1: NotRequired[
        TrailerStatReeferStateZone1TypeResponseBodyTypedDict
    ]
    r"""Reefer state event."""
    reefer_state_zone2: NotRequired[
        TrailerStatReeferStateZone2TypeResponseBodyTypedDict
    ]
    r"""Reefer state event."""
    reefer_state_zone3: NotRequired[
        TrailerStatReeferStateZone3TypeResponseBodyTypedDict
    ]
    r"""Reefer state event."""
    reefer_supply_air_temperature_milli_c_zone1: NotRequired[
        TrailerStatReeferSupplyAirTemperatureMilliCZone1TypeResponseBodyTypedDict
    ]
    r"""Supply or discharge air temperature of zone 2 of the reefer. This is the temperature of the air as it leaves the cooling unit."""
    reefer_supply_air_temperature_milli_c_zone2: NotRequired[
        TrailerStatReeferSupplyAirTemperatureMilliCZone2TypeResponseBodyTypedDict
    ]
    r"""Supply or discharge air temperature of zone 2 of the reefer. This is the temperature of the air as it leaves the cooling unit."""
    reefer_supply_air_temperature_milli_c_zone3: NotRequired[
        TrailerStatReeferSupplyAirTemperatureMilliCZone3TypeResponseBodyTypedDict
    ]
    r"""Supply or discharge air temperature of zone 2 of the reefer. This is the temperature of the air as it leaves the cooling unit."""


class TrailerStatDecorationResponseBody(BaseModel):
    r"""Decorated values for the primary trailer stat datapoints."""

    carrier_reefer_state: Annotated[
        Optional[TrailerStatReeferStateTypeResponseBody],
        pydantic.Field(alias="carrierReeferState"),
    ] = None
    r"""Reefer state event."""

    gps: Optional[TrailerStatGpsTypeResponseBody] = None
    r"""GPS location data for the trailer."""

    gps_odometer_meters: Annotated[
        Optional[TrailerStatGpsOdometerMetersTypeResponseBody],
        pydantic.Field(alias="gpsOdometerMeters"),
    ] = None
    r"""Trailer GPS odometer event."""

    reefer_alarms: Annotated[
        Optional[TrailerStatReeferAlarmTypeResponseBody],
        pydantic.Field(alias="reeferAlarms"),
    ] = None
    r"""Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Annotated[
        Optional[TrailerStatReeferAmbientAirTemperatureMilliCTypeResponseBody],
        pydantic.Field(alias="reeferAmbientAirTemperatureMilliC"),
    ] = None
    r"""Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Annotated[
        Optional[TrailerStatReeferDoorStateZone1TypeResponseBody],
        pydantic.Field(alias="reeferDoorStateZone1"),
    ] = None
    r"""The door state of the reefer."""

    reefer_door_state_zone2: Annotated[
        Optional[TrailerStatReeferDoorStateZone2TypeResponseBody],
        pydantic.Field(alias="reeferDoorStateZone2"),
    ] = None
    r"""The door state of the reefer."""

    reefer_door_state_zone3: Annotated[
        Optional[TrailerStatReeferDoorStateZone3TypeResponseBody],
        pydantic.Field(alias="reeferDoorStateZone3"),
    ] = None
    r"""The door state of the reefer."""

    reefer_fuel_percent: Annotated[
        Optional[TrailerStatReeferFuelPercentTypeResponseBody],
        pydantic.Field(alias="reeferFuelPercent"),
    ] = None
    r"""The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Annotated[
        Optional[TrailerStatReeferObdEngineSecondsTypeResponseBody],
        pydantic.Field(alias="reeferObdEngineSeconds"),
    ] = None
    r"""Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Annotated[
        Optional[TrailerStatReeferReturnAirTemperatureMilliCZone1TypeResponseBody],
        pydantic.Field(alias="reeferReturnAirTemperatureMilliCZone1"),
    ] = None
    r"""Return air temperature of zone 1 of the reefer. This is the temperature of the air as it enters the cooling unit."""

    reefer_return_air_temperature_milli_c_zone2: Annotated[
        Optional[TrailerStatReeferReturnAirTemperatureMilliCZone2TypeResponseBody],
        pydantic.Field(alias="reeferReturnAirTemperatureMilliCZone2"),
    ] = None
    r"""Return air temperature of zone 2 of the reefer. This is the temperature of the air as it enters the cooling unit."""

    reefer_return_air_temperature_milli_c_zone3: Annotated[
        Optional[TrailerStatReeferReturnAirTemperatureMilliCZone3TypeResponseBody],
        pydantic.Field(alias="reeferReturnAirTemperatureMilliCZone3"),
    ] = None
    r"""Return air temperature of zone 3 of the reefer. This is the temperature of the air as it enters the cooling unit."""

    reefer_run_mode: Annotated[
        Optional[TrailerStatReeferRunModeTypeResponseBody],
        pydantic.Field(alias="reeferRunMode"),
    ] = None
    r"""The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Annotated[
        Optional[TrailerStatReeferSetPointTemperatureMilliCZone1TypeResponseBody],
        pydantic.Field(alias="reeferSetPointTemperatureMilliCZone1"),
    ] = None
    r"""Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Annotated[
        Optional[TrailerStatReeferSetPointTemperatureMilliCZone2TypeResponseBody],
        pydantic.Field(alias="reeferSetPointTemperatureMilliCZone2"),
    ] = None
    r"""Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Annotated[
        Optional[TrailerStatReeferSetPointTemperatureMilliCZone3TypeResponseBody],
        pydantic.Field(alias="reeferSetPointTemperatureMilliCZone3"),
    ] = None
    r"""Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Annotated[
        Optional[TrailerStatReeferStateZone1TypeResponseBody],
        pydantic.Field(alias="reeferStateZone1"),
    ] = None
    r"""Reefer state event."""

    reefer_state_zone2: Annotated[
        Optional[TrailerStatReeferStateZone2TypeResponseBody],
        pydantic.Field(alias="reeferStateZone2"),
    ] = None
    r"""Reefer state event."""

    reefer_state_zone3: Annotated[
        Optional[TrailerStatReeferStateZone3TypeResponseBody],
        pydantic.Field(alias="reeferStateZone3"),
    ] = None
    r"""Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Annotated[
        Optional[TrailerStatReeferSupplyAirTemperatureMilliCZone1TypeResponseBody],
        pydantic.Field(alias="reeferSupplyAirTemperatureMilliCZone1"),
    ] = None
    r"""Supply or discharge air temperature of zone 2 of the reefer. This is the temperature of the air as it leaves the cooling unit."""

    reefer_supply_air_temperature_milli_c_zone2: Annotated[
        Optional[TrailerStatReeferSupplyAirTemperatureMilliCZone2TypeResponseBody],
        pydantic.Field(alias="reeferSupplyAirTemperatureMilliCZone2"),
    ] = None
    r"""Supply or discharge air temperature of zone 2 of the reefer. This is the temperature of the air as it leaves the cooling unit."""

    reefer_supply_air_temperature_milli_c_zone3: Annotated[
        Optional[TrailerStatReeferSupplyAirTemperatureMilliCZone3TypeResponseBody],
        pydantic.Field(alias="reeferSupplyAirTemperatureMilliCZone3"),
    ] = None
    r"""Supply or discharge air temperature of zone 2 of the reefer. This is the temperature of the air as it leaves the cooling unit."""
