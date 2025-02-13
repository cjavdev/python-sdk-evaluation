# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["IncidentStreamParams"]


class IncidentStreamParams(TypedDict, total=False):
    configuration_ids: Required[Annotated[List[str], PropertyInfo(alias="configurationIds")]]
    """Required array of alert configuration ids to return incident data for."""

    start_time: Required[Annotated[str, PropertyInfo(alias="startTime")]]
    """Required RFC 3339 timestamp that indicates when to begin receiving data.

    This will be based on updatedAtTime.
    """

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    end_time: Annotated[str, PropertyInfo(alias="endTime")]
    """Optional RFC 3339 timestamp to stop receiving data.

    Defaults to now if not provided. This will be based on updatedAtTime.
    """
