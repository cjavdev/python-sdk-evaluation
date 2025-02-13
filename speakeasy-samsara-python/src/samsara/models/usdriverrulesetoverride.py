"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class Cycle(str, Enum):
    r"""The driver's working cycle. Valid values: `USA Property (8/70)`, `USA Property (7/60)`, `USA Passenger (8/70)`, `USA Passenger (7/60)`, `Alaska Property (8/80)`, `Alaska Property (7/70)`, `Alaska Passenger (8/80)`, `Alaska Passenger (7/70)`, `California School/FLV (8/80)`, `California Farm (8/112)`, `California Property (8/80)`, `California Flammable Liquid (8/80)`, `California Passenger (8/80)`, `California Motion Picture (8/80)`, `Florida (8/80)`, `Florida (7/70)`, `Nebraska (8/80)`, `Nebraska (7/70)`, `North Carolina (8/80)`, `North Carolina (7/70)`, `Oklahoma (8/70)`, `Oklahoma (7/60)`, `Oregon (8/80)`, `Oregon (7/70)`, `South Carolina (8/80)`, `South Carolina (7/70)`, `Texas (7/70)`, `Wisconsin (8/80)`, `Wisconsin (7/70)`"""

    USA_PROPERTY_8_70_ = "USA Property (8/70)"
    USA_PROPERTY_7_60_ = "USA Property (7/60)"
    USA_PASSENGER_8_70_ = "USA Passenger (8/70)"
    USA_PASSENGER_7_60_ = "USA Passenger (7/60)"
    ALASKA_PROPERTY_8_80_ = "Alaska Property (8/80)"
    ALASKA_PROPERTY_7_70_ = "Alaska Property (7/70)"
    ALASKA_PASSENGER_8_80_ = "Alaska Passenger (8/80)"
    ALASKA_PASSENGER_7_70_ = "Alaska Passenger (7/70)"
    CALIFORNIA_SCHOOL_FLV_8_80_ = "California School/FLV (8/80)"
    CALIFORNIA_FARM_8_112_ = "California Farm (8/112)"
    CALIFORNIA_PROPERTY_8_80_ = "California Property (8/80)"
    CALIFORNIA_FLAMMABLE_LIQUID_8_80_ = "California Flammable Liquid (8/80)"
    CALIFORNIA_PASSENGER_8_80_ = "California Passenger (8/80)"
    CALIFORNIA_MOTION_PICTURE_8_80_ = "California Motion Picture (8/80)"
    FLORIDA_8_80_ = "Florida (8/80)"
    FLORIDA_7_70_ = "Florida (7/70)"
    NEBRASKA_8_80_ = "Nebraska (8/80)"
    NEBRASKA_7_70_ = "Nebraska (7/70)"
    NORTH_CAROLINA_8_80_ = "North Carolina (8/80)"
    NORTH_CAROLINA_7_70_ = "North Carolina (7/70)"
    OKLAHOMA_8_70_ = "Oklahoma (8/70)"
    OKLAHOMA_7_60_ = "Oklahoma (7/60)"
    OREGON_8_80_ = "Oregon (8/80)"
    OREGON_7_70_ = "Oregon (7/70)"
    SOUTH_CAROLINA_8_80_ = "South Carolina (8/80)"
    SOUTH_CAROLINA_7_70_ = "South Carolina (7/70)"
    TEXAS_7_70_ = "Texas (7/70)"
    WISCONSIN_8_80_ = "Wisconsin (8/80)"
    WISCONSIN_7_70_ = "Wisconsin (7/70)"


class Restart(str, Enum):
    r"""Amount of time necessary for the driver to be resting in order to restart their cycle. Valid values: `34-hour Restart`, `24-hour Restart`, `36-hour Restart`, `72-hour Restart`, `None`."""

    THIRTY_FOUR_HOUR_RESTART = "34-hour Restart"
    TWENTY_FOUR_HOUR_RESTART = "24-hour Restart"
    THIRTY_SIX_HOUR_RESTART = "36-hour Restart"
    SEVENTY_TWO_HOUR_RESTART = "72-hour Restart"
    NONE = "None"


class Restbreak(str, Enum):
    r"""The restbreak required for this driver. Valid values: `Property (off-duty/sleeper)`, `California Mealbreak (off-duty/sleeper)`, `None`."""

    PROPERTY_OFF_DUTY_SLEEPER_ = "Property (off-duty/sleeper)"
    CALIFORNIA_MEALBREAK_OFF_DUTY_SLEEPER_ = "California Mealbreak (off-duty/sleeper)"
    NONE = "None"


