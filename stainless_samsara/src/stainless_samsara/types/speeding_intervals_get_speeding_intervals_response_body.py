# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SpeedingIntervalsGetSpeedingIntervalsResponseBody",
    "Data",
    "DataAsset",
    "DataInterval",
    "DataIntervalLocation",
    "DataIntervalLocationAddress",
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


class DataIntervalLocationAddress(BaseModel):
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


class DataIntervalLocation(BaseModel):
    address: DataIntervalLocationAddress
    """Closest address that the GPS latitude and longitude match to."""

    heading_degrees: int = FieldInfo(alias="headingDegrees")
    """Heading of the asset in degrees. May be 0 if the asset is not moving."""

    latitude: float
    """Latitude of the closest location point to the interval."""

    longitude: float
    """Longitude of the closest location point to the interval."""

    accuracy_meters: Optional[float] = FieldInfo(alias="accuracyMeters", default=None)
    """Radial accuracy of gps location in meters.

    This will only return if strong GPS is not available.
    """


class DataInterval(BaseModel):
    end_time: str = FieldInfo(alias="endTime")
    """UTC time the interval ended in RFC 3339 format."""

    is_dismissed: bool = FieldInfo(alias="isDismissed")
    """Whether the interval is dismissed."""

    location: DataIntervalLocation
    """Location object of the closest location point to the interval."""

    max_speed_kilometers_per_hour: float = FieldInfo(alias="maxSpeedKilometersPerHour")
    """The max speed exceeded for the speeding interval."""

    posted_speed_limit_kilometers_per_hour: float = FieldInfo(alias="postedSpeedLimitKilometersPerHour")
    """The posted speed limit associated with the speeding interval."""

    severity_level: Literal["light", "moderate", "heavy", "severe"] = FieldInfo(alias="severityLevel")
    """Specifies the severity level of the speeding interval.

    Valid values: `light`, `moderate`, `heavy`, `severe`
    """

    start_time: str = FieldInfo(alias="startTime")
    """UTC time the interval started in RFC 3339 format."""


class Data(BaseModel):
    asset: DataAsset
    """Asset that the location readings are tied to"""

    created_at_time: str = FieldInfo(alias="createdAtTime")
    """UTC time the trip was created in Samsara in RFC 3339 format."""

    intervals: List[DataInterval]
    """List of speeding intervals that belong to the trip.

    The full list of intervals associated with the trip is always returned, empty if
    no intervals exist.
    """

    trip_start_time: str = FieldInfo(alias="tripStartTime")
    """UTC time the trip started in RFC 3339 format."""

    updated_at_time: str = FieldInfo(alias="updatedAtTime")
    """UTC time the trip was last updated in Samsara in RFC 3339 format.

    Valid updates are when trip's endTime populates or interval.isDismissed changes
    value.
    """

    driver_id: Optional[str] = FieldInfo(alias="driverId", default=None)
    """The driver ID assigned to the trip.

    Only returned if includeDriverId is set to true. 'null' if no driver id.
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


class SpeedingIntervalsGetSpeedingIntervalsResponseBody(BaseModel):
    data: List[Data]
    """List of speeding intervals associated with trips."""

    pagination: Pagination
    """Pagination parameters."""
