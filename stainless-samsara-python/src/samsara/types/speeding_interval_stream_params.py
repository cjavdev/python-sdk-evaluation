# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SpeedingIntervalStreamParams"]


class SpeedingIntervalStreamParams(TypedDict, total=False):
    asset_ids: Required[Annotated[List[str], PropertyInfo(alias="assetIds")]]
    """Comma-separated list of asset IDs. Include up to 50 asset IDs."""

    start_time: Required[Annotated[str, PropertyInfo(alias="startTime")]]
    """RFC 3339 timestamp that indicates when to begin receiving data.

    Value is compared against `updatedAtTime` or `tripStartTime` depending on the
    queryBy parameter.
    """

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    end_time: Annotated[str, PropertyInfo(alias="endTime")]
    """
    RFC 3339 timestamp which is compared against `updatedAtTime` or `tripStartTime`
    depending on the queryBy parameter. If not provided then the endpoint behaves as
    an unending feed of changes.
    """

    include_asset: Annotated[bool, PropertyInfo(alias="includeAsset")]
    """Indicates whether or not to return expanded “asset” data"""

    include_driver_id: Annotated[bool, PropertyInfo(alias="includeDriverId")]
    """Indicates whether or not to return trip's driver id"""

    query_by: Annotated[Literal["updatedAtTime", "tripStartTime"], PropertyInfo(alias="queryBy")]
    """Decide which timestamp the `startTime` and `endTime` are compared to.

    Valid values: `updatedAtTime`, `tripStartTime`
    """

    severity_levels: Annotated[List[str], PropertyInfo(alias="severityLevels")]
    """
    Optional string of comma-separated severity levels to filter speeding intervals
    by. Valid values: “light”, ”moderate”, ”heavy”, “severe”.
    """