class UsStateToOverride(str, Enum):
    r"""The jurisdiction of the ruleset applied to this driver. These are specified by either the ISO 3166-2 postal code for the supported US states, or empty string '' for US Federal Ruleset jurisdiction. Valid values: ``, `AK`, `CA`, `FL`, `NE`, `NC`, `OK`, `OR`, `SC`, `TX`, `WI`."""

    UNKNOWN = ""
    AK = "AK"
    CA = "CA"
    FL = "FL"
    NE = "NE"
    NC = "NC"
    OK = "OK"
    OR = "OR"
    SC = "SC"
    TX = "TX"
    WI = "WI"


class UsDriverRulesetOverrideTypedDict(TypedDict):
    r"""US Driver Ruleset override for a given driver. If the driver is operating under a ruleset different from the organization default, the override is used. Updating this value only updates the override setting for this driver. Explicitly setting this field to `null` will delete driver's ruleset override. If the driver does not have an override ruleset set, the response will not include any usDriverRulesetOverride information."""

    cycle: Cycle
    r"""The driver's working cycle. Valid values: `USA Property (8/70)`, `USA Property (7/60)`, `USA Passenger (8/70)`, `USA Passenger (7/60)`, `Alaska Property (8/80)`, `Alaska Property (7/70)`, `Alaska Passenger (8/80)`, `Alaska Passenger (7/70)`, `California School/FLV (8/80)`, `California Farm (8/112)`, `California Property (8/80)`, `California Flammable Liquid (8/80)`, `California Passenger (8/80)`, `California Motion Picture (8/80)`, `Florida (8/80)`, `Florida (7/70)`, `Nebraska (8/80)`, `Nebraska (7/70)`, `North Carolina (8/80)`, `North Carolina (7/70)`, `Oklahoma (8/70)`, `Oklahoma (7/60)`, `Oregon (8/80)`, `Oregon (7/70)`, `South Carolina (8/80)`, `South Carolina (7/70)`, `Texas (7/70)`, `Wisconsin (8/80)`, `Wisconsin (7/70)`"""
    restart: Restart
    r"""Amount of time necessary for the driver to be resting in order to restart their cycle. Valid values: `34-hour Restart`, `24-hour Restart`, `36-hour Restart`, `72-hour Restart`, `None`."""
    restbreak: Restbreak
    r"""The restbreak required for this driver. Valid values: `Property (off-duty/sleeper)`, `California Mealbreak (off-duty/sleeper)`, `None`."""
    us_state_to_override: UsStateToOverride
    r"""The jurisdiction of the ruleset applied to this driver. These are specified by either the ISO 3166-2 postal code for the supported US states, or empty string '' for US Federal Ruleset jurisdiction. Valid values: ``, `AK`, `CA`, `FL`, `NE`, `NC`, `OK`, `OR`, `SC`, `TX`, `WI`."""


class UsDriverRulesetOverride(BaseModel):
    r"""US Driver Ruleset override for a given driver. If the driver is operating under a ruleset different from the organization default, the override is used. Updating this value only updates the override setting for this driver. Explicitly setting this field to `null` will delete driver's ruleset override. If the driver does not have an override ruleset set, the response will not include any usDriverRulesetOverride information."""

    cycle: Cycle
    r"""The driver's working cycle. Valid values: `USA Property (8/70)`, `USA Property (7/60)`, `USA Passenger (8/70)`, `USA Passenger (7/60)`, `Alaska Property (8/80)`, `Alaska Property (7/70)`, `Alaska Passenger (8/80)`, `Alaska Passenger (7/70)`, `California School/FLV (8/80)`, `California Farm (8/112)`, `California Property (8/80)`, `California Flammable Liquid (8/80)`, `California Passenger (8/80)`, `California Motion Picture (8/80)`, `Florida (8/80)`, `Florida (7/70)`, `Nebraska (8/80)`, `Nebraska (7/70)`, `North Carolina (8/80)`, `North Carolina (7/70)`, `Oklahoma (8/70)`, `Oklahoma (7/60)`, `Oregon (8/80)`, `Oregon (7/70)`, `South Carolina (8/80)`, `South Carolina (7/70)`, `Texas (7/70)`, `Wisconsin (8/80)`, `Wisconsin (7/70)`"""

    restart: Restart
    r"""Amount of time necessary for the driver to be resting in order to restart their cycle. Valid values: `34-hour Restart`, `24-hour Restart`, `36-hour Restart`, `72-hour Restart`, `None`."""

    restbreak: Restbreak
    r"""The restbreak required for this driver. Valid values: `Property (off-duty/sleeper)`, `California Mealbreak (off-duty/sleeper)`, `None`."""

    us_state_to_override: Annotated[
        UsStateToOverride, pydantic.Field(alias="usStateToOverride")
    ]
    r"""The jurisdiction of the ruleset applied to this driver. These are specified by either the ISO 3166-2 postal code for the supported US states, or empty string '' for US Federal Ruleset jurisdiction. Valid values: ``, `AK`, `CA`, `FL`, `NE`, `NC`, `OK`, `OR`, `SC`, `TX`, `WI`."""
