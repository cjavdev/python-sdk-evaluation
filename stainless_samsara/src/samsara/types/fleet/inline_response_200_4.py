# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "InlineResponse200_4",
    "Vehicle",
    "VehicleJ1939",
    "VehicleJ1939CheckEngineLight",
    "VehicleJ1939DiagnosticTroubleCode",
    "VehiclePassenger",
    "VehiclePassengerCheckEngineLight",
    "VehiclePassengerDiagnosticTroubleCode",
]


class VehicleJ1939CheckEngineLight(BaseModel):
    emissions_is_on: Optional[bool] = FieldInfo(alias="emissionsIsOn", default=None)

    protect_is_on: Optional[bool] = FieldInfo(alias="protectIsOn", default=None)

    stop_is_on: Optional[bool] = FieldInfo(alias="stopIsOn", default=None)

    warning_is_on: Optional[bool] = FieldInfo(alias="warningIsOn", default=None)


class VehicleJ1939DiagnosticTroubleCode(BaseModel):
    fmi_id: int = FieldInfo(alias="fmiId")

    fmi_text: str = FieldInfo(alias="fmiText")

    occurrence_count: int = FieldInfo(alias="occurrenceCount")

    spn_description: str = FieldInfo(alias="spnDescription")

    spn_id: int = FieldInfo(alias="spnId")

    tx_id: int = FieldInfo(alias="txId")


class VehicleJ1939(BaseModel):
    check_engine_light: Optional[VehicleJ1939CheckEngineLight] = FieldInfo(alias="checkEngineLight", default=None)
    """J1939 check engine lights."""

    diagnostic_trouble_codes: Optional[List[VehicleJ1939DiagnosticTroubleCode]] = FieldInfo(
        alias="diagnosticTroubleCodes", default=None
    )
    """J1939 DTCs."""


class VehiclePassengerCheckEngineLight(BaseModel):
    is_on: Optional[bool] = FieldInfo(alias="isOn", default=None)


class VehiclePassengerDiagnosticTroubleCode(BaseModel):
    dtc_description: str = FieldInfo(alias="dtcDescription")

    dtc_id: int = FieldInfo(alias="dtcId")

    dtc_short_code: str = FieldInfo(alias="dtcShortCode")


class VehiclePassenger(BaseModel):
    check_engine_light: Optional[VehiclePassengerCheckEngineLight] = FieldInfo(alias="checkEngineLight", default=None)
    """Passenger vehicle check engine light."""

    diagnostic_trouble_codes: Optional[List[VehiclePassengerDiagnosticTroubleCode]] = FieldInfo(
        alias="diagnosticTroubleCodes", default=None
    )
    """Passenger vehicle DTCs."""


class Vehicle(BaseModel):
    id: int
    """ID of the vehicle."""

    j1939: Optional[VehicleJ1939] = None
    """J1939 based data. Null if no data is available."""

    passenger: Optional[VehiclePassenger] = None
    """Passenger vehicle data. Null if no data is available."""


class InlineResponse200_4(BaseModel):
    vehicles: Optional[List[Vehicle]] = None
