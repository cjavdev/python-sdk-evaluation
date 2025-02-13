# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "VehicleStatsResponse",
    "Data",
    "DataAmbientAirTemperatureMilliC",
    "DataAuxInput1",
    "DataAuxInput10",
    "DataAuxInput11",
    "DataAuxInput12",
    "DataAuxInput13",
    "DataAuxInput2",
    "DataAuxInput3",
    "DataAuxInput4",
    "DataAuxInput5",
    "DataAuxInput6",
    "DataAuxInput7",
    "DataAuxInput8",
    "DataAuxInput9",
    "DataBarometricPressurePa",
    "DataBatteryMilliVolts",
    "DataDefLevelMilliPercent",
    "DataEcuSpeedMph",
    "DataEngineCoolantTemperatureMilliC",
    "DataEngineImmobilizer",
    "DataEngineLoadPercent",
    "DataEngineOilPressureKPa",
    "DataEngineRpm",
    "DataEngineState",
    "DataEvAverageBatteryTemperatureMilliCelsius",
    "DataEvBatteryCurrentMilliAmp",
    "DataEvBatteryStateOfHealthMilliPercent",
    "DataEvBatteryVoltageMilliVolt",
    "DataEvChargingCurrentMilliAmp",
    "DataEvChargingEnergyMicroWh",
    "DataEvChargingStatus",
    "DataEvChargingVoltageMilliVolt",
    "DataEvConsumedEnergyMicroWh",
    "DataEvDistanceDrivenMeters",
    "DataEvRegeneratedEnergyMicroWh",
    "DataEvStateOfChargeMilliPercent",
    "DataFaultCodes",
    "DataFaultCodesJ1939",
    "DataFaultCodesJ1939CheckEngineLights",
    "DataFaultCodesJ1939DiagnosticTroubleCode",
    "DataFaultCodesJ1939DiagnosticTroubleCodeVendorSpecificFields",
    "DataFaultCodesObdii",
    "DataFaultCodesObdiiDiagnosticTroubleCode",
    "DataFaultCodesObdiiDiagnosticTroubleCodeConfirmedDtc",
    "DataFaultCodesObdiiDiagnosticTroubleCodeMonitorStatus",
    "DataFaultCodesObdiiDiagnosticTroubleCodePendingDtc",
    "DataFaultCodesObdiiDiagnosticTroubleCodePermanentDtc",
    "DataFaultCodesOem",
    "DataFaultCodesOemDiagnosticTroubleCode",
    "DataFuelPercent",
    "DataGps",
    "DataGpsAddress",
    "DataGpsReverseGeo",
    "DataGpsDistanceMeters",
    "DataGpsOdometerMeters",
    "DataIntakeManifoldTemperatureMilliC",
    "DataNfcCardScan",
    "DataNfcCardScanCard",
    "DataObdEngineSeconds",
    "DataObdOdometerMeters",
    "DataSeatbeltDriver",
    "DataSpreaderActive",
    "DataSpreaderAirTemp",
    "DataSpreaderBlastState",
    "DataSpreaderGranularName",
    "DataSpreaderGranularRate",
    "DataSpreaderLiquidName",
    "DataSpreaderLiquidRate",
    "DataSpreaderOnState",
    "DataSpreaderPlowStatus",
    "DataSpreaderPrewetName",
    "DataSpreaderPrewetRate",
    "DataSpreaderRoadTemp",
    "DataSyntheticEngineSeconds",
    "DataSyntheticEngineSecondsDecorations",
    "DataSyntheticEngineSecondsDecorationsAmbientAirTemperatureMilliC",
    "DataSyntheticEngineSecondsDecorationsAuxInput1",
    "DataSyntheticEngineSecondsDecorationsAuxInput10",
    "DataSyntheticEngineSecondsDecorationsAuxInput11",
    "DataSyntheticEngineSecondsDecorationsAuxInput12",
    "DataSyntheticEngineSecondsDecorationsAuxInput13",
    "DataSyntheticEngineSecondsDecorationsAuxInput2",
    "DataSyntheticEngineSecondsDecorationsAuxInput3",
    "DataSyntheticEngineSecondsDecorationsAuxInput4",
    "DataSyntheticEngineSecondsDecorationsAuxInput5",
    "DataSyntheticEngineSecondsDecorationsAuxInput6",
    "DataSyntheticEngineSecondsDecorationsAuxInput7",
    "DataSyntheticEngineSecondsDecorationsAuxInput8",
    "DataSyntheticEngineSecondsDecorationsAuxInput9",
    "DataSyntheticEngineSecondsDecorationsBarometricPressurePa",
    "DataSyntheticEngineSecondsDecorationsBatteryMilliVolts",
    "DataSyntheticEngineSecondsDecorationsDefLevelMilliPercent",
    "DataSyntheticEngineSecondsDecorationsEcuSpeedMph",
    "DataSyntheticEngineSecondsDecorationsEngineCoolantTemperatureMilliC",
    "DataSyntheticEngineSecondsDecorationsEngineImmobilizer",
    "DataSyntheticEngineSecondsDecorationsEngineLoadPercent",
    "DataSyntheticEngineSecondsDecorationsEngineOilPressureKPa",
    "DataSyntheticEngineSecondsDecorationsEngineRpm",
    "DataSyntheticEngineSecondsDecorationsEngineStates",
    "DataSyntheticEngineSecondsDecorationsEvAverageBatteryTemperatureMilliCelsius",
    "DataSyntheticEngineSecondsDecorationsEvBatteryCurrentMilliAmp",
    "DataSyntheticEngineSecondsDecorationsEvBatteryStateOfHealthMilliPercent",
    "DataSyntheticEngineSecondsDecorationsEvBatteryVoltageMilliVolt",
    "DataSyntheticEngineSecondsDecorationsEvChargingCurrentMilliAmp",
    "DataSyntheticEngineSecondsDecorationsEvChargingEnergyMicroWh",
    "DataSyntheticEngineSecondsDecorationsEvChargingStatus",
    "DataSyntheticEngineSecondsDecorationsEvChargingVoltageMilliVolt",
    "DataSyntheticEngineSecondsDecorationsEvConsumedEnergyMicroWh",
    "DataSyntheticEngineSecondsDecorationsEvDistanceDrivenMeters",
    "DataSyntheticEngineSecondsDecorationsEvRegeneratedEnergyMicroWh",
    "DataSyntheticEngineSecondsDecorationsEvStateOfChargeMilliPercent",
    "DataSyntheticEngineSecondsDecorationsFaultCodes",
    "DataSyntheticEngineSecondsDecorationsFaultCodesJ1939",
    "DataSyntheticEngineSecondsDecorationsFaultCodesJ1939CheckEngineLights",
    "DataSyntheticEngineSecondsDecorationsFaultCodesJ1939DiagnosticTroubleCode",
    "DataSyntheticEngineSecondsDecorationsFaultCodesJ1939DiagnosticTroubleCodeVendorSpecificFields",
    "DataSyntheticEngineSecondsDecorationsFaultCodesObdii",
    "DataSyntheticEngineSecondsDecorationsFaultCodesObdiiDiagnosticTroubleCode",
    "DataSyntheticEngineSecondsDecorationsFaultCodesObdiiDiagnosticTroubleCodeConfirmedDtc",
    "DataSyntheticEngineSecondsDecorationsFaultCodesObdiiDiagnosticTroubleCodeMonitorStatus",
    "DataSyntheticEngineSecondsDecorationsFaultCodesObdiiDiagnosticTroubleCodePendingDtc",
    "DataSyntheticEngineSecondsDecorationsFaultCodesObdiiDiagnosticTroubleCodePermanentDtc",
    "DataSyntheticEngineSecondsDecorationsFaultCodesOem",
    "DataSyntheticEngineSecondsDecorationsFaultCodesOemDiagnosticTroubleCode",
    "DataSyntheticEngineSecondsDecorationsFuelPercents",
    "DataSyntheticEngineSecondsDecorationsGps",
    "DataSyntheticEngineSecondsDecorationsGpsAddress",
    "DataSyntheticEngineSecondsDecorationsGpsReverseGeo",
    "DataSyntheticEngineSecondsDecorationsGpsDistanceMeters",
    "DataSyntheticEngineSecondsDecorationsGpsOdometerMeters",
    "DataSyntheticEngineSecondsDecorationsIntakeManifoldTemperatureMilliC",
    "DataSyntheticEngineSecondsDecorationsObdEngineSeconds",
    "DataSyntheticEngineSecondsDecorationsObdOdometerMeters",
    "DataSyntheticEngineSecondsDecorationsSeatbeltDriver",
    "DataSyntheticEngineSecondsDecorationsSpreaderActive",
    "DataSyntheticEngineSecondsDecorationsSpreaderAirTemp",
    "DataSyntheticEngineSecondsDecorationsSpreaderBlastState",
    "DataSyntheticEngineSecondsDecorationsSpreaderGranularName",
    "DataSyntheticEngineSecondsDecorationsSpreaderGranularRate",
    "DataSyntheticEngineSecondsDecorationsSpreaderLiquidName",
    "DataSyntheticEngineSecondsDecorationsSpreaderLiquidRate",
    "DataSyntheticEngineSecondsDecorationsSpreaderOnState",
    "DataSyntheticEngineSecondsDecorationsSpreaderPlowStatus",
    "DataSyntheticEngineSecondsDecorationsSpreaderPrewetName",
    "DataSyntheticEngineSecondsDecorationsSpreaderPrewetRate",
    "DataSyntheticEngineSecondsDecorationsSpreaderRoadTemp",
    "DataSyntheticEngineSecondsDecorationsTirePressure",
    "Pagination",
]


class DataAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """The ambient air temperature reading in millidegree Celsius."""


