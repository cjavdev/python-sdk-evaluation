# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .trailer_stat_reefer_state_type_response_body import TrailerStatReeferStateTypeResponseBody
from ..core.serialization import FieldMetadata
from .trailer_stat_gps_type_response_body import TrailerStatGpsTypeResponseBody
from .trailer_stat_gps_odometer_meters_type_response_body import TrailerStatGpsOdometerMetersTypeResponseBody
from .trailer_stat_reefer_alarm_type_response_body import TrailerStatReeferAlarmTypeResponseBody
from .trailer_stat_reefer_ambient_air_temperature_milli_c_type_response_body import (
    TrailerStatReeferAmbientAirTemperatureMilliCTypeResponseBody,
)
from .trailer_stat_reefer_door_state_zone_1_type_response_body import TrailerStatReeferDoorStateZone1TypeResponseBody
from .trailer_stat_reefer_door_state_zone_2_type_response_body import TrailerStatReeferDoorStateZone2TypeResponseBody
from .trailer_stat_reefer_door_state_zone_3_type_response_body import TrailerStatReeferDoorStateZone3TypeResponseBody
from .trailer_stat_reefer_fuel_percent_type_response_body import TrailerStatReeferFuelPercentTypeResponseBody
from .trailer_stat_reefer_obd_engine_seconds_type_response_body import TrailerStatReeferObdEngineSecondsTypeResponseBody
from .trailer_stat_reefer_return_air_temperature_milli_c_zone_1_type_response_body import (
    TrailerStatReeferReturnAirTemperatureMilliCZone1TypeResponseBody,
)
from .trailer_stat_reefer_return_air_temperature_milli_c_zone_2_type_response_body import (
    TrailerStatReeferReturnAirTemperatureMilliCZone2TypeResponseBody,
)
from .trailer_stat_reefer_return_air_temperature_milli_c_zone_3_type_response_body import (
    TrailerStatReeferReturnAirTemperatureMilliCZone3TypeResponseBody,
)
from .trailer_stat_reefer_run_mode_type_response_body import TrailerStatReeferRunModeTypeResponseBody
from .trailer_stat_reefer_set_point_temperature_milli_c_zone_1_type_response_body import (
    TrailerStatReeferSetPointTemperatureMilliCZone1TypeResponseBody,
)
from .trailer_stat_reefer_set_point_temperature_milli_c_zone_2_type_response_body import (
    TrailerStatReeferSetPointTemperatureMilliCZone2TypeResponseBody,
)
from .trailer_stat_reefer_set_point_temperature_milli_c_zone_3_type_response_body import (
    TrailerStatReeferSetPointTemperatureMilliCZone3TypeResponseBody,
)
from .trailer_stat_reefer_state_zone_1_type_response_body import TrailerStatReeferStateZone1TypeResponseBody
from .trailer_stat_reefer_state_zone_2_type_response_body import TrailerStatReeferStateZone2TypeResponseBody
from .trailer_stat_reefer_state_zone_3_type_response_body import TrailerStatReeferStateZone3TypeResponseBody
from .trailer_stat_reefer_supply_air_temperature_milli_c_zone_1_type_response_body import (
    TrailerStatReeferSupplyAirTemperatureMilliCZone1TypeResponseBody,
)
from .trailer_stat_reefer_supply_air_temperature_milli_c_zone_2_type_response_body import (
    TrailerStatReeferSupplyAirTemperatureMilliCZone2TypeResponseBody,
)
from .trailer_stat_reefer_supply_air_temperature_milli_c_zone_3_type_response_body import (
    TrailerStatReeferSupplyAirTemperatureMilliCZone3TypeResponseBody,
)
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class TrailerStatDecorationResponseBody(UniversalBaseModel):
    """
    Decorated values for the primary trailer stat datapoints.
    """

    carrier_reefer_state: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferStateTypeResponseBody], FieldMetadata(alias="carrierReeferState")
    ] = None
    gps: typing.Optional[TrailerStatGpsTypeResponseBody] = None
    gps_odometer_meters: typing_extensions.Annotated[
        typing.Optional[TrailerStatGpsOdometerMetersTypeResponseBody], FieldMetadata(alias="gpsOdometerMeters")
    ] = None
    reefer_alarms: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferAlarmTypeResponseBody], FieldMetadata(alias="reeferAlarms")
    ] = None
    reefer_ambient_air_temperature_milli_c: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferAmbientAirTemperatureMilliCTypeResponseBody],
        FieldMetadata(alias="reeferAmbientAirTemperatureMilliC"),
    ] = None
    reefer_door_state_zone_1: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferDoorStateZone1TypeResponseBody], FieldMetadata(alias="reeferDoorStateZone1")
    ] = None
    reefer_door_state_zone_2: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferDoorStateZone2TypeResponseBody], FieldMetadata(alias="reeferDoorStateZone2")
    ] = None
    reefer_door_state_zone_3: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferDoorStateZone3TypeResponseBody], FieldMetadata(alias="reeferDoorStateZone3")
    ] = None
    reefer_fuel_percent: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferFuelPercentTypeResponseBody], FieldMetadata(alias="reeferFuelPercent")
    ] = None
    reefer_obd_engine_seconds: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferObdEngineSecondsTypeResponseBody],
        FieldMetadata(alias="reeferObdEngineSeconds"),
    ] = None
    reefer_return_air_temperature_milli_c_zone_1: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferReturnAirTemperatureMilliCZone1TypeResponseBody],
        FieldMetadata(alias="reeferReturnAirTemperatureMilliCZone1"),
    ] = None
    reefer_return_air_temperature_milli_c_zone_2: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferReturnAirTemperatureMilliCZone2TypeResponseBody],
        FieldMetadata(alias="reeferReturnAirTemperatureMilliCZone2"),
    ] = None
    reefer_return_air_temperature_milli_c_zone_3: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferReturnAirTemperatureMilliCZone3TypeResponseBody],
        FieldMetadata(alias="reeferReturnAirTemperatureMilliCZone3"),
    ] = None
    reefer_run_mode: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferRunModeTypeResponseBody], FieldMetadata(alias="reeferRunMode")
    ] = None
    reefer_set_point_temperature_milli_c_zone_1: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferSetPointTemperatureMilliCZone1TypeResponseBody],
        FieldMetadata(alias="reeferSetPointTemperatureMilliCZone1"),
    ] = None
    reefer_set_point_temperature_milli_c_zone_2: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferSetPointTemperatureMilliCZone2TypeResponseBody],
        FieldMetadata(alias="reeferSetPointTemperatureMilliCZone2"),
    ] = None
    reefer_set_point_temperature_milli_c_zone_3: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferSetPointTemperatureMilliCZone3TypeResponseBody],
        FieldMetadata(alias="reeferSetPointTemperatureMilliCZone3"),
    ] = None
    reefer_state_zone_1: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferStateZone1TypeResponseBody], FieldMetadata(alias="reeferStateZone1")
    ] = None
    reefer_state_zone_2: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferStateZone2TypeResponseBody], FieldMetadata(alias="reeferStateZone2")
    ] = None
    reefer_state_zone_3: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferStateZone3TypeResponseBody], FieldMetadata(alias="reeferStateZone3")
    ] = None
    reefer_supply_air_temperature_milli_c_zone_1: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferSupplyAirTemperatureMilliCZone1TypeResponseBody],
        FieldMetadata(alias="reeferSupplyAirTemperatureMilliCZone1"),
    ] = None
    reefer_supply_air_temperature_milli_c_zone_2: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferSupplyAirTemperatureMilliCZone2TypeResponseBody],
        FieldMetadata(alias="reeferSupplyAirTemperatureMilliCZone2"),
    ] = None
    reefer_supply_air_temperature_milli_c_zone_3: typing_extensions.Annotated[
        typing.Optional[TrailerStatReeferSupplyAirTemperatureMilliCZone3TypeResponseBody],
        FieldMetadata(alias="reeferSupplyAirTemperatureMilliCZone3"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
