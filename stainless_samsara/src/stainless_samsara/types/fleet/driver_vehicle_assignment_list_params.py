# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DriverVehicleAssignmentListParams"]


class DriverVehicleAssignmentListParams(TypedDict, total=False):
    filter_by: Required[Annotated[Literal["drivers", "vehicles"], PropertyInfo(alias="filterBy")]]
    """Option to filter by drivers or vehicles. Valid values: `drivers`, `vehicles`"""

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    assignment_type: Annotated[
        Literal[
            "HOS", "idCard", "static", "faceId", "tachograph", "safetyManual", "RFID", "trailer", "external", "qrCode"
        ],
        PropertyInfo(alias="assignmentType"),
    ]
    """Specifies which assignment type to filter by.

    Valid values: `HOS`, `idCard`, `static`, `faceId`, `tachograph`, `safetyManual`,
    `RFID`, `trailer`, `external`, `qrCode`
    """

    driver_ids: Annotated[List[str], PropertyInfo(alias="driverIds")]
    """
    A filter on the data based on this comma-separated list of driver IDs and
    externalIds. Example: `driverIds=1234,5678,payroll:4841`
    """

    driver_tag_ids: Annotated[str, PropertyInfo(alias="driverTagIds")]
    """A filter on the data based on this comma-separated list of driver tag IDs.

    Example: `tagIds=1234,5678`
    """

    end_time: Annotated[str, PropertyInfo(alias="endTime")]
    """An end time in RFC 3339 format.

    Defaults to now if not provided. Millisecond precision and timezones are
    supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """

    start_time: Annotated[str, PropertyInfo(alias="startTime")]
    """A start time in RFC 3339 format.

    Defaults to now if not provided. Millisecond precision and timezones are
    supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """

    vehicle_ids: Annotated[List[str], PropertyInfo(alias="vehicleIds")]
    """ID of the vehicle.

    This can either be the Samsara-specified ID, or an external ID. External IDs are
    customer specified key-value pairs created in the POST or PATCH requests of this
    resource. To specify an external ID as part of a path parameter, use the
    following format: "key:value". For example, "maintenanceId:250020".
    """

    vehicle_tag_ids: Annotated[str, PropertyInfo(alias="vehicleTagIds")]
    """A filter on the data based on this comma-separated list of vehicle tag IDs.

    Example: `tagIds=1234,5678`
    """
