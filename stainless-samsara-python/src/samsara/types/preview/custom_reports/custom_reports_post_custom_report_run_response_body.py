# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CustomReportsPostCustomReportRunResponseBody", "Data"]


class Data(BaseModel):
    id: str
    """Unique id for the custom report run object."""

    created_at_time: datetime = FieldInfo(alias="createdAtTime")
    """Time of when the custom report run was created and queued in UTC."""

    custom_report_id: str = FieldInfo(alias="customReportId")
    """Unique Id for the custom report (config) linked to this run."""


class CustomReportsPostCustomReportRunResponseBody(BaseModel):
    data: Data
    """Full post custom report run response object"""
