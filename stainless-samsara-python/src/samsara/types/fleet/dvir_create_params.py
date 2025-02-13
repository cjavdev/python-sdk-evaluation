# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DvirCreateParams"]


class DvirCreateParams(TypedDict, total=False):
    author_id: Required[Annotated[str, PropertyInfo(alias="authorId")]]
    """Samsara user ID of the mechanic creating the DVIR."""

    safety_status: Required[Annotated[Literal["safe", "unsafe"], PropertyInfo(alias="safetyStatus")]]
    """Whether or not this vehicle or trailer is safe to drive."""

    type: Required[Literal["mechanic"]]
    """Only type 'mechanic' is currently accepted."""

    license_plate: Annotated[str, PropertyInfo(alias="licensePlate")]
    """The license plate of this vehicle."""

    location: str
    """Optional string if your jurisdiction requires a location of the DVIR."""

    mechanic_notes: Annotated[str, PropertyInfo(alias="mechanicNotes")]
    """The mechanics notes on the DVIR."""

    odometer_meters: Annotated[int, PropertyInfo(alias="odometerMeters")]
    """The odometer reading in meters."""

    resolved_defect_ids: Annotated[List[str], PropertyInfo(alias="resolvedDefectIds")]
    """Array of ids for defects being resolved with this DVIR."""

    trailer_id: Annotated[str, PropertyInfo(alias="trailerId")]
    """Id of trailer being inspected. Either vehicleId or trailerId must be provided."""

    vehicle_id: Annotated[str, PropertyInfo(alias="vehicleId")]
    """Id of vehicle being inspected. Either vehicleId or trailerId must be provided."""
