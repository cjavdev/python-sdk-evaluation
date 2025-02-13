# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "AddressModifyParams",
    "Geofence",
    "GeofenceCircle",
    "GeofencePolygon",
    "GeofencePolygonVertex",
    "GeofenceSettings",
]


class AddressModifyParams(TypedDict, total=False):
    address_types: Annotated[
        List[Literal["yard", "shortHaul", "workforceSite", "riskZone", "industrialSite", "alertsOnly"]],
        PropertyInfo(alias="addressTypes"),
    ]
    """
    Reporting location type associated with the address (used for ELD reporting
    purposes). Valid values: `yard`, `shortHaul`, `workforceSite`, `riskZone`,
    `industrialSite`, `alertsOnly`.
    """

    contact_ids: Annotated[List[str], PropertyInfo(alias="contactIds")]
    """An array of Contact IDs associated with this Address."""

    external_ids: Annotated[Dict[str, str], PropertyInfo(alias="externalIds")]
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    formatted_address: Annotated[str, PropertyInfo(alias="formattedAddress")]
    """
    The full street address for this address/geofence, as it might be recognized by
    Google Maps.
    """

    geofence: Geofence
    """The geofence that defines this address and its bounds.

    This can either be a circle or a polygon, but not both.
    """

    latitude: float
    """Latitude of the address.

    Will be geocoded from `formattedAddress` if not provided.
    """

    longitude: float
    """Longitude of the address.

    Will be geocoded from `formattedAddress` if not provided.
    """

    name: str
    """Name of the address."""

    notes: str
    """Notes about the address."""

    tag_ids: Annotated[List[str], PropertyInfo(alias="tagIds")]
    """An array of IDs of tags to associate with this address."""


class GeofenceCircle(TypedDict, total=False):
    radius_meters: Required[Annotated[int, PropertyInfo(alias="radiusMeters")]]
    """The radius of the circular geofence in meters."""

    latitude: float
    """Latitude of the address.

    Will be geocoded from `formattedAddress` if not provided.
    """

    longitude: float
    """Longitude of the address.

    Will be geocoded from `formattedAddress` if not provided.
    """


class GeofencePolygonVertex(TypedDict, total=False):
    latitude: Required[float]
    """The latitude of a geofence vertex in decimal degrees."""

    longitude: Required[float]
    """The longitude of a geofence vertex in decimal degrees."""


class GeofencePolygon(TypedDict, total=False):
    vertices: Required[Iterable[GeofencePolygonVertex]]
    """The vertices of the polygon geofence.

    These geofence vertices describe the perimeter of the polygon, and must consist
    of at least 3 vertices and less than 40.
    """


class GeofenceSettings(TypedDict, total=False):
    show_addresses: Annotated[bool, PropertyInfo(alias="showAddresses")]
    """
    If this property is set to true, then underlying geofence addresses will be
    shown in reports instead of a geofence's name.
    """


class Geofence(TypedDict, total=False):
    circle: GeofenceCircle
    """Information about a circular geofence.

    This field is only needed if the geofence is a circle.
    """

    polygon: GeofencePolygon
    """Information about a polygon geofence.

    This field is only needed if the geofence is a polygon.
    """

    settings: GeofenceSettings
    """Information about a geofence's settings."""
