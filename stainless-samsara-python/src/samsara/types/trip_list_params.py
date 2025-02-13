# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TripListParams"]


class TripListParams(TypedDict, total=False):
    end_ms: Required[Annotated[int, PropertyInfo(alias="endMs")]]
    """End of the time range, specified in milliseconds UNIX time."""

    start_ms: Required[Annotated[int, PropertyInfo(alias="startMs")]]
    """Beginning of the time range, specified in milliseconds UNIX time.

    Limited to a 90 day window with respect to startMs and endMs
    """

    vehicle_id: Required[Annotated[int, PropertyInfo(alias="vehicleId")]]
    """Vehicle ID to query."""
