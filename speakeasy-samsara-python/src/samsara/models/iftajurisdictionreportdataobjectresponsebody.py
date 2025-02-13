"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .iftajurisdictionsummaryobjectresponsebody import (
    IftaJurisdictionSummaryObjectResponseBody,
    IftaJurisdictionSummaryObjectResponseBodyTypedDict,
)
from .iftareporttroubleshootingobjectresponsebody import (
    IftaReportTroubleshootingObjectResponseBody,
    IftaReportTroubleshootingObjectResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class IftaJurisdictionReportDataObjectResponseBodyTypedDict(TypedDict):
    r"""Dictionary containing summarized jurisdiction report data."""

    jurisdiction_reports: List[IftaJurisdictionSummaryObjectResponseBodyTypedDict]
    r"""List of summarized jurisdiction reports."""
    year: int
    r"""The specified year for this IFTA report."""
    month: NotRequired[str]
    r"""The specified month duration for this IFTA report."""
    quarter: NotRequired[str]
    r"""The specified quarter duration for this IFTA report."""
    troubleshooting: NotRequired[IftaReportTroubleshootingObjectResponseBodyTypedDict]
    r"""IFTA report troubleshooting information."""


class IftaJurisdictionReportDataObjectResponseBody(BaseModel):
    r"""Dictionary containing summarized jurisdiction report data."""

    jurisdiction_reports: Annotated[
        List[IftaJurisdictionSummaryObjectResponseBody],
        pydantic.Field(alias="jurisdictionReports"),
    ]
    r"""List of summarized jurisdiction reports."""

    year: int
    r"""The specified year for this IFTA report."""

    month: Optional[str] = None
    r"""The specified month duration for this IFTA report."""

    quarter: Optional[str] = None
    r"""The specified quarter duration for this IFTA report."""

    troubleshooting: Optional[IftaReportTroubleshootingObjectResponseBody] = None
    r"""IFTA report troubleshooting information."""
