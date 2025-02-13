# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DriverVehicleAssignmentCreateParams", "Metadata"]


class DriverVehicleAssignmentCreateParams(TypedDict, total=False):
    driver_id: Required[Annotated[str, PropertyInfo(alias="driverId")]]
    """ID of the driver.

    This can be either a unique Samsara ID or an
    [external ID](https://developers.samsara.com/docs/external-ids) for the driver.
    """

    vehicle_id: Required[Annotated[str, PropertyInfo(alias="vehicleId")]]
    """ID of the vehicle.

    This can be either a unique Samsara ID or an
    [external ID](https://developers.samsara.com/docs/external-ids) for the vehicle.
    """

    assigned_at_time: Annotated[str, PropertyInfo(alias="assignedAtTime")]
    """The time at which the assignment was made in RFC 3339 format.

    Defaults to now if not provided. Millisecond precision and timezones are
    supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """

    end_time: Annotated[str, PropertyInfo(alias="endTime")]
    """The end time in RFC 3339 format.

    Defaults to max-time (meaning it's an ongoing assignment) if not provided.
    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    is_passenger: Annotated[bool, PropertyInfo(alias="isPassenger")]
    """Is this driver a passenger? Defaults to false if not provided"""

    metadata: Metadata
    """Metadata about this driver assignment"""

    start_time: Annotated[str, PropertyInfo(alias="startTime")]
    """The start time in RFC 3339 format.

    Defaults to now if not provided. Millisecond precision and timezones are
    supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """


class Metadata(TypedDict, total=False):
    source_name: Annotated[str, PropertyInfo(alias="sourceName")]
    """Describes where the external assignment is coming from"""
