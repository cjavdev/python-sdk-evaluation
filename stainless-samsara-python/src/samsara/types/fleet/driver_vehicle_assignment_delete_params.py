# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DriverVehicleAssignmentDeleteParams"]


class DriverVehicleAssignmentDeleteParams(TypedDict, total=False):
    vehicle_id: Required[Annotated[str, PropertyInfo(alias="vehicleId")]]
    """ID of the vehicle.

    This can be either a unique Samsara ID or an
    [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.
    """

    assigned_at_time: Annotated[str, PropertyInfo(alias="assignedAtTime")]
    """Assigned at time in RFC 3339 format.

    Defaults to now if not provided. Millisecond precision and timezones are
    supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """

    end_time: Annotated[str, PropertyInfo(alias="endTime")]
    """An end time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    is_passenger: Annotated[bool, PropertyInfo(alias="isPassenger")]
    """Indicates if assigned driver is passenger"""

    start_time: Annotated[str, PropertyInfo(alias="startTime")]
    """A start time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """
