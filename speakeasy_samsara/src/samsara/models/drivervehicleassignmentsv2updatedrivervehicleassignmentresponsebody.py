"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .patchdrivervehicleassignmentsv2responsebodyresponsebody import (
    PatchDriverVehicleAssignmentsV2ResponseBodyResponseBody,
    PatchDriverVehicleAssignmentsV2ResponseBodyResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing_extensions import TypedDict


class DriverVehicleAssignmentsV2UpdateDriverVehicleAssignmentResponseBodyTypedDict(
    TypedDict
):
    data: PatchDriverVehicleAssignmentsV2ResponseBodyResponseBodyTypedDict
    r"""Response after successfully updating a Driver Assignment"""


class DriverVehicleAssignmentsV2UpdateDriverVehicleAssignmentResponseBody(BaseModel):
    data: PatchDriverVehicleAssignmentsV2ResponseBodyResponseBody
    r"""Response after successfully updating a Driver Assignment"""
