# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AddressListResponse",
    "Data",
    "DataGeofence",
    "DataGeofenceCircle",
    "DataGeofencePolygon",
    "DataGeofencePolygonVertex",
    "DataGeofenceSettings",
    "DataContact",
    "DataTag",
    "Pagination",
]


class DataGeofenceCircle(BaseModel):
    radius_meters: int = FieldInfo(alias="radiusMeters")
    """The radius of the circular geofence in meters."""

    latitude: Optional[float] = None
    """Latitude of the address.

    Will be geocoded from `formattedAddress` if not provided.
    """

    longitude: Optional[float] = None
    """Longitude of the address.

    Will be geocoded from `formattedAddress` if not provided.
    """


class DataGeofencePolygonVertex(BaseModel):
    latitude: float
    """The latitude of a geofence vertex in decimal degrees."""

    longitude: float
    """The longitude of a geofence vertex in decimal degrees."""


class DataGeofencePolygon(BaseModel):
    vertices: List[DataGeofencePolygonVertex]
    """The vertices of the polygon geofence.

    These geofence vertices describe the perimeter of the polygon, and must consist
    of at least 3 vertices and less than 40.
    """


class DataGeofenceSettings(BaseModel):
    show_addresses: Optional[bool] = FieldInfo(alias="showAddresses", default=None)
    """
    If this property is set to true, then underlying geofence addresses will be
    shown in reports instead of a geofence's name.
    """


class DataGeofence(BaseModel):
    circle: Optional[DataGeofenceCircle] = None
    """Information about a circular geofence.

    This field is only needed if the geofence is a circle.
    """

    polygon: Optional[DataGeofencePolygon] = None
    """Information about a polygon geofence.

    This field is only needed if the geofence is a polygon.
    """

    settings: Optional[DataGeofenceSettings] = None
    """Information about a geofence's settings."""


class DataContact(BaseModel):
    id: Optional[str] = None
    """ID of the contact."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """First name of the contact."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """Last name of the contact."""


class DataTag(BaseModel):
    id: Optional[str] = None
    """ID of the tag."""

    name: Optional[str] = None
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class Data(BaseModel):
    id: str
    """ID of the Address."""

    formatted_address: str = FieldInfo(alias="formattedAddress")
    """
    The full street address for this address/geofence, as it might be recognized by
    Google Maps.
    """

    geofence: DataGeofence
    """The geofence that defines this address and its bounds.

    This can either be a circle or a polygon, but not both.
    """

    name: str
    """Name of the address."""

    address_types: Optional[
        List[Literal["yard", "shortHaul", "workforceSite", "riskZone", "industrialSite", "alertsOnly"]]
    ] = FieldInfo(alias="addressTypes", default=None)
    """
    Reporting location type associated with the address (used for ELD reporting
    purposes). Valid values: `yard`, `shortHaul`, `workforceSite`, `riskZone`,
    `industrialSite`, `alertsOnly`.
    """

    contacts: Optional[List[DataContact]] = None
    """An array Contact mini-objects that are associated the Address."""

    created_at_time: Optional[datetime] = FieldInfo(alias="createdAtTime", default=None)
    """The date and time this address was created in RFC 3339 format."""

    external_ids: Optional[object] = FieldInfo(alias="externalIds", default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    latitude: Optional[float] = None
    """Latitude of the address.

    Will be geocoded from `formattedAddress` if not provided.
    """

    longitude: Optional[float] = None
    """Longitude of the address.

    Will be geocoded from `formattedAddress` if not provided.
    """

    notes: Optional[str] = None
    """Notes about the address."""

    tags: Optional[List[DataTag]] = None
    """
    An array of all tag mini-objects that are associated with the given address
    entry.
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


class AddressListResponse(BaseModel):
    data: List[Data]
    """A list of Addresses."""

    pagination: Pagination
    """Pagination parameters."""
