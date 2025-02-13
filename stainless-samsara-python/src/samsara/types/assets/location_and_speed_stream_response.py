# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "LocationAndSpeedStreamResponse",
    "Data",
    "DataAsset",
    "DataLocation",
    "DataLocationAddress",
    "DataLocationGeofence",
    "DataSpeed",
    "Pagination",
]


class DataAsset(BaseModel):
    id: str
    """ID of the asset"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class DataLocationAddress(BaseModel):
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


class DataLocationGeofence(BaseModel):
    id: Optional[str] = None
    """Unique ID of the geofence object."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class DataLocation(BaseModel):
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

    address: Optional[DataLocationAddress] = None
    """Closest address that the GPS latitude and longitude match to."""

    geofence: Optional[DataLocationGeofence] = None
    """Closest geofence based on 1000 meter radial search."""


class DataSpeed(BaseModel):
    ecu_speed_meters_per_second: Optional[float] = FieldInfo(alias="ecuSpeedMetersPerSecond", default=None)
    """Speed of asset based on ECU data."""

    gps_speed_meters_per_second: Optional[float] = FieldInfo(alias="gpsSpeedMetersPerSecond", default=None)
    """Speed of asset based on GPS data."""


class Data(BaseModel):
    asset: DataAsset
    """Asset that the location readings are tied to."""

    happened_at_time: str = FieldInfo(alias="happenedAtTime")
    """UTC timestamp in RFC 3339 format of the event."""

    location: DataLocation
    """Location object."""

    speed: Optional[DataSpeed] = None
    """Speed object."""


class Pagination(BaseModel):
    has_next_page: bool = FieldInfo(alias="hasNextPage")
    """
    True if there are more pages of results immediately available after this
    endCursor.
    """

    end_cursor: Optional[str] = FieldInfo(alias="endCursor", default=None)
    """Cursor identifier representing the last element in the response.

    This value should be used in conjunction with a subsequent request's 'after'
    query parameter. This may be an empty string if there are no more pages left to
    view.
    """


class LocationAndSpeedStreamResponse(BaseModel):
    data: List[Data]
    """List of location and speed objects."""

    pagination: Pagination
    """Pagination parameters."""
