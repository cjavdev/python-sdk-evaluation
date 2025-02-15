"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .vehiclestatsfaultcodesoemtroublecode import (
    VehicleStatsFaultCodesOemTroubleCode,
    VehicleStatsFaultCodesOemTroubleCodeTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class VehicleStatsFaultCodesOemTypedDict(TypedDict):
    r"""Vehicle fault codes for OEM vehicles."""

    diagnostic_trouble_codes: NotRequired[
        List[VehicleStatsFaultCodesOemTroubleCodeTypedDict]
    ]
    r"""Proprietary diagnostic trouble codes for OEM vehicles."""


class VehicleStatsFaultCodesOem(BaseModel):
    r"""Vehicle fault codes for OEM vehicles."""

    diagnostic_trouble_codes: Annotated[
        Optional[List[VehicleStatsFaultCodesOemTroubleCode]],
        pydantic.Field(alias="diagnosticTroubleCodes"),
    ] = None
    r"""Proprietary diagnostic trouble codes for OEM vehicles."""
