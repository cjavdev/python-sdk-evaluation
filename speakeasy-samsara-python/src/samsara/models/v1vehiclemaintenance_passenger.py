"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v1vehiclemaintenance_passenger_checkenginelight import (
    V1VehicleMaintenancePassengerCheckEngineLight,
    V1VehicleMaintenancePassengerCheckEngineLightTypedDict,
)
from .v1vehiclemaintenance_passenger_diagnostictroublecodes import (
    V1VehicleMaintenancePassengerDiagnosticTroubleCodes,
    V1VehicleMaintenancePassengerDiagnosticTroubleCodesTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V1VehicleMaintenancePassengerTypedDict(TypedDict):
    r"""Passenger vehicle data. Null if no data is available."""

    check_engine_light: NotRequired[
        V1VehicleMaintenancePassengerCheckEngineLightTypedDict
    ]
    r"""Passenger vehicle check engine light."""
    diagnostic_trouble_codes: NotRequired[
        List[V1VehicleMaintenancePassengerDiagnosticTroubleCodesTypedDict]
    ]
    r"""Passenger vehicle DTCs."""


class V1VehicleMaintenancePassenger(BaseModel):
    r"""Passenger vehicle data. Null if no data is available."""

    check_engine_light: Annotated[
        Optional[V1VehicleMaintenancePassengerCheckEngineLight],
        pydantic.Field(alias="checkEngineLight"),
    ] = None
    r"""Passenger vehicle check engine light."""

    diagnostic_trouble_codes: Annotated[
        Optional[List[V1VehicleMaintenancePassengerDiagnosticTroubleCodes]],
        pydantic.Field(alias="diagnosticTroubleCodes"),
    ] = None
    r"""Passenger vehicle DTCs."""
