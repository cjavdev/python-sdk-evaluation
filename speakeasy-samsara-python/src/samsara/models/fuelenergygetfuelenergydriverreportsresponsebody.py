"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .fuelenergydriverreportdataobjectresponsebody import (
    FuelEnergyDriverReportDataObjectResponseBody,
    FuelEnergyDriverReportDataObjectResponseBodyTypedDict,
)
from .goapaginationresponseresponsebody import (
    GoaPaginationResponseResponseBody,
    GoaPaginationResponseResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing_extensions import TypedDict


class FuelEnergyGetFuelEnergyDriverReportsResponseBodyTypedDict(TypedDict):
    data: FuelEnergyDriverReportDataObjectResponseBodyTypedDict
    r"""Dictionary containing summarized driver report data."""
    pagination: GoaPaginationResponseResponseBodyTypedDict
    r"""Pagination parameters."""


class FuelEnergyGetFuelEnergyDriverReportsResponseBody(BaseModel):
    data: FuelEnergyDriverReportDataObjectResponseBody
    r"""Dictionary containing summarized driver report data."""

    pagination: GoaPaginationResponseResponseBody
    r"""Pagination parameters."""
