# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["VehicleIdlingListResponse", "Data", "DataAddress", "DataVehicle", "Pagination"]


class DataAddress(BaseModel):
    formatted: str
    """The formatted address of the idling location."""

    latitude: float
    """The latitude of the idling location."""

    longitude: float
    """The longitude of the idling location."""


class DataVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the vehicle"""


class Data(BaseModel):
    address: DataAddress
    """Address where the idling event took place."""

    duration_ms: int = FieldInfo(alias="durationMs")
    """The duration of this idling event in milliseconds."""

    end_time: str = FieldInfo(alias="endTime")
    """The end time of this idling event in RFC 3339 format."""

    fuel_consumption_ml: float = FieldInfo(alias="fuelConsumptionMl")
    """The amount of fuel consumed in milliliters during this idling event."""

    is_pto_active: bool = FieldInfo(alias="isPtoActive")
    """Whether or not power take-off was active during this idling event."""

    start_time: str = FieldInfo(alias="startTime")
    """The start time of this idling event in RFC 3339 format."""

    vehicle: DataVehicle
    """A minified vehicle object.

    This object is only returned if the route is assigned to the vehicle.
    """


class Pagination(BaseModel):
    end_cursor: str = FieldInfo(alias="endCursor")
    """Cursor identifier representing the last element in the response.

    This value should be used in conjunction with a subsequent request's 'after'
    query parameter. This may be an empty string if there are no more pages left to
    view.
    """

    has_next_page: bool = FieldInfo(alias="hasNextPage")
    """
    True if there are more pages of results immediately available after this
    endCursor.
    """


class VehicleIdlingListResponse(BaseModel):
    data: List[Data]
    """Multiple idling events."""

    pagination: Pagination
    """Pagination parameters."""

    request_end_time: str = FieldInfo(alias="requestEndTime")
    """The requested end time in RFC 3339 format."""

    request_start_time: str = FieldInfo(alias="requestStartTime")
    """The requested start time in RFC 3339 format."""
