"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class VehicleStatsFaultCodesVendorSpecificFieldsTypedDict(TypedDict):
    r"""Vendor specific data for J1939 vehicles."""

    dtc_description: NotRequired[str]
    r"""The DTC description, if available."""
    repair_instructions_url: NotRequired[str]
    r"""A link to vendor repair instructions, if available."""


class VehicleStatsFaultCodesVendorSpecificFields(BaseModel):
    r"""Vendor specific data for J1939 vehicles."""

    dtc_description: Annotated[
        Optional[str], pydantic.Field(alias="dtcDescription")
    ] = None
    r"""The DTC description, if available."""

    repair_instructions_url: Annotated[
        Optional[str], pydantic.Field(alias="repairInstructionsUrl")
    ] = None
    r"""A link to vendor repair instructions, if available."""
