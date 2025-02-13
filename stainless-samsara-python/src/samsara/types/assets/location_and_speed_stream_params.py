# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LocationAndSpeedStreamParams"]


class LocationAndSpeedStreamParams(TypedDict, total=False):
    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    end_time: Annotated[str, PropertyInfo(alias="endTime")]
    """An end time in RFC 3339 format.

    Defaults to never if not provided; if not provided then pagination will not
    cease, and a valid pagination cursor will always be returned. Millisecond
    precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z,
    2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    ids: List[str]
    """Comma-separated list of asset IDs."""

    include_external_ids: Annotated[bool, PropertyInfo(alias="includeExternalIds")]
    """
    Optional boolean indicating whether to return external IDs on supported entities
    """

    include_geofence_lookup: Annotated[bool, PropertyInfo(alias="includeGeofenceLookup")]
    """Optional boolean indicating whether or not to return the 'geofence' object"""

    include_reverse_geo: Annotated[bool, PropertyInfo(alias="includeReverseGeo")]
    """Optional boolean indicating whether or not to return the 'address' object"""

    include_speed: Annotated[bool, PropertyInfo(alias="includeSpeed")]
    """Optional boolean indicating whether or not to return the 'speed' object"""

    limit: int
    """The limit for how many objects will be in the response.

    Default and max for this value is 512 objects.
    """

    start_time: Annotated[str, PropertyInfo(alias="startTime")]
    """A start time in RFC 3339 format.

    Defaults to now if not provided. Millisecond precision and timezones are
    supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """
