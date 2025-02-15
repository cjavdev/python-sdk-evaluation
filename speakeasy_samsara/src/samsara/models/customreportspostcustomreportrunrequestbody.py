"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CustomReportsPostCustomReportRunRequestBodyTypedDict(TypedDict):
    r"""This creates and queues a new custom report run for the given body parameters."""

    custom_report_id: str
    r"""Required unique ID for the custom report linked to this run."""
    end_time: datetime
    r"""The end time of the custom report run in RFC 3339 format."""
    start_time: datetime
    r"""The start time of the custom report run in RFC 3339 format."""
    attribute_value_ids: NotRequired[List[str]]
    r"""The optional array of attribute value ids to filter the custom report run by."""
    tag_ids: NotRequired[List[int]]
    r"""The optional array of tag ids to filter the custom report run by."""


class CustomReportsPostCustomReportRunRequestBody(BaseModel):
    r"""This creates and queues a new custom report run for the given body parameters."""

    custom_report_id: Annotated[str, pydantic.Field(alias="customReportId")]
    r"""Required unique ID for the custom report linked to this run."""

    end_time: Annotated[datetime, pydantic.Field(alias="endTime")]
    r"""The end time of the custom report run in RFC 3339 format."""

    start_time: Annotated[datetime, pydantic.Field(alias="startTime")]
    r"""The start time of the custom report run in RFC 3339 format."""

    attribute_value_ids: Annotated[
        Optional[List[str]], pydantic.Field(alias="attributeValueIds")
    ] = None
    r"""The optional array of attribute value ids to filter the custom report run by."""

    tag_ids: Annotated[Optional[List[int]], pydantic.Field(alias="tagIds")] = None
    r"""The optional array of tag ids to filter the custom report run by."""
