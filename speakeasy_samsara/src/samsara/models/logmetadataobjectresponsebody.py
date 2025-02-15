"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .vehicleresponseresponsebody import (
    VehicleResponseResponseBody,
    VehicleResponseResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class LogMetaDataObjectResponseBodyTypedDict(TypedDict):
    r"""The metadata of the log."""

    adverse_driving_claimed: NotRequired[bool]
    r"""Whether the driver has claimed the [Adverse Driving Exemption](https://kb.samsara.com/hc/en-us/articles/360047336792-Adverse-Driving-Exemption) for this HOS day chart."""
    big_day_claimed: NotRequired[bool]
    r"""Whether the driver has claimed the [Big Day Exemption](https://kb.samsara.com/hc/en-us/articles/360057113891-16-Hour-Short-Haul-Exemption-Big-Day-) for this HOS day chart."""
    carrier_formatted_address: NotRequired[str]
    r"""The address of the carrier used for this HOS chart."""
    carrier_name: NotRequired[str]
    r"""The name of the carrier used for this HOS chart."""
    carrier_us_dot_number: NotRequired[int]
    r"""The US DOT number of the carrier used for this HOS chart."""
    certified_at_time: NotRequired[str]
    r"""The time this log was certified in RFC 3339 format."""
    home_terminal_formatted_address: NotRequired[str]
    r"""The address of the Home Terminal used for this HOS chart."""
    home_terminal_name: NotRequired[str]
    r"""The name of the Home Terminal used for this HOS chart."""
    is_certified: NotRequired[bool]
    r"""Whether this HOS day chart was certified by the driver."""
    is_us_short_haul_active: NotRequired[bool]
    r"""Whether the driver has the 150 air-mile Short Haul Exemption active for this HOS day chart."""
    shipping_docs: NotRequired[str]
    r"""List of shipping document names associated with the driver for the day. This field maps to Shipping ID in the dashboard."""
    trailer_names: NotRequired[List[str]]
    r"""List of trailer names associated with the driver for the day. If a trailer was associated with a log through the driver app the trailer name will be the trailer ID."""
    vehicles: NotRequired[List[VehicleResponseResponseBodyTypedDict]]
    r"""List of vehicles associated with the driver for the day."""


class LogMetaDataObjectResponseBody(BaseModel):
    r"""The metadata of the log."""

    adverse_driving_claimed: Annotated[
        Optional[bool], pydantic.Field(alias="adverseDrivingClaimed")
    ] = None
    r"""Whether the driver has claimed the [Adverse Driving Exemption](https://kb.samsara.com/hc/en-us/articles/360047336792-Adverse-Driving-Exemption) for this HOS day chart."""

    big_day_claimed: Annotated[
        Optional[bool], pydantic.Field(alias="bigDayClaimed")
    ] = None
    r"""Whether the driver has claimed the [Big Day Exemption](https://kb.samsara.com/hc/en-us/articles/360057113891-16-Hour-Short-Haul-Exemption-Big-Day-) for this HOS day chart."""

    carrier_formatted_address: Annotated[
        Optional[str], pydantic.Field(alias="carrierFormattedAddress")
    ] = None
    r"""The address of the carrier used for this HOS chart."""

    carrier_name: Annotated[Optional[str], pydantic.Field(alias="carrierName")] = None
    r"""The name of the carrier used for this HOS chart."""

    carrier_us_dot_number: Annotated[
        Optional[int], pydantic.Field(alias="carrierUsDotNumber")
    ] = None
    r"""The US DOT number of the carrier used for this HOS chart."""

    certified_at_time: Annotated[
        Optional[str], pydantic.Field(alias="certifiedAtTime")
    ] = None
    r"""The time this log was certified in RFC 3339 format."""

    home_terminal_formatted_address: Annotated[
        Optional[str], pydantic.Field(alias="homeTerminalFormattedAddress")
    ] = None
    r"""The address of the Home Terminal used for this HOS chart."""

    home_terminal_name: Annotated[
        Optional[str], pydantic.Field(alias="homeTerminalName")
    ] = None
    r"""The name of the Home Terminal used for this HOS chart."""

    is_certified: Annotated[Optional[bool], pydantic.Field(alias="isCertified")] = None
    r"""Whether this HOS day chart was certified by the driver."""

    is_us_short_haul_active: Annotated[
        Optional[bool], pydantic.Field(alias="isUsShortHaulActive")
    ] = None
    r"""Whether the driver has the 150 air-mile Short Haul Exemption active for this HOS day chart."""

    shipping_docs: Annotated[Optional[str], pydantic.Field(alias="shippingDocs")] = None
    r"""List of shipping document names associated with the driver for the day. This field maps to Shipping ID in the dashboard."""

    trailer_names: Annotated[
        Optional[List[str]], pydantic.Field(alias="trailerNames")
    ] = None
    r"""List of trailer names associated with the driver for the day. If a trailer was associated with a log through the driver app the trailer name will be the trailer ID."""

    vehicles: Optional[List[VehicleResponseResponseBody]] = None
    r"""List of vehicles associated with the driver for the day."""
