# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RunCreateParams"]


class RunCreateParams(TypedDict, total=False):
    custom_report_id: Required[Annotated[str, PropertyInfo(alias="customReportId")]]
    """Required unique ID for the custom report linked to this run."""

    end_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="endTime", format="iso8601")]]
    """The end time of the custom report run in RFC 3339 format."""

    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="startTime", format="iso8601")]]
    """The start time of the custom report run in RFC 3339 format."""

    attribute_value_ids: Annotated[List[str], PropertyInfo(alias="attributeValueIds")]
    """The optional array of attribute value ids to filter the custom report run by."""

    tag_ids: Annotated[Iterable[int], PropertyInfo(alias="tagIds")]
    """The optional array of tag ids to filter the custom report run by."""
