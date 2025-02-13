# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "TripsGetTripsResponseBody",
    "Data",
    "DataAsset",
    "DataStartLocation",
    "DataStartLocationAddress",
    "DataStartLocationGeofence",
    "DataEndLocation",
    "DataEndLocationAddress",
    "DataEndLocationGeofence",
    "Pagination",
]


class DataAsset(BaseModel):
    id: str
    """Unique ID for the asset object that is reporting the location."""

    name: Optional[str] = None
    """Name for the asset object that is reporting the location.

    Only returns when `includeAsset` is set to `true`.
    """

    type: Optional[Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"]] = None
    """Type for the asset object that is reporting the location.

    Only returns when `includeAsset` is set to `true`. Valid values:
    `uncategorized`, `trailer`, `equipment`, `unpowered`, `vehicle`
    """

    vin: Optional[str] = None
    """VIN for the asset object that is reporting the location.

    Only returns when `includeAsset` is set to `true`.
    """


class DataStartLocationAddress(BaseModel):
    city: Optional[str] = None
    """The name of the city"""

    country: Optional[str] = None
    """The country"""

    neighborhood: Optional[str] = None
    """The name of the neighborhood if one exists"""

    point_of_interest: Optional[str] = FieldInfo(alias="pointOfInterest", default=None)
    """Point that may be of interest to the user"""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The zip code"""

    state: Optional[str] = None
    """The name of the state"""

    street: Optional[str] = None
    """The street name"""

    street_number: Optional[str] = FieldInfo(alias="streetNumber", default=None)
    """Street number of the address"""


class DataStartLocationGeofence(BaseModel):
    id: Optional[str] = None
    """Unique ID of the geofence object."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class DataStartLocation(BaseModel):
    heading_degrees: int = FieldInfo(alias="headingDegrees")
    """Heading of the asset in degrees. May be 0 if the asset is not moving."""

    latitude: float
    """Latitude of the location of the asset."""

    longitude: float
    """Longitude of the location of the asset."""

    accuracy_meters: Optional[float] = FieldInfo(alias="accuracyMeters", default=None)
    """Radial accuracy of gps location in meters.

    This will only return if strong GPS is not available.
    """

    address: Optional[DataStartLocationAddress] = None
    """Closest address that the GPS latitude and longitude match to."""

    geofence: Optional[DataStartLocationGeofence] = None
    """Closest geofence based on 1000 meter radial search."""


class DataEndLocationAddress(BaseModel):
    city: Optional[str] = None
    """The name of the city"""

    country: Optional[str] = None
    """The country"""

    neighborhood: Optional[str] = None
    """The name of the neighborhood if one exists"""

    point_of_interest: Optional[str] = FieldInfo(alias="pointOfInterest", default=None)
    """Point that may be of interest to the user"""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """The zip code"""

    state: Optional[str] = None
    """The name of the state"""

    street: Optional[str] = None
    """The street name"""

    street_number: Optional[str] = FieldInfo(alias="streetNumber", default=None)
    """Street number of the address"""


class DataEndLocationGeofence(BaseModel):
    id: Optional[str] = None
    """Unique ID of the geofence object."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class DataEndLocation(BaseModel):
    heading_degrees: int = FieldInfo(alias="headingDegrees")
    """Heading of the asset in degrees. May be 0 if the asset is not moving."""

    latitude: float
    """Latitude of the location of the asset."""

    longitude: float
    """Longitude of the location of the asset."""

    accuracy_meters: Optional[float] = FieldInfo(alias="accuracyMeters", default=None)
    """Radial accuracy of gps location in meters.

    This will only return if strong GPS is not available.
    """

    address: Optional[DataEndLocationAddress] = None
    """Closest address that the GPS latitude and longitude match to."""

    geofence: Optional[DataEndLocationGeofence] = None
    """Closest geofence based on 1000 meter radial search."""


class Data(BaseModel):
    asset: DataAsset
    """Asset that the location readings are tied to"""

    completion_status: Literal["inProgress", "completed"] = FieldInfo(alias="completionStatus")
    """Trip completion status Valid values: `inProgress`, `completed`"""

    created_at_time: str = FieldInfo(alias="createdAtTime")
    """[RFC 3339] Time the trip was created in Samsara in UTC."""

    start_location: DataStartLocation = FieldInfo(alias="startLocation")
    """Location object."""

    trip_start_time: str = FieldInfo(alias="tripStartTime")
    """[RFC 3339] Time the trip started in UTC."""

    updated_at_time: str = FieldInfo(alias="updatedAtTime")
    """[RFC 3339] Time the trip was updated in Samsara in UTC.

    Valid updates are when `endTime` populates or `completionStatus` changes values.
    """

    end_location: Optional[DataEndLocation] = FieldInfo(alias="endLocation", default=None)
    """Location object."""

    trip_end_time: Optional[str] = FieldInfo(alias="tripEndTime", default=None)
    """[RFC 3339] Time the trip ended in UTC."""


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


class TripsGetTripsResponseBody(BaseModel):
    data: List[Data]
    """List of trips"""

    pagination: Pagination
    """Pagination parameters."""
