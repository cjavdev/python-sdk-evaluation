"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class DriverEldRulesetShift(str, Enum):
    r"""The shift of the ELD ruleset applied to this driver. Valid values: `US Interstate Property`, `US Interstate Passenger`, `Texas Intrastate`."""

    US_INTERSTATE_PROPERTY = "US Interstate Property"
    US_INTERSTATE_PASSENGER = "US Interstate Passenger"
    TEXAS_INTRASTATE = "Texas Intrastate"
