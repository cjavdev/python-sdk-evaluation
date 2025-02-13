# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HosDailyLogsUpdateShippingDocsResponseBody", "Data"]


class Data(BaseModel):
    adverse_driving_claimed: Optional[bool] = FieldInfo(alias="adverseDrivingClaimed", default=None)
    """
    Whether the driver has claimed the
    [Adverse Driving Exemption](https://kb.samsara.com/hc/en-us/articles/360047336792-Adverse-Driving-Exemption)
    for this HOS day chart.
    """

    big_day_claimed: Optional[bool] = FieldInfo(alias="bigDayClaimed", default=None)
    """
    Whether the driver has claimed the
    [Big Day Exemption](https://kb.samsara.com/hc/en-us/articles/360057113891-16-Hour-Short-Haul-Exemption-Big-Day-)
    for this HOS day chart.
    """

    carrier_formatted_address: Optional[str] = FieldInfo(alias="carrierFormattedAddress", default=None)
    """The address of the carrier used for this HOS chart."""

    carrier_name: Optional[str] = FieldInfo(alias="carrierName", default=None)
    """The name of the carrier used for this HOS chart."""

    carrier_us_dot_number: Optional[int] = FieldInfo(alias="carrierUsDotNumber", default=None)
    """The US DOT number of the carrier used for this HOS chart."""

    home_terminal_formatted_address: Optional[str] = FieldInfo(alias="homeTerminalFormattedAddress", default=None)
    """The address of the Home Terminal used for this HOS chart."""

    home_terminal_name: Optional[str] = FieldInfo(alias="homeTerminalName", default=None)
    """The name of the Home Terminal used for this HOS chart."""

    is_certified: Optional[bool] = FieldInfo(alias="isCertified", default=None)
    """Whether this HOS day chart was certified by the driver."""

    is_us_short_haul_active: Optional[bool] = FieldInfo(alias="isUsShortHaulActive", default=None)
    """
    Whether the driver has the 150 air-mile Short Haul Exemption active for this HOS
    day chart.
    """

    trailer_names: Optional[List[str]] = FieldInfo(alias="trailerNames", default=None)
    """List of trailer names associated with the driver for the day.

    If a trailer was associated with a log through the driver app, the trailer name
    will be the trailer ID.
    """


class HosDailyLogsUpdateShippingDocsResponseBody(BaseModel):
    data: Data
    """Response after successfully updating the LogMetaData object."""
