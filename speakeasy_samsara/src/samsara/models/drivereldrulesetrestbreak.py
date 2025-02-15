"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class DriverEldRulesetRestBreak(str, Enum):
    r"""The rest break required setting of the ELD ruleset applied to this driver. Valid values: `Property (off-duty/sleeper)`, `Explosives/HazMat (on-duty)`"""

    PROPERTY_OFF_DUTY_SLEEPER_ = "Property (off-duty/sleeper)"
    EXPLOSIVES_HAZ_MAT_ON_DUTY_ = "Explosives/HazMat (on-duty)"
