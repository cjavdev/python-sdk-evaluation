"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class PostCustomReportRunResponseObjectResponseBodyTypedDict(TypedDict):
    r"""Full post custom report run response object"""

    created_at_time: datetime
    r"""Time of when the custom report run was created and queued in UTC."""
    custom_report_id: str
    r"""Unique Id for the custom report (config) linked to this run."""
    id: str
    r"""Unique id for the custom report run object."""


class PostCustomReportRunResponseObjectResponseBody(BaseModel):
    r"""Full post custom report run response object"""

    created_at_time: Annotated[datetime, pydantic.Field(alias="createdAtTime")]
    r"""Time of when the custom report run was created and queued in UTC."""

    custom_report_id: Annotated[str, pydantic.Field(alias="customReportId")]
    r"""Unique Id for the custom report (config) linked to this run."""

    id: str
    r"""Unique id for the custom report run object."""
