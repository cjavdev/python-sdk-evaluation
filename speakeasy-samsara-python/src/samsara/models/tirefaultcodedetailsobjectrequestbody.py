"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TireFaultCodeDetailsObjectRequestBodyManufacturer(str, Enum):
    r"""The tire manufacturer.  Valid values: `MANUFACTURER_BENDIX`, `MANUFACTURER_CONTINENTAL`, `MANUFACTURER_DORAN`, `MANUFACTURER_HENDRICKSON`, `MANUFACTURER_INVALID`, `MANUFACTURER_PRESSURE_PRO`, `MANUFACTURER_UNIVERSAL_J1939`, `MANUFACTURER_UNIVERSAL_R141`"""

    MANUFACTURER_BENDIX = "MANUFACTURER_BENDIX"
    MANUFACTURER_CONTINENTAL = "MANUFACTURER_CONTINENTAL"
    MANUFACTURER_DORAN = "MANUFACTURER_DORAN"
    MANUFACTURER_HENDRICKSON = "MANUFACTURER_HENDRICKSON"
    MANUFACTURER_INVALID = "MANUFACTURER_INVALID"
    MANUFACTURER_PRESSURE_PRO = "MANUFACTURER_PRESSURE_PRO"
    MANUFACTURER_UNIVERSAL_J1939 = "MANUFACTURER_UNIVERSAL_J1939"
    MANUFACTURER_UNIVERSAL_R141 = "MANUFACTURER_UNIVERSAL_R141"


class TireFaultCodeDetailsObjectRequestBodySpecificTireFaultCodes(str, Enum):
    r"""The specific tire fault codes.  Valid values: `TIRE_ALERT_ACROSS_AXLE_FAULT`, `TIRE_ALERT_EXTREME_OVER_PRESSURE`, `TIRE_ALERT_EXTREME_UNDER_PRESSURE`, `TIRE_ALERT_INVALID`, `TIRE_ALERT_LEAK_DETECTED`, `TIRE_ALERT_OVER_PRESSURE`, `TIRE_ALERT_OVER_TEMPERATURE`, `TIRE_ALERT_UNDER_PRESSURE`"""

    TIRE_ALERT_ACROSS_AXLE_FAULT = "TIRE_ALERT_ACROSS_AXLE_FAULT"
    TIRE_ALERT_EXTREME_OVER_PRESSURE = "TIRE_ALERT_EXTREME_OVER_PRESSURE"
    TIRE_ALERT_EXTREME_UNDER_PRESSURE = "TIRE_ALERT_EXTREME_UNDER_PRESSURE"
    TIRE_ALERT_INVALID = "TIRE_ALERT_INVALID"
    TIRE_ALERT_LEAK_DETECTED = "TIRE_ALERT_LEAK_DETECTED"
    TIRE_ALERT_OVER_PRESSURE = "TIRE_ALERT_OVER_PRESSURE"
    TIRE_ALERT_OVER_TEMPERATURE = "TIRE_ALERT_OVER_TEMPERATURE"
    TIRE_ALERT_UNDER_PRESSURE = "TIRE_ALERT_UNDER_PRESSURE"


class TireFaultCodeDetailsObjectRequestBodyTypedDict(TypedDict):
    r"""Details specific to Tire Fault Code. At least one fault code or fault code group must be selected."""

    manufacturer: TireFaultCodeDetailsObjectRequestBodyManufacturer
    r"""The tire manufacturer.  Valid values: `MANUFACTURER_BENDIX`, `MANUFACTURER_CONTINENTAL`, `MANUFACTURER_DORAN`, `MANUFACTURER_HENDRICKSON`, `MANUFACTURER_INVALID`, `MANUFACTURER_PRESSURE_PRO`, `MANUFACTURER_UNIVERSAL_J1939`, `MANUFACTURER_UNIVERSAL_R141`"""
    has_cautionary_tire_fault_codes: NotRequired[bool]
    r"""If true then alert over pressure, under pressure, across axle fault, or leak detected fault codes. Defaults to false."""
    has_critical_tire_fault_codes: NotRequired[bool]
    r"""If true then alert over temperature or extreme pressure over or under fault codes. Defaults to false."""
    specific_tire_fault_codes: NotRequired[
        List[TireFaultCodeDetailsObjectRequestBodySpecificTireFaultCodes]
    ]
    r"""The list of specific tire fault codes to be alerted on."""


class TireFaultCodeDetailsObjectRequestBody(BaseModel):
    r"""Details specific to Tire Fault Code. At least one fault code or fault code group must be selected."""

    manufacturer: TireFaultCodeDetailsObjectRequestBodyManufacturer
    r"""The tire manufacturer.  Valid values: `MANUFACTURER_BENDIX`, `MANUFACTURER_CONTINENTAL`, `MANUFACTURER_DORAN`, `MANUFACTURER_HENDRICKSON`, `MANUFACTURER_INVALID`, `MANUFACTURER_PRESSURE_PRO`, `MANUFACTURER_UNIVERSAL_J1939`, `MANUFACTURER_UNIVERSAL_R141`"""

    has_cautionary_tire_fault_codes: Annotated[
        Optional[bool], pydantic.Field(alias="hasCautionaryTireFaultCodes")
    ] = None
    r"""If true then alert over pressure, under pressure, across axle fault, or leak detected fault codes. Defaults to false."""

    has_critical_tire_fault_codes: Annotated[
        Optional[bool], pydantic.Field(alias="hasCriticalTireFaultCodes")
    ] = None
    r"""If true then alert over temperature or extreme pressure over or under fault codes. Defaults to false."""

    specific_tire_fault_codes: Annotated[
        Optional[List[TireFaultCodeDetailsObjectRequestBodySpecificTireFaultCodes]],
        pydantic.Field(alias="specificTireFaultCodes"),
    ] = None
    r"""The list of specific tire fault codes to be alerted on."""