class DataAuxInput1(BaseModel):
    name: Optional[str] = None
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[bool] = None
    """Boolean indicating the state of the auxiliary equipment."""


class DataAuxInput10(BaseModel):
    name: Optional[str] = None
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[bool] = None
    """Boolean indicating the state of the auxiliary equipment."""


class DataAuxInput11(BaseModel):
    name: Optional[str] = None
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[bool] = None
    """Boolean indicating the state of the auxiliary equipment."""


class DataAuxInput12(BaseModel):
    name: Optional[str] = None
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[bool] = None
    """Boolean indicating the state of the auxiliary equipment."""


class DataAuxInput13(BaseModel):
    name: Optional[str] = None
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[bool] = None
    """Boolean indicating the state of the auxiliary equipment."""


class DataAuxInput2(BaseModel):
    name: Optional[str] = None
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[bool] = None
    """Boolean indicating the state of the auxiliary equipment."""


class DataAuxInput3(BaseModel):
    name: Optional[str] = None
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[bool] = None
    """Boolean indicating the state of the auxiliary equipment."""


class DataAuxInput4(BaseModel):
    name: Optional[str] = None
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[bool] = None
    """Boolean indicating the state of the auxiliary equipment."""


class DataAuxInput5(BaseModel):
    name: Optional[str] = None
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[bool] = None
    """Boolean indicating the state of the auxiliary equipment."""


class DataAuxInput6(BaseModel):
    name: Optional[str] = None
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[bool] = None
    """Boolean indicating the state of the auxiliary equipment."""


class DataAuxInput7(BaseModel):
    name: Optional[str] = None
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[bool] = None
    """Boolean indicating the state of the auxiliary equipment."""


class DataAuxInput8(BaseModel):
    name: Optional[str] = None
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[bool] = None
    """Boolean indicating the state of the auxiliary equipment."""


class DataAuxInput9(BaseModel):
    name: Optional[str] = None
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    time: Optional[str] = None
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[bool] = None
    """Boolean indicating the state of the auxiliary equipment."""


class DataBarometricPressurePa(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """The barometric pressure reading in pascals."""


class DataBatteryMilliVolts(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """The battery voltage in millivolts."""


class DataDefLevelMilliPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g.

    `99001`, `49999`, etc).
    """


class DataEcuSpeedMph(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: float
    """The speed of the vehicle in miles per hour."""


class DataEngineCoolantTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """The engine coolant temperature reading in millidegree Celsius."""


class DataEngineImmobilizer(BaseModel):
    connected: bool
    """Whether the engine immobilizer is connected or not"""

    state: Literal["ignition_disabled", "ignition_enabled"]
    """The state of the engine immobilizer.

    Valid values: `ignition_disabled`, `ignition_enabled`. This stat type will only
    return states of our first Engine Immobilizer Hardware (ACC-EI). Please use
    <a href="https://developers.samsara.com/reference/getengineimmobilizerstates" target="_blank">Get
    engine immobilizer states</a> to get states for both Engine Immobilizer Hardware
    versions (incl. HW-EI21).
    """

    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""


class DataEngineLoadPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """The engine load in percentage points (e.g. `99`, `50`, etc)."""


class DataEngineOilPressureKPa(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """The engine oil pressure reading in kilopascals."""


class DataEngineRpm(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """The revolutions per minute of the engine."""


class DataEngineState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Literal["Off", "On", "Idle"]
    """The state of the engine."""


class DataEvAverageBatteryTemperatureMilliCelsius(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Battery temperature for electric and hybrid vehicles in milli celsius."""


class DataEvBatteryCurrentMilliAmp(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Battery current for electric and hybrid vehicles in milli amps."""


class DataEvBatteryStateOfHealthMilliPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Milli percent battery state of health for electric and hybrid vehicles."""


class DataEvBatteryVoltageMilliVolt(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Battery voltage for electric and hybrid vehicles in milli volts."""


class DataEvChargingCurrentMilliAmp(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Charging current for electric and hybrid vehicles in milli amps."""


class DataEvChargingEnergyMicroWh(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Charging energy for electric and hybrid vehicles in microwatt hours."""


class DataEvChargingStatus(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Literal[0, 1, 2, 3, 4]
    """Charging status for electric and hybrid vehicles.

    Statuses: unknown - 0, not charging - 1, charging - 2.
    """


class DataEvChargingVoltageMilliVolt(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Charging voltage for electric and hybrid vehicles in milli volts."""


class DataEvConsumedEnergyMicroWh(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """
    Consumed energy (including regenerated) for electric and hybrid vehicles in
    microwatt hours.
    """


class DataEvDistanceDrivenMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Electric distance driven for electric and hybrid vehicles in meters."""


class DataEvRegeneratedEnergyMicroWh(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Regenerated energy for electric and hybrid vehicles in microwatt hours."""


class DataEvStateOfChargeMilliPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Milli percent State of Charge for electric and hybrid vehicles."""


class DataFaultCodesJ1939CheckEngineLights(BaseModel):
    emissions_is_on: bool = FieldInfo(alias="emissionsIsOn")
    """True if the MIL status is nonzero."""

    protect_is_on: bool = FieldInfo(alias="protectIsOn")
    """True if the engine protect lamp status is nonzero."""

    stop_is_on: bool = FieldInfo(alias="stopIsOn")
    """True if the red lamp status is nonzero."""

    warning_is_on: bool = FieldInfo(alias="warningIsOn")
    """True if the amber lamp status is nonzero."""


class DataFaultCodesJ1939DiagnosticTroubleCodeVendorSpecificFields(BaseModel):
    dtc_description: Optional[str] = FieldInfo(alias="dtcDescription", default=None)
    """The DTC description, if available."""

    repair_instructions_url: Optional[str] = FieldInfo(alias="repairInstructionsUrl", default=None)
    """A link to vendor repair instructions, if available."""


class DataFaultCodesJ1939DiagnosticTroubleCode(BaseModel):
    fmi_id: int = FieldInfo(alias="fmiId")
    """The FMI identifier."""

    mil_status: int = FieldInfo(alias="milStatus")
    """The MIL status, indicating a check engine light."""

    occurrence_count: int = FieldInfo(alias="occurrenceCount")
    """The number of times this fault has triggered."""

    spn_id: int = FieldInfo(alias="spnId")
    """The SPN identifier."""

    tx_id: int = FieldInfo(alias="txId")
    """The TX identifier."""

    fmi_description: Optional[str] = FieldInfo(alias="fmiDescription", default=None)
    """A short description of the FMI identifier, if available."""

    source_address_name: Optional[str] = FieldInfo(alias="sourceAddressName", default=None)
    """The source address name corresponding to the txId"""

    spn_description: Optional[str] = FieldInfo(alias="spnDescription", default=None)
    """A short description of the SPN identifier, if available."""

    vendor_specific_fields: Optional[DataFaultCodesJ1939DiagnosticTroubleCodeVendorSpecificFields] = FieldInfo(
        alias="vendorSpecificFields", default=None
    )
    """Vendor specific data for J1939 vehicles."""


class DataFaultCodesJ1939(BaseModel):
    check_engine_lights: Optional[DataFaultCodesJ1939CheckEngineLights] = FieldInfo(
        alias="checkEngineLights", default=None
    )
    """Status of engine lights on J1939 vehicles."""

    diagnostic_trouble_codes: Optional[List[DataFaultCodesJ1939DiagnosticTroubleCode]] = FieldInfo(
        alias="diagnosticTroubleCodes", default=None
    )
    """Diagnostic trouble codes for J1939 vehicles."""


class DataFaultCodesObdiiDiagnosticTroubleCodeConfirmedDtc(BaseModel):
    dtc_id: int = FieldInfo(alias="dtcId")
    """The DTC identifier."""

    dtc_description: Optional[str] = FieldInfo(alias="dtcDescription", default=None)
    """The DTC description, if available."""

    dtc_short_code: Optional[str] = FieldInfo(alias="dtcShortCode", default=None)
    """The DTC short code, if available."""


class DataFaultCodesObdiiDiagnosticTroubleCodeMonitorStatus(BaseModel):
    catalyst: Optional[Literal["N", "R", "U"]] = None
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    comprehensive: Optional[Literal["N", "R", "U"]] = None
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    egr: Optional[Literal["N", "R", "U"]] = None
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    evap_system: Optional[Literal["N", "R", "U"]] = FieldInfo(alias="evapSystem", default=None)
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    fuel: Optional[Literal["N", "R", "U"]] = None
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    heated_catalyst: Optional[Literal["N", "R", "U"]] = FieldInfo(alias="heatedCatalyst", default=None)
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    heated_o2_sensor: Optional[Literal["N", "R", "U"]] = FieldInfo(alias="heatedO2Sensor", default=None)
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    iso_sae_reserved: Optional[Literal["N", "R", "U"]] = FieldInfo(alias="isoSaeReserved", default=None)
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    misfire: Optional[Literal["N", "R", "U"]] = None
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    not_ready_count: Optional[int] = FieldInfo(alias="notReadyCount", default=None)
    """Count of the number of sensors reporting N: Not Complete"""

    o2_sensor: Optional[Literal["N", "R", "U"]] = FieldInfo(alias="o2Sensor", default=None)
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    secondary_air: Optional[Literal["N", "R", "U"]] = FieldInfo(alias="secondaryAir", default=None)
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""


class DataFaultCodesObdiiDiagnosticTroubleCodePendingDtc(BaseModel):
    dtc_id: int = FieldInfo(alias="dtcId")
    """The DTC identifier."""

    dtc_description: Optional[str] = FieldInfo(alias="dtcDescription", default=None)
    """The DTC description, if available."""

    dtc_short_code: Optional[str] = FieldInfo(alias="dtcShortCode", default=None)
    """The DTC short code, if available."""


class DataFaultCodesObdiiDiagnosticTroubleCodePermanentDtc(BaseModel):
    dtc_id: int = FieldInfo(alias="dtcId")
    """The DTC identifier."""

    dtc_description: Optional[str] = FieldInfo(alias="dtcDescription", default=None)
    """The DTC description, if available."""

    dtc_short_code: Optional[str] = FieldInfo(alias="dtcShortCode", default=None)
    """The DTC short code, if available."""


class DataFaultCodesObdiiDiagnosticTroubleCode(BaseModel):
    tx_id: int = FieldInfo(alias="txId")
    """The TX identifier."""

    confirmed_dtcs: Optional[List[DataFaultCodesObdiiDiagnosticTroubleCodeConfirmedDtc]] = FieldInfo(
        alias="confirmedDtcs", default=None
    )
    """Confirmed DTC codes."""

    ignition_type: Optional[Literal["spark", "compression"]] = FieldInfo(alias="ignitionType", default=None)
    """The ignition type of this passenger vehicle.

    Valid values: `spark`, `compression`.
    """

    mil_status: Optional[bool] = FieldInfo(alias="milStatus", default=None)
    """The MIL status, indicating a check engine light."""

    monitor_status: Optional[DataFaultCodesObdiiDiagnosticTroubleCodeMonitorStatus] = FieldInfo(
        alias="monitorStatus", default=None
    )
    """Readings from engine sensors"""

    pending_dtcs: Optional[List[DataFaultCodesObdiiDiagnosticTroubleCodePendingDtc]] = FieldInfo(
        alias="pendingDtcs", default=None
    )
    """Pending DTC codes."""

    permanent_dtcs: Optional[List[DataFaultCodesObdiiDiagnosticTroubleCodePermanentDtc]] = FieldInfo(
        alias="permanentDtcs", default=None
    )
    """Permanent DTC codes."""


class DataFaultCodesObdii(BaseModel):
    check_engine_light_is_on: Optional[bool] = FieldInfo(alias="checkEngineLightIsOn", default=None)
    """
    True if the check engine light is illuminated (MIL status field is nonzero for
    any faults).
    """

    diagnostic_trouble_codes: Optional[List[DataFaultCodesObdiiDiagnosticTroubleCode]] = FieldInfo(
        alias="diagnosticTroubleCodes", default=None
    )
    """Diagnostic trouble codes for passenger vehicles."""


class DataFaultCodesOemDiagnosticTroubleCode(BaseModel):
    code_description: Optional[str] = FieldInfo(alias="codeDescription", default=None)
    """The OEM code description."""

    code_identifier: Optional[str] = FieldInfo(alias="codeIdentifier", default=None)
    """The OEM code identifier."""

    code_severity: Optional[str] = FieldInfo(alias="codeSeverity", default=None)
    """The OEM code severity."""

    code_source: Optional[str] = FieldInfo(alias="codeSource", default=None)
    """The OEM code source."""


class DataFaultCodesOem(BaseModel):
    diagnostic_trouble_codes: Optional[List[DataFaultCodesOemDiagnosticTroubleCode]] = FieldInfo(
        alias="diagnosticTroubleCodes", default=None
    )
    """Proprietary diagnostic trouble codes for OEM vehicles."""


class DataFaultCodes(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    can_bus_type: Optional[str] = FieldInfo(alias="canBusType", default=None)
    """The CAN bus type of the vehicle."""

    j1939: Optional[DataFaultCodesJ1939] = None
    """Vehicle fault codes for J1939 vehicles."""

    obdii: Optional[DataFaultCodesObdii] = None
    """Vehicle fault codes for passenger vehicles."""

    oem: Optional[DataFaultCodesOem] = None
    """Vehicle fault codes for OEM vehicles."""


class DataFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """The engine fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataGpsAddress(BaseModel):
    id: Optional[str] = None
    """Id of the address."""

    name: Optional[str] = None
    """Name of address."""


class DataGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees"""

    longitude: float
    """GPS longitude represented in degrees"""

    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    address: Optional[DataGpsAddress] = None
    """Address that the location is in."""

    heading_degrees: Optional[float] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the vehicle in degrees."""

    is_ecu_speed: Optional[bool] = FieldInfo(alias="isEcuSpeed", default=None)
    """True if the speed value is reported from the ECU.

    Speed value is reported from GPS otherwise.
    """

    reverse_geo: Optional[DataGpsReverseGeo] = FieldInfo(alias="reverseGeo", default=None)
    """Reverse geocoded information."""

    speed_miles_per_hour: Optional[float] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the vehicle in miles per hour.

    See `isEcuSpeed` to determine speed data source.
    """


class DataGpsDistanceMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: float
    """
    Number of meters the vehicle has traveled since the gateway was installed, based
    on GPS calculations.
    """


class DataGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """
    Number of meters the vehicle has traveled according to the GPS calculations and
    the manually-specified odometer reading.
    """


class DataIntakeManifoldTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """The intake manifold temperature reading in millidegree Celsius."""


class DataNfcCardScanCard(BaseModel):
    id: Optional[str] = None
    """The id code of the card that was scanned."""


class DataNfcCardScan(BaseModel):
    card: DataNfcCardScanCard
    """The card that was scanned."""

    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""


class DataObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """
    Number of seconds the vehicle's engine has been on according to the on-board
    diagnostics.
    """


class DataObdOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """
    Number of meters the vehicle has traveled according to the on-board diagnostics.
    """


class DataSeatbeltDriver(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Literal["Buckled", "Unbuckled"]
    """Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`."""


class DataSpreaderActive(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Literal["Off", "On"]
    """Whether vehicle is actively spreading any material."""


class DataSpreaderAirTemp(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Air (ambient) temperature in milli celsius reading from material spreader."""


class DataSpreaderBlastState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Literal["On", "Off"]
    """Whether vehicle is actively spreading material in ‘blast mode’."""


class DataSpreaderGranularName(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: str
    """
    Name of most recent type of granular material spread, read from the material
    spreader.
    """


class DataSpreaderGranularRate(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """
    Granular spread rate reading in milliliters per meter, read from the material
    spreader. Unfiltered live stats are supplied as-read from the Material Spreader
    unit. Readings do not consider total spread rate(s) over time or distance.
    Unfiltered live stats are supplied as-read from the Material Spreader unit.
    Readings do not consider total spread rate(s) over time or distance.
    """


class DataSpreaderLiquidName(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: str
    """
    Name of most recent type of liquid material spread, read from the material
    spreader.
    """


class DataSpreaderLiquidRate(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """
    Liquid spread rate reading in milliliters per meter, read from the material
    spreader. Unfiltered live stats are supplied as-read from the Material Spreader
    unit. Readings do not consider total spread rate(s) over time or distance.
    Unfiltered live stats are supplied as-read from the Material Spreader unit.
    Readings do not consider total spread rate(s) over time or distance.
    """


class DataSpreaderOnState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Literal["On", "Off"]
    """Whether vehicle spreader is enabled."""


class DataSpreaderPlowStatus(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Literal["Up", "Down"]
    """Snow plow status, as read from the material spreader"""


class DataSpreaderPrewetName(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: str
    """
    Name of most recent type of prewet material spread, read from the material
    spreader.
    """


class DataSpreaderPrewetRate(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """
    Prewet spread rate reading in milliliters per meter, read from the material
    spreader. Unfiltered live stats are supplied as-read from the Material Spreader
    unit. Readings do not consider total spread rate(s) over time or distance.
    Unfiltered live stats are supplied as-read from the Material Spreader unit.
    Readings do not consider total spread rate(s) over time or distance.
    """


class DataSpreaderRoadTemp(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Road temperature reading in milli celsius from material spreader."""


class DataSyntheticEngineSecondsDecorationsAmbientAirTemperatureMilliC(BaseModel):
    value: int
    """The ambient air temperature reading in millidegree Celsius."""


class DataSyntheticEngineSecondsDecorationsAuxInput1(BaseModel):
    name: str
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    value: bool
    """Boolean indicating the state of the auxiliary equipment."""


class DataSyntheticEngineSecondsDecorationsAuxInput10(BaseModel):
    name: str
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    value: bool
    """Boolean indicating the state of the auxiliary equipment."""


class DataSyntheticEngineSecondsDecorationsAuxInput11(BaseModel):
    name: str
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    value: bool
    """Boolean indicating the state of the auxiliary equipment."""


class DataSyntheticEngineSecondsDecorationsAuxInput12(BaseModel):
    name: str
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    value: bool
    """Boolean indicating the state of the auxiliary equipment."""


class DataSyntheticEngineSecondsDecorationsAuxInput13(BaseModel):
    name: str
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    value: bool
    """Boolean indicating the state of the auxiliary equipment."""


class DataSyntheticEngineSecondsDecorationsAuxInput2(BaseModel):
    name: str
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    value: bool
    """Boolean indicating the state of the auxiliary equipment."""


class DataSyntheticEngineSecondsDecorationsAuxInput3(BaseModel):
    name: str
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    value: bool
    """Boolean indicating the state of the auxiliary equipment."""


class DataSyntheticEngineSecondsDecorationsAuxInput4(BaseModel):
    name: str
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    value: bool
    """Boolean indicating the state of the auxiliary equipment."""


class DataSyntheticEngineSecondsDecorationsAuxInput5(BaseModel):
    name: str
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    value: bool
    """Boolean indicating the state of the auxiliary equipment."""


class DataSyntheticEngineSecondsDecorationsAuxInput6(BaseModel):
    name: str
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    value: bool
    """Boolean indicating the state of the auxiliary equipment."""


class DataSyntheticEngineSecondsDecorationsAuxInput7(BaseModel):
    name: str
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    value: bool
    """Boolean indicating the state of the auxiliary equipment."""


class DataSyntheticEngineSecondsDecorationsAuxInput8(BaseModel):
    name: str
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    value: bool
    """Boolean indicating the state of the auxiliary equipment."""


class DataSyntheticEngineSecondsDecorationsAuxInput9(BaseModel):
    name: str
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    value: bool
    """Boolean indicating the state of the auxiliary equipment."""


class DataSyntheticEngineSecondsDecorationsBarometricPressurePa(BaseModel):
    value: int
    """The barometric pressure reading in pascals."""


class DataSyntheticEngineSecondsDecorationsBatteryMilliVolts(BaseModel):
    value: int
    """The battery voltage in millivolts."""


class DataSyntheticEngineSecondsDecorationsDefLevelMilliPercent(BaseModel):
    value: int
    """The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g.

    `99001`, `49999`, etc).
    """


class DataSyntheticEngineSecondsDecorationsEcuSpeedMph(BaseModel):
    value: float
    """The speed of the vehicle in miles per hour, as reported by the ECU."""


class DataSyntheticEngineSecondsDecorationsEngineCoolantTemperatureMilliC(BaseModel):
    value: int
    """The engine coolant temperature reading in millidegree Celsius."""


class DataSyntheticEngineSecondsDecorationsEngineImmobilizer(BaseModel):
    connected: bool
    """Whether the engine immobilizer is connected or not"""

    state: Literal["ignition_disabled", "ignition_enabled"]
    """The state of the engine immobilizer.

    Valid values: `ignition_disabled`, `ignition_enabled`. This stat type will only
    return states of our first Engine Immobilizer Hardware (ACC-EI). Please use
    <a href="https://developers.samsara.com/reference/getengineimmobilizerstates" target="_blank">Get
    engine immobilizer states</a> to get states for both Engine Immobilizer Hardware
    versions (incl. HW-EI21).
    """

    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""


class DataSyntheticEngineSecondsDecorationsEngineLoadPercent(BaseModel):
    value: int
    """The engine load in percentage points (e.g. `99`, `50`, etc)."""


class DataSyntheticEngineSecondsDecorationsEngineOilPressureKPa(BaseModel):
    value: int
    """The engine oil pressure reading in kilopascals."""


class DataSyntheticEngineSecondsDecorationsEngineRpm(BaseModel):
    value: int
    """The revolutions per minute of the engine."""


class DataSyntheticEngineSecondsDecorationsEngineStates(BaseModel):
    value: Literal["Off", "On", "Idle"]
    """The state of the engine."""


class DataSyntheticEngineSecondsDecorationsEvAverageBatteryTemperatureMilliCelsius(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Battery temperature for electric and hybrid vehicles in milli celsius."""


class DataSyntheticEngineSecondsDecorationsEvBatteryCurrentMilliAmp(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Battery current for electric and hybrid vehicles in milli amps."""


class DataSyntheticEngineSecondsDecorationsEvBatteryStateOfHealthMilliPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Milli percent battery state of health for electric and hybrid vehicles."""


class DataSyntheticEngineSecondsDecorationsEvBatteryVoltageMilliVolt(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Battery voltage for electric and hybrid vehicles in milli volts."""


class DataSyntheticEngineSecondsDecorationsEvChargingCurrentMilliAmp(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Charging current for electric and hybrid vehicles in milli amps."""


class DataSyntheticEngineSecondsDecorationsEvChargingEnergyMicroWh(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Charging energy for electric and hybrid vehicles in microwatt hours."""


class DataSyntheticEngineSecondsDecorationsEvChargingStatus(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Literal[0, 1, 2, 3, 4]
    """Charging status for electric and hybrid vehicles.

    Statuses: unknown - 0, not charging - 1, charging - 2.
    """


class DataSyntheticEngineSecondsDecorationsEvChargingVoltageMilliVolt(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Charging voltage for electric and hybrid vehicles in milli volts."""


class DataSyntheticEngineSecondsDecorationsEvConsumedEnergyMicroWh(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """
    Consumed energy (including regenerated) for electric and hybrid vehicles in
    microwatt hours.
    """


class DataSyntheticEngineSecondsDecorationsEvDistanceDrivenMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Electric distance driven for electric and hybrid vehicles in meters."""


class DataSyntheticEngineSecondsDecorationsEvRegeneratedEnergyMicroWh(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Regenerated energy for electric and hybrid vehicles in microwatt hours."""


class DataSyntheticEngineSecondsDecorationsEvStateOfChargeMilliPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Milli percent State of Charge for electric and hybrid vehicles."""


class DataSyntheticEngineSecondsDecorationsFaultCodesJ1939CheckEngineLights(BaseModel):
    emissions_is_on: bool = FieldInfo(alias="emissionsIsOn")
    """True if the MIL status is nonzero."""

    protect_is_on: bool = FieldInfo(alias="protectIsOn")
    """True if the engine protect lamp status is nonzero."""

    stop_is_on: bool = FieldInfo(alias="stopIsOn")
    """True if the red lamp status is nonzero."""

    warning_is_on: bool = FieldInfo(alias="warningIsOn")
    """True if the amber lamp status is nonzero."""


class DataSyntheticEngineSecondsDecorationsFaultCodesJ1939DiagnosticTroubleCodeVendorSpecificFields(BaseModel):
    dtc_description: Optional[str] = FieldInfo(alias="dtcDescription", default=None)
    """The DTC description, if available."""

    repair_instructions_url: Optional[str] = FieldInfo(alias="repairInstructionsUrl", default=None)
    """A link to vendor repair instructions, if available."""


class DataSyntheticEngineSecondsDecorationsFaultCodesJ1939DiagnosticTroubleCode(BaseModel):
    fmi_id: int = FieldInfo(alias="fmiId")
    """The FMI identifier."""

    mil_status: int = FieldInfo(alias="milStatus")
    """The MIL status, indicating a check engine light."""

    occurrence_count: int = FieldInfo(alias="occurrenceCount")
    """The number of times this fault has triggered."""

    spn_id: int = FieldInfo(alias="spnId")
    """The SPN identifier."""

    tx_id: int = FieldInfo(alias="txId")
    """The TX identifier."""

    fmi_description: Optional[str] = FieldInfo(alias="fmiDescription", default=None)
    """A short description of the FMI identifier, if available."""

    source_address_name: Optional[str] = FieldInfo(alias="sourceAddressName", default=None)
    """The source address name corresponding to the txId"""

    spn_description: Optional[str] = FieldInfo(alias="spnDescription", default=None)
    """A short description of the SPN identifier, if available."""

    vendor_specific_fields: Optional[
        DataSyntheticEngineSecondsDecorationsFaultCodesJ1939DiagnosticTroubleCodeVendorSpecificFields
    ] = FieldInfo(alias="vendorSpecificFields", default=None)
    """Vendor specific data for J1939 vehicles."""


class DataSyntheticEngineSecondsDecorationsFaultCodesJ1939(BaseModel):
    check_engine_lights: Optional[DataSyntheticEngineSecondsDecorationsFaultCodesJ1939CheckEngineLights] = FieldInfo(
        alias="checkEngineLights", default=None
    )
    """Status of engine lights on J1939 vehicles."""

    diagnostic_trouble_codes: Optional[
        List[DataSyntheticEngineSecondsDecorationsFaultCodesJ1939DiagnosticTroubleCode]
    ] = FieldInfo(alias="diagnosticTroubleCodes", default=None)
    """Diagnostic trouble codes for J1939 vehicles."""


class DataSyntheticEngineSecondsDecorationsFaultCodesObdiiDiagnosticTroubleCodeConfirmedDtc(BaseModel):
    dtc_id: int = FieldInfo(alias="dtcId")
    """The DTC identifier."""

    dtc_description: Optional[str] = FieldInfo(alias="dtcDescription", default=None)
    """The DTC description, if available."""

    dtc_short_code: Optional[str] = FieldInfo(alias="dtcShortCode", default=None)
    """The DTC short code, if available."""


class DataSyntheticEngineSecondsDecorationsFaultCodesObdiiDiagnosticTroubleCodeMonitorStatus(BaseModel):
    catalyst: Optional[Literal["N", "R", "U"]] = None
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    comprehensive: Optional[Literal["N", "R", "U"]] = None
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    egr: Optional[Literal["N", "R", "U"]] = None
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    evap_system: Optional[Literal["N", "R", "U"]] = FieldInfo(alias="evapSystem", default=None)
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    fuel: Optional[Literal["N", "R", "U"]] = None
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    heated_catalyst: Optional[Literal["N", "R", "U"]] = FieldInfo(alias="heatedCatalyst", default=None)
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    heated_o2_sensor: Optional[Literal["N", "R", "U"]] = FieldInfo(alias="heatedO2Sensor", default=None)
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    iso_sae_reserved: Optional[Literal["N", "R", "U"]] = FieldInfo(alias="isoSaeReserved", default=None)
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    misfire: Optional[Literal["N", "R", "U"]] = None
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    not_ready_count: Optional[int] = FieldInfo(alias="notReadyCount", default=None)
    """Count of the number of sensors reporting N: Not Complete"""

    o2_sensor: Optional[Literal["N", "R", "U"]] = FieldInfo(alias="o2Sensor", default=None)
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""

    secondary_air: Optional[Literal["N", "R", "U"]] = FieldInfo(alias="secondaryAir", default=None)
    """Enum of monitor status: -U: Unsupported -N: Not Complete -R: Complete"""


class DataSyntheticEngineSecondsDecorationsFaultCodesObdiiDiagnosticTroubleCodePendingDtc(BaseModel):
    dtc_id: int = FieldInfo(alias="dtcId")
    """The DTC identifier."""

    dtc_description: Optional[str] = FieldInfo(alias="dtcDescription", default=None)
    """The DTC description, if available."""

    dtc_short_code: Optional[str] = FieldInfo(alias="dtcShortCode", default=None)
    """The DTC short code, if available."""


class DataSyntheticEngineSecondsDecorationsFaultCodesObdiiDiagnosticTroubleCodePermanentDtc(BaseModel):
    dtc_id: int = FieldInfo(alias="dtcId")
    """The DTC identifier."""

    dtc_description: Optional[str] = FieldInfo(alias="dtcDescription", default=None)
    """The DTC description, if available."""

    dtc_short_code: Optional[str] = FieldInfo(alias="dtcShortCode", default=None)
    """The DTC short code, if available."""


class DataSyntheticEngineSecondsDecorationsFaultCodesObdiiDiagnosticTroubleCode(BaseModel):
    tx_id: int = FieldInfo(alias="txId")
    """The TX identifier."""

    confirmed_dtcs: Optional[
        List[DataSyntheticEngineSecondsDecorationsFaultCodesObdiiDiagnosticTroubleCodeConfirmedDtc]
    ] = FieldInfo(alias="confirmedDtcs", default=None)
    """Confirmed DTC codes."""

    ignition_type: Optional[Literal["spark", "compression"]] = FieldInfo(alias="ignitionType", default=None)
    """The ignition type of this passenger vehicle.

    Valid values: `spark`, `compression`.
    """

    mil_status: Optional[bool] = FieldInfo(alias="milStatus", default=None)
    """The MIL status, indicating a check engine light."""

    monitor_status: Optional[DataSyntheticEngineSecondsDecorationsFaultCodesObdiiDiagnosticTroubleCodeMonitorStatus] = (
        FieldInfo(alias="monitorStatus", default=None)
    )
    """Readings from engine sensors"""

    pending_dtcs: Optional[
        List[DataSyntheticEngineSecondsDecorationsFaultCodesObdiiDiagnosticTroubleCodePendingDtc]
    ] = FieldInfo(alias="pendingDtcs", default=None)
    """Pending DTC codes."""

    permanent_dtcs: Optional[
        List[DataSyntheticEngineSecondsDecorationsFaultCodesObdiiDiagnosticTroubleCodePermanentDtc]
    ] = FieldInfo(alias="permanentDtcs", default=None)
    """Permanent DTC codes."""


class DataSyntheticEngineSecondsDecorationsFaultCodesObdii(BaseModel):
    check_engine_light_is_on: Optional[bool] = FieldInfo(alias="checkEngineLightIsOn", default=None)
    """
    True if the check engine light is illuminated (MIL status field is nonzero for
    any faults).
    """

    diagnostic_trouble_codes: Optional[
        List[DataSyntheticEngineSecondsDecorationsFaultCodesObdiiDiagnosticTroubleCode]
    ] = FieldInfo(alias="diagnosticTroubleCodes", default=None)
    """Diagnostic trouble codes for passenger vehicles."""


class DataSyntheticEngineSecondsDecorationsFaultCodesOemDiagnosticTroubleCode(BaseModel):
    code_description: Optional[str] = FieldInfo(alias="codeDescription", default=None)
    """The OEM code description."""

    code_identifier: Optional[str] = FieldInfo(alias="codeIdentifier", default=None)
    """The OEM code identifier."""

    code_severity: Optional[str] = FieldInfo(alias="codeSeverity", default=None)
    """The OEM code severity."""

    code_source: Optional[str] = FieldInfo(alias="codeSource", default=None)
    """The OEM code source."""


class DataSyntheticEngineSecondsDecorationsFaultCodesOem(BaseModel):
    diagnostic_trouble_codes: Optional[
        List[DataSyntheticEngineSecondsDecorationsFaultCodesOemDiagnosticTroubleCode]
    ] = FieldInfo(alias="diagnosticTroubleCodes", default=None)
    """Proprietary diagnostic trouble codes for OEM vehicles."""


class DataSyntheticEngineSecondsDecorationsFaultCodes(BaseModel):
    can_bus_type: Optional[str] = FieldInfo(alias="canBusType", default=None)
    """The CAN bus type of the vehicle."""

    j1939: Optional[DataSyntheticEngineSecondsDecorationsFaultCodesJ1939] = None
    """Vehicle fault codes for J1939 vehicles."""

    obdii: Optional[DataSyntheticEngineSecondsDecorationsFaultCodesObdii] = None
    """Vehicle fault codes for passenger vehicles."""

    oem: Optional[DataSyntheticEngineSecondsDecorationsFaultCodesOem] = None
    """Vehicle fault codes for OEM vehicles."""


class DataSyntheticEngineSecondsDecorationsFuelPercents(BaseModel):
    value: int
    """The engine fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataSyntheticEngineSecondsDecorationsGpsAddress(BaseModel):
    id: Optional[str] = None
    """Id of the address."""

    name: Optional[str] = None
    """Name of address."""


class DataSyntheticEngineSecondsDecorationsGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataSyntheticEngineSecondsDecorationsGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees"""

    longitude: float
    """GPS longitude represented in degrees"""

    address: Optional[DataSyntheticEngineSecondsDecorationsGpsAddress] = None
    """Address that the location is in."""

    heading_degrees: Optional[float] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the vehicle in degrees."""

    is_ecu_speed: Optional[bool] = FieldInfo(alias="isEcuSpeed", default=None)
    """True if the speed value is reported from the ECU.

    Speed value is reported from GPS otherwise.
    """

    reverse_geo: Optional[DataSyntheticEngineSecondsDecorationsGpsReverseGeo] = FieldInfo(
        alias="reverseGeo", default=None
    )
    """Reverse geocoded information."""

    speed_miles_per_hour: Optional[float] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the vehicle in miles per hour.

    See `isEcuSpeed` to determine speed data source.
    """


class DataSyntheticEngineSecondsDecorationsGpsDistanceMeters(BaseModel):
    value: float
    """
    Number of meters the vehicle has traveled since the gateway was installed, based
    on GPS calculations.
    """


class DataSyntheticEngineSecondsDecorationsGpsOdometerMeters(BaseModel):
    value: int
    """
    Number of meters the vehicle has traveled according to the GPS calculations and
    the manually-specified odometer reading.
    """


class DataSyntheticEngineSecondsDecorationsIntakeManifoldTemperatureMilliC(BaseModel):
    value: int
    """The intake manifold temperature reading in millidegree Celsius."""


class DataSyntheticEngineSecondsDecorationsObdEngineSeconds(BaseModel):
    value: int
    """
    Number of seconds the vehicle's engine has been on according to the on-board
    diagnostics.
    """


class DataSyntheticEngineSecondsDecorationsObdOdometerMeters(BaseModel):
    value: int
    """
    Number of meters the vehicle has traveled according to the on-board diagnostics.
    """


class DataSyntheticEngineSecondsDecorationsSeatbeltDriver(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Literal["Buckled", "Unbuckled"]
    """Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`."""


class DataSyntheticEngineSecondsDecorationsSpreaderActive(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Literal["Off", "On"]
    """Whether vehicle is actively spreading any material."""


class DataSyntheticEngineSecondsDecorationsSpreaderAirTemp(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Air (ambient) temperature in milli celsius reading from material spreader."""


class DataSyntheticEngineSecondsDecorationsSpreaderBlastState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Literal["On", "Off"]
    """Whether vehicle is actively spreading material in ‘blast mode’."""


class DataSyntheticEngineSecondsDecorationsSpreaderGranularName(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: str
    """
    Name of most recent type of granular material spread, read from the material
    spreader.
    """


class DataSyntheticEngineSecondsDecorationsSpreaderGranularRate(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """
    Granular spread rate reading in milliliters per meter, read from the material
    spreader. Unfiltered live stats are supplied as-read from the Material Spreader
    unit. Readings do not consider total spread rate(s) over time or distance.
    Unfiltered live stats are supplied as-read from the Material Spreader unit.
    Readings do not consider total spread rate(s) over time or distance.
    """


class DataSyntheticEngineSecondsDecorationsSpreaderLiquidName(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: str
    """
    Name of most recent type of liquid material spread, read from the material
    spreader.
    """


class DataSyntheticEngineSecondsDecorationsSpreaderLiquidRate(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """
    Liquid spread rate reading in milliliters per meter, read from the material
    spreader. Unfiltered live stats are supplied as-read from the Material Spreader
    unit. Readings do not consider total spread rate(s) over time or distance.
    Unfiltered live stats are supplied as-read from the Material Spreader unit.
    Readings do not consider total spread rate(s) over time or distance.
    """


class DataSyntheticEngineSecondsDecorationsSpreaderOnState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Literal["On", "Off"]
    """Whether vehicle spreader is enabled."""


class DataSyntheticEngineSecondsDecorationsSpreaderPlowStatus(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Literal["Up", "Down"]
    """Snow plow status, as read from the material spreader"""


class DataSyntheticEngineSecondsDecorationsSpreaderPrewetName(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: str
    """
    Name of most recent type of prewet material spread, read from the material
    spreader.
    """


class DataSyntheticEngineSecondsDecorationsSpreaderPrewetRate(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """
    Prewet spread rate reading in milliliters per meter, read from the material
    spreader. Unfiltered live stats are supplied as-read from the Material Spreader
    unit. Readings do not consider total spread rate(s) over time or distance.
    Unfiltered live stats are supplied as-read from the Material Spreader unit.
    Readings do not consider total spread rate(s) over time or distance.
    """


class DataSyntheticEngineSecondsDecorationsSpreaderRoadTemp(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """Road temperature reading in milli celsius from material spreader."""


class DataSyntheticEngineSecondsDecorationsTirePressure(BaseModel):
    back_left_tire_pressure_k_pa: Optional[int] = FieldInfo(alias="backLeftTirePressureKPa", default=None)
    """
    The tire pressure of the rear left tire as seen when standing behind the vehicle
    in kilopascals.
    """

    back_right_tire_pressure_k_pa: Optional[int] = FieldInfo(alias="backRightTirePressureKPa", default=None)
    """
    The tire pressure of the rear right tire as seen when standing behind the
    vehicle in kilopascals.
    """

    front_left_tire_pressure_k_pa: Optional[int] = FieldInfo(alias="frontLeftTirePressureKPa", default=None)
    """
    The tire pressure of the front left tire as seen when standing behind the
    vehicle in kilopascals.
    """

    front_right_tire_pressure_k_pa: Optional[int] = FieldInfo(alias="frontRightTirePressureKPa", default=None)
    """
    The tire pressure of the front right tire as seen when standing behind the
    vehicle in kilopascals.
    """


class DataSyntheticEngineSecondsDecorations(BaseModel):
    ambient_air_temperature_milli_c: Optional[DataSyntheticEngineSecondsDecorationsAmbientAirTemperatureMilliC] = (
        FieldInfo(alias="ambientAirTemperatureMilliC", default=None)
    )

    aux_input1: Optional[DataSyntheticEngineSecondsDecorationsAuxInput1] = FieldInfo(alias="auxInput1", default=None)

    aux_input10: Optional[DataSyntheticEngineSecondsDecorationsAuxInput10] = FieldInfo(alias="auxInput10", default=None)

    aux_input11: Optional[DataSyntheticEngineSecondsDecorationsAuxInput11] = FieldInfo(alias="auxInput11", default=None)

    aux_input12: Optional[DataSyntheticEngineSecondsDecorationsAuxInput12] = FieldInfo(alias="auxInput12", default=None)

    aux_input13: Optional[DataSyntheticEngineSecondsDecorationsAuxInput13] = FieldInfo(alias="auxInput13", default=None)

    aux_input2: Optional[DataSyntheticEngineSecondsDecorationsAuxInput2] = FieldInfo(alias="auxInput2", default=None)

    aux_input3: Optional[DataSyntheticEngineSecondsDecorationsAuxInput3] = FieldInfo(alias="auxInput3", default=None)

    aux_input4: Optional[DataSyntheticEngineSecondsDecorationsAuxInput4] = FieldInfo(alias="auxInput4", default=None)

    aux_input5: Optional[DataSyntheticEngineSecondsDecorationsAuxInput5] = FieldInfo(alias="auxInput5", default=None)

    aux_input6: Optional[DataSyntheticEngineSecondsDecorationsAuxInput6] = FieldInfo(alias="auxInput6", default=None)

    aux_input7: Optional[DataSyntheticEngineSecondsDecorationsAuxInput7] = FieldInfo(alias="auxInput7", default=None)

    aux_input8: Optional[DataSyntheticEngineSecondsDecorationsAuxInput8] = FieldInfo(alias="auxInput8", default=None)

    aux_input9: Optional[DataSyntheticEngineSecondsDecorationsAuxInput9] = FieldInfo(alias="auxInput9", default=None)

    barometric_pressure_pa: Optional[DataSyntheticEngineSecondsDecorationsBarometricPressurePa] = FieldInfo(
        alias="barometricPressurePa", default=None
    )

    battery_milli_volts: Optional[DataSyntheticEngineSecondsDecorationsBatteryMilliVolts] = FieldInfo(
        alias="batteryMilliVolts", default=None
    )

    def_level_milli_percent: Optional[DataSyntheticEngineSecondsDecorationsDefLevelMilliPercent] = FieldInfo(
        alias="defLevelMilliPercent", default=None
    )

    ecu_speed_mph: Optional[DataSyntheticEngineSecondsDecorationsEcuSpeedMph] = FieldInfo(
        alias="ecuSpeedMph", default=None
    )

    engine_coolant_temperature_milli_c: Optional[
        DataSyntheticEngineSecondsDecorationsEngineCoolantTemperatureMilliC
    ] = FieldInfo(alias="engineCoolantTemperatureMilliC", default=None)

    engine_immobilizer: Optional[DataSyntheticEngineSecondsDecorationsEngineImmobilizer] = FieldInfo(
        alias="engineImmobilizer", default=None
    )
    """Data for the engine immobilizer"""

    engine_load_percent: Optional[DataSyntheticEngineSecondsDecorationsEngineLoadPercent] = FieldInfo(
        alias="engineLoadPercent", default=None
    )

    engine_oil_pressure_k_pa: Optional[DataSyntheticEngineSecondsDecorationsEngineOilPressureKPa] = FieldInfo(
        alias="engineOilPressureKPa", default=None
    )

    engine_rpm: Optional[DataSyntheticEngineSecondsDecorationsEngineRpm] = FieldInfo(alias="engineRpm", default=None)

    engine_states: Optional[DataSyntheticEngineSecondsDecorationsEngineStates] = FieldInfo(
        alias="engineStates", default=None
    )

    ev_average_battery_temperature_milli_celsius: Optional[
        DataSyntheticEngineSecondsDecorationsEvAverageBatteryTemperatureMilliCelsius
    ] = FieldInfo(alias="evAverageBatteryTemperatureMilliCelsius", default=None)
    """Battery temperature for electric and hybrid vehicles in milli celsius.

    Not all EV and HEVs may report this field.
    """

    ev_battery_current_milli_amp: Optional[DataSyntheticEngineSecondsDecorationsEvBatteryCurrentMilliAmp] = FieldInfo(
        alias="evBatteryCurrentMilliAmp", default=None
    )
    """Battery current for electric and hybrid vehicles in milli amps.

    Not all EV and HEVs may report this field.
    """

    ev_battery_state_of_health_milli_percent: Optional[
        DataSyntheticEngineSecondsDecorationsEvBatteryStateOfHealthMilliPercent
    ] = FieldInfo(alias="evBatteryStateOfHealthMilliPercent", default=None)
    """Milli percent battery state of health for electric and hybrid vehicles.

    Not all EV and HEVs may report this field.
    """

    ev_battery_voltage_milli_volt: Optional[DataSyntheticEngineSecondsDecorationsEvBatteryVoltageMilliVolt] = FieldInfo(
        alias="evBatteryVoltageMilliVolt", default=None
    )
    """Battery voltage for electric and hybrid vehicles in milli volts.

    Not all EV and HEVs may report this field.
    """

    ev_charging_current_milli_amp: Optional[DataSyntheticEngineSecondsDecorationsEvChargingCurrentMilliAmp] = FieldInfo(
        alias="evChargingCurrentMilliAmp", default=None
    )
    """Charging current for electric and hybrid vehicles in milli amps.

    Not all EV and HEVs may report this field.
    """

    ev_charging_energy_micro_wh: Optional[DataSyntheticEngineSecondsDecorationsEvChargingEnergyMicroWh] = FieldInfo(
        alias="evChargingEnergyMicroWh", default=None
    )
    """Charging energy for electric and hybrid vehicles in microwatt hours.

    Not all EV and HEVs may report this field.
    """

    ev_charging_status: Optional[DataSyntheticEngineSecondsDecorationsEvChargingStatus] = FieldInfo(
        alias="evChargingStatus", default=None
    )
    """Charging status for electric and hybrid vehicles.

    Not all EV and HEVs may report this field.
    """

    ev_charging_voltage_milli_volt: Optional[DataSyntheticEngineSecondsDecorationsEvChargingVoltageMilliVolt] = (
        FieldInfo(alias="evChargingVoltageMilliVolt", default=None)
    )
    """Charging voltage for electric and hybrid vehicles in milli volts.

    Not all EV and HEVs may report this field.
    """

    ev_consumed_energy_micro_wh: Optional[DataSyntheticEngineSecondsDecorationsEvConsumedEnergyMicroWh] = FieldInfo(
        alias="evConsumedEnergyMicroWh", default=None
    )
    """
    Consumed energy (including regenerated) for electric and hybrid vehicles in
    microwatt hours. Not all EV and HEVs may report this field.
    """

    ev_distance_driven_meters: Optional[DataSyntheticEngineSecondsDecorationsEvDistanceDrivenMeters] = FieldInfo(
        alias="evDistanceDrivenMeters", default=None
    )
    """Electric distance driven for electric and hybrid vehicles in meters.

    Not all EV and HEVs may report this field.
    """

    ev_regenerated_energy_micro_wh: Optional[DataSyntheticEngineSecondsDecorationsEvRegeneratedEnergyMicroWh] = (
        FieldInfo(alias="evRegeneratedEnergyMicroWh", default=None)
    )
    """Regenerated energy for electric and hybrid vehicles in microwatt hours.

    Not all EV and HEVs may report this field.
    """

    ev_state_of_charge_milli_percent: Optional[DataSyntheticEngineSecondsDecorationsEvStateOfChargeMilliPercent] = (
        FieldInfo(alias="evStateOfChargeMilliPercent", default=None)
    )
    """State of Charge for electric and hybrid vehicles.

    Not all EV and HEVs may report this field.
    """

    fault_codes: Optional[DataSyntheticEngineSecondsDecorationsFaultCodes] = FieldInfo(alias="faultCodes", default=None)
    """Fault codes for the vehicle"""

    fuel_percents: Optional[DataSyntheticEngineSecondsDecorationsFuelPercents] = FieldInfo(
        alias="fuelPercents", default=None
    )

    gps: Optional[DataSyntheticEngineSecondsDecorationsGps] = None

    gps_distance_meters: Optional[DataSyntheticEngineSecondsDecorationsGpsDistanceMeters] = FieldInfo(
        alias="gpsDistanceMeters", default=None
    )

    gps_odometer_meters: Optional[DataSyntheticEngineSecondsDecorationsGpsOdometerMeters] = FieldInfo(
        alias="gpsOdometerMeters", default=None
    )

    intake_manifold_temperature_milli_c: Optional[
        DataSyntheticEngineSecondsDecorationsIntakeManifoldTemperatureMilliC
    ] = FieldInfo(alias="intakeManifoldTemperatureMilliC", default=None)

    obd_engine_seconds: Optional[DataSyntheticEngineSecondsDecorationsObdEngineSeconds] = FieldInfo(
        alias="obdEngineSeconds", default=None
    )

    obd_odometer_meters: Optional[DataSyntheticEngineSecondsDecorationsObdOdometerMeters] = FieldInfo(
        alias="obdOdometerMeters", default=None
    )

    seatbelt_driver: Optional[DataSyntheticEngineSecondsDecorationsSeatbeltDriver] = FieldInfo(
        alias="seatbeltDriver", default=None
    )
    """Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`."""

    spreader_active: Optional[DataSyntheticEngineSecondsDecorationsSpreaderActive] = FieldInfo(
        alias="spreaderActive", default=None
    )
    """Whether vehicle is actively spreading any material."""

    spreader_air_temp: Optional[DataSyntheticEngineSecondsDecorationsSpreaderAirTemp] = FieldInfo(
        alias="spreaderAirTemp", default=None
    )
    """Air (ambient) temperature in milli celsius reading from material spreader."""

    spreader_blast_state: Optional[DataSyntheticEngineSecondsDecorationsSpreaderBlastState] = FieldInfo(
        alias="spreaderBlastState", default=None
    )
    """Whether vehicle is actively spreading material in ‘blast mode’."""

    spreader_granular_name: Optional[DataSyntheticEngineSecondsDecorationsSpreaderGranularName] = FieldInfo(
        alias="spreaderGranularName", default=None
    )
    """
    Name of most recent type of granular material spread, read from the material
    spreader.
    """

    spreader_granular_rate: Optional[DataSyntheticEngineSecondsDecorationsSpreaderGranularRate] = FieldInfo(
        alias="spreaderGranularRate", default=None
    )
    """
    Granular spread rate reading in milliliters per meter, read from the material
    spreader. Unfiltered live stats are supplied as-read from the Material Spreader
    unit. Readings do not consider total spread rate(s) over time or distance.
    Unfiltered live stats are supplied as-read from the Material Spreader unit.
    Readings do not consider total spread rate(s) over time or distance.
    """

    spreader_liquid_name: Optional[DataSyntheticEngineSecondsDecorationsSpreaderLiquidName] = FieldInfo(
        alias="spreaderLiquidName", default=None
    )
    """
    Name of most recent type of liquid material spread, read from the material
    spreader.
    """

    spreader_liquid_rate: Optional[DataSyntheticEngineSecondsDecorationsSpreaderLiquidRate] = FieldInfo(
        alias="spreaderLiquidRate", default=None
    )
    """
    Liquid spread rate reading in milliliters per meter, read from the material
    spreader. Unfiltered live stats are supplied as-read from the Material Spreader
    unit. Readings do not consider total spread rate(s) over time or distance.
    Unfiltered live stats are supplied as-read from the Material Spreader unit.
    Readings do not consider total spread rate(s) over time or distance.
    """

    spreader_on_state: Optional[DataSyntheticEngineSecondsDecorationsSpreaderOnState] = FieldInfo(
        alias="spreaderOnState", default=None
    )
    """Whether vehicle spreader is enabled."""

    spreader_plow_status: Optional[DataSyntheticEngineSecondsDecorationsSpreaderPlowStatus] = FieldInfo(
        alias="spreaderPlowStatus", default=None
    )
    """Snow plow status (`Up` or `Down`), as read from the material spreader.

    Note: this is separate from plow status defined via auxInput.
    """

    spreader_prewet_name: Optional[DataSyntheticEngineSecondsDecorationsSpreaderPrewetName] = FieldInfo(
        alias="spreaderPrewetName", default=None
    )
    """
    Name of most recent type of prewet material spread, read from the material
    spreader.
    """

    spreader_prewet_rate: Optional[DataSyntheticEngineSecondsDecorationsSpreaderPrewetRate] = FieldInfo(
        alias="spreaderPrewetRate", default=None
    )
    """
    Prewet spread rate reading in milliliters per meter, read from the material
    spreader. Unfiltered live stats are supplied as-read from the Material Spreader
    unit. Readings do not consider total spread rate(s) over time or distance.
    Unfiltered live stats are supplied as-read from the Material Spreader unit.
    Readings do not consider total spread rate(s) over time or distance.
    """

    spreader_road_temp: Optional[DataSyntheticEngineSecondsDecorationsSpreaderRoadTemp] = FieldInfo(
        alias="spreaderRoadTemp", default=None
    )
    """Road temperature reading in milli celsius from material spreader."""

    tire_pressure: Optional[DataSyntheticEngineSecondsDecorationsTirePressure] = FieldInfo(
        alias="tirePressure", default=None
    )
    """Tire pressure readings for each of four tires in kilopascals."""


class DataSyntheticEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    """
    Stats for the number of seconds the vehicle's engine has been on, calculated
    based on a manually-specified engine seconds reading and the number of seconds
    the vehicle has been on according to the engine state changes reported to the
    vehicle gateway since that reading was set. This stat will not be present for
    any vehicle that does not have the engine seconds reading set. The engine
    seconds reading can be set from the UI on the vehicle details page.
    """

    decorations: Optional[DataSyntheticEngineSecondsDecorations] = None
    """Optional decorations to the primary stat event.

    See [here](doc:decorations) for more details. The example shows the response if
    you were to submit `decorations=engineStates&obdEngineSeconds` to the query
    parameter:

    ```json
    "decorations":{
      "engineStates": {
        "value": "Off"
      },
      "obdEngineSeconds": {
        "value": 9723103
      }
    }
    ```
    """


class Data(BaseModel):
    id: str
    """The unique Samsara ID of the Vehicle.

    This is automatically generated when the Vehicle object is created. It cannot be
    changed.
    """

    name: str
    """The human-readable name of the Vehicle.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. **By default**, this name is
    the serial number of the Samsara Vehicle Gateway. It can be set or updated
    through the Samsara Dashboard or through the API at any time.
    """

    ambient_air_temperature_milli_c: Optional[DataAmbientAirTemperatureMilliC] = FieldInfo(
        alias="ambientAirTemperatureMilliC", default=None
    )
    """Vehicle ambient air temperature reading."""

    aux_input1: Optional[DataAuxInput1] = FieldInfo(alias="auxInput1", default=None)
    """Data for auxiliary digio equipment."""

    aux_input10: Optional[DataAuxInput10] = FieldInfo(alias="auxInput10", default=None)
    """Data for auxiliary digio equipment."""

    aux_input11: Optional[DataAuxInput11] = FieldInfo(alias="auxInput11", default=None)
    """Data for auxiliary digio equipment."""

    aux_input12: Optional[DataAuxInput12] = FieldInfo(alias="auxInput12", default=None)
    """Data for auxiliary digio equipment."""

    aux_input13: Optional[DataAuxInput13] = FieldInfo(alias="auxInput13", default=None)
    """Data for auxiliary digio equipment."""

    aux_input2: Optional[DataAuxInput2] = FieldInfo(alias="auxInput2", default=None)
    """Data for auxiliary digio equipment."""

    aux_input3: Optional[DataAuxInput3] = FieldInfo(alias="auxInput3", default=None)
    """Data for auxiliary digio equipment."""

    aux_input4: Optional[DataAuxInput4] = FieldInfo(alias="auxInput4", default=None)
    """Data for auxiliary digio equipment."""

    aux_input5: Optional[DataAuxInput5] = FieldInfo(alias="auxInput5", default=None)
    """Data for auxiliary digio equipment."""

    aux_input6: Optional[DataAuxInput6] = FieldInfo(alias="auxInput6", default=None)
    """Data for auxiliary digio equipment."""

    aux_input7: Optional[DataAuxInput7] = FieldInfo(alias="auxInput7", default=None)
    """Data for auxiliary digio equipment."""

    aux_input8: Optional[DataAuxInput8] = FieldInfo(alias="auxInput8", default=None)
    """Data for auxiliary digio equipment."""

    aux_input9: Optional[DataAuxInput9] = FieldInfo(alias="auxInput9", default=None)
    """Data for auxiliary digio equipment."""

    barometric_pressure_pa: Optional[DataBarometricPressurePa] = FieldInfo(alias="barometricPressurePa", default=None)
    """Vehicle barometric pressure reading."""

    battery_milli_volts: Optional[DataBatteryMilliVolts] = FieldInfo(alias="batteryMilliVolts", default=None)
    """Vehicle battery voltage reading."""

    def_level_milli_percent: Optional[DataDefLevelMilliPercent] = FieldInfo(alias="defLevelMilliPercent", default=None)
    """The Diesel Exhaust Fluid (DEF) milli percentage reading."""

    ecu_speed_mph: Optional[DataEcuSpeedMph] = FieldInfo(alias="ecuSpeedMph", default=None)
    """The speed of the vehicle in miles per hour, as reported by the ECU."""

    engine_coolant_temperature_milli_c: Optional[DataEngineCoolantTemperatureMilliC] = FieldInfo(
        alias="engineCoolantTemperatureMilliC", default=None
    )
    """Vehicle engine coolant temperature reading."""

    engine_immobilizer: Optional[DataEngineImmobilizer] = FieldInfo(alias="engineImmobilizer", default=None)
    """Data for the engine immobilizer"""

    engine_load_percent: Optional[DataEngineLoadPercent] = FieldInfo(alias="engineLoadPercent", default=None)
    """The engine load percentage reading."""

    engine_oil_pressure_k_pa: Optional[DataEngineOilPressureKPa] = FieldInfo(alias="engineOilPressureKPa", default=None)
    """Vehicle engine oil pressure reading."""

    engine_rpm: Optional[DataEngineRpm] = FieldInfo(alias="engineRpm", default=None)
    """Vehicle engine RPM reading."""

    engine_state: Optional[DataEngineState] = FieldInfo(alias="engineState", default=None)
    """Vehicle engine state event."""

    ev_average_battery_temperature_milli_celsius: Optional[DataEvAverageBatteryTemperatureMilliCelsius] = FieldInfo(
        alias="evAverageBatteryTemperatureMilliCelsius", default=None
    )
    """Battery temperature for electric and hybrid vehicles in milli celsius.

    Not all EV and HEVs may report this field.
    """

    ev_battery_current_milli_amp: Optional[DataEvBatteryCurrentMilliAmp] = FieldInfo(
        alias="evBatteryCurrentMilliAmp", default=None
    )
    """Battery current for electric and hybrid vehicles in milli amps.

    Not all EV and HEVs may report this field.
    """

    ev_battery_state_of_health_milli_percent: Optional[DataEvBatteryStateOfHealthMilliPercent] = FieldInfo(
        alias="evBatteryStateOfHealthMilliPercent", default=None
    )
    """Milli percent battery state of health for electric and hybrid vehicles.

    Not all EV and HEVs may report this field.
    """

    ev_battery_voltage_milli_volt: Optional[DataEvBatteryVoltageMilliVolt] = FieldInfo(
        alias="evBatteryVoltageMilliVolt", default=None
    )
    """Battery voltage for electric and hybrid vehicles in milli volts.

    Not all EV and HEVs may report this field.
    """

    ev_charging_current_milli_amp: Optional[DataEvChargingCurrentMilliAmp] = FieldInfo(
        alias="evChargingCurrentMilliAmp", default=None
    )
    """Charging current for electric and hybrid vehicles in milli amps.

    Not all EV and HEVs may report this field.
    """

    ev_charging_energy_micro_wh: Optional[DataEvChargingEnergyMicroWh] = FieldInfo(
        alias="evChargingEnergyMicroWh", default=None
    )
    """Charging energy for electric and hybrid vehicles in microwatt hours.

    Not all EV and HEVs may report this field.
    """

    ev_charging_status: Optional[DataEvChargingStatus] = FieldInfo(alias="evChargingStatus", default=None)
    """Charging status for electric and hybrid vehicles.

    Not all EV and HEVs may report this field.
    """

    ev_charging_voltage_milli_volt: Optional[DataEvChargingVoltageMilliVolt] = FieldInfo(
        alias="evChargingVoltageMilliVolt", default=None
    )
    """Charging voltage for electric and hybrid vehicles in milli volts.

    Not all EV and HEVs may report this field.
    """

    ev_consumed_energy_micro_wh: Optional[DataEvConsumedEnergyMicroWh] = FieldInfo(
        alias="evConsumedEnergyMicroWh", default=None
    )
    """
    Consumed energy (including regenerated) for electric and hybrid vehicles in
    microwatt hours. Not all EV and HEVs may report this field.
    """

    ev_distance_driven_meters: Optional[DataEvDistanceDrivenMeters] = FieldInfo(
        alias="evDistanceDrivenMeters", default=None
    )
    """Electric distance driven for electric and hybrid vehicles in meters.

    Not all EV and HEVs may report this field.
    """

    ev_regenerated_energy_micro_wh: Optional[DataEvRegeneratedEnergyMicroWh] = FieldInfo(
        alias="evRegeneratedEnergyMicroWh", default=None
    )
    """Regenerated energy for electric and hybrid vehicles in microwatt hours.

    Not all EV and HEVs may report this field.
    """

    ev_state_of_charge_milli_percent: Optional[DataEvStateOfChargeMilliPercent] = FieldInfo(
        alias="evStateOfChargeMilliPercent", default=None
    )
    """State of Charge for electric and hybrid vehicles.

    Not all EV and HEVs may report this field.
    """

    external_ids: Optional[object] = FieldInfo(alias="externalIds", default=None)
    """
    The <a href="/docs/external-ids" target="_blank">external IDs</a> for the given
    object.
    """

    fault_codes: Optional[DataFaultCodes] = FieldInfo(alias="faultCodes", default=None)
    """Engine fault codes read from J1939, OBDII, and OEM vehicles."""

    fuel_percent: Optional[DataFuelPercent] = FieldInfo(alias="fuelPercent", default=None)
    """Vehicle fuel percentage reading."""

    gps: Optional[DataGps] = None
    """GPS location data for the vehicle."""

    gps_distance_meters: Optional[DataGpsDistanceMeters] = FieldInfo(alias="gpsDistanceMeters", default=None)
    """Vehicle GPS distance event."""

    gps_odometer_meters: Optional[DataGpsOdometerMeters] = FieldInfo(alias="gpsOdometerMeters", default=None)
    """Vehicle GPS odometer event."""

    intake_manifold_temperature_milli_c: Optional[DataIntakeManifoldTemperatureMilliC] = FieldInfo(
        alias="intakeManifoldTemperatureMilliC", default=None
    )
    """Vehicle intake manifold temperature reading."""

    nfc_card_scan: Optional[DataNfcCardScan] = FieldInfo(alias="nfcCardScan", default=None)
    """Data for the nfc card and the time that it was scanned."""

    obd_engine_seconds: Optional[DataObdEngineSeconds] = FieldInfo(alias="obdEngineSeconds", default=None)
    """Vehicle OBD engine seconds reading."""

    obd_odometer_meters: Optional[DataObdOdometerMeters] = FieldInfo(alias="obdOdometerMeters", default=None)
    """Vehicle OBD odometer reading."""

    seatbelt_driver: Optional[DataSeatbeltDriver] = FieldInfo(alias="seatbeltDriver", default=None)
    """Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`."""

    spreader_active: Optional[DataSpreaderActive] = FieldInfo(alias="spreaderActive", default=None)
    """Whether vehicle is actively spreading any material."""

    spreader_air_temp: Optional[DataSpreaderAirTemp] = FieldInfo(alias="spreaderAirTemp", default=None)
    """Air (ambient) temperature in milli celsius reading from material spreader."""

    spreader_blast_state: Optional[DataSpreaderBlastState] = FieldInfo(alias="spreaderBlastState", default=None)
    """Whether vehicle is actively spreading material in ‘blast mode’."""

    spreader_granular_name: Optional[DataSpreaderGranularName] = FieldInfo(alias="spreaderGranularName", default=None)
    """
    Name of most recent type of granular material spread, read from the material
    spreader.
    """

    spreader_granular_rate: Optional[DataSpreaderGranularRate] = FieldInfo(alias="spreaderGranularRate", default=None)
    """
    Granular spread rate reading in milliliters per meter, read from the material
    spreader. Unfiltered live stats are supplied as-read from the Material Spreader
    unit. Readings do not consider total spread rate(s) over time or distance.
    Unfiltered live stats are supplied as-read from the Material Spreader unit.
    Readings do not consider total spread rate(s) over time or distance.
    """

    spreader_liquid_name: Optional[DataSpreaderLiquidName] = FieldInfo(alias="spreaderLiquidName", default=None)
    """
    Name of most recent type of liquid material spread, read from the material
    spreader.
    """

    spreader_liquid_rate: Optional[DataSpreaderLiquidRate] = FieldInfo(alias="spreaderLiquidRate", default=None)
    """
    Liquid spread rate reading in milliliters per meter, read from the material
    spreader. Unfiltered live stats are supplied as-read from the Material Spreader
    unit. Readings do not consider total spread rate(s) over time or distance.
    Unfiltered live stats are supplied as-read from the Material Spreader unit.
    Readings do not consider total spread rate(s) over time or distance.
    """

    spreader_on_state: Optional[DataSpreaderOnState] = FieldInfo(alias="spreaderOnState", default=None)
    """Whether vehicle spreader is enabled."""

    spreader_plow_status: Optional[DataSpreaderPlowStatus] = FieldInfo(alias="spreaderPlowStatus", default=None)
    """Snow plow status (`Up` or `Down`), as read from the material spreader.

    Note: this is separate from plow status defined via auxInput.
    """

    spreader_prewet_name: Optional[DataSpreaderPrewetName] = FieldInfo(alias="spreaderPrewetName", default=None)
    """
    Name of most recent type of prewet material spread, read from the material
    spreader.
    """

    spreader_prewet_rate: Optional[DataSpreaderPrewetRate] = FieldInfo(alias="spreaderPrewetRate", default=None)
    """
    Prewet spread rate reading in milliliters per meter, read from the material
    spreader. Unfiltered live stats are supplied as-read from the Material Spreader
    unit. Readings do not consider total spread rate(s) over time or distance.
    Unfiltered live stats are supplied as-read from the Material Spreader unit.
    Readings do not consider total spread rate(s) over time or distance.
    """

    spreader_road_temp: Optional[DataSpreaderRoadTemp] = FieldInfo(alias="spreaderRoadTemp", default=None)
    """Road temperature reading in milli celsius from material spreader."""

    synthetic_engine_seconds: Optional[DataSyntheticEngineSeconds] = FieldInfo(
        alias="syntheticEngineSeconds", default=None
    )
    """Data for the synthetic engine seconds for the vehicle"""


class Pagination(BaseModel):
    end_cursor: str = FieldInfo(alias="endCursor")
    """Cursor identifier representing the last element in the response.

    This value should be used in conjunction with a subsequent request's 'after'
    query parameter. This may be an empty string if there are no more pages left to
    view.
    """

    has_next_page: bool = FieldInfo(alias="hasNextPage")
    """
    True if there are more pages of results immediately available after this
    endCursor.
    """


class VehicleStatsResponse(BaseModel):
    data: List[Data]
    """List of vehicles and a snapshot of the request stats."""

    pagination: Pagination
    """Pagination parameters."""
