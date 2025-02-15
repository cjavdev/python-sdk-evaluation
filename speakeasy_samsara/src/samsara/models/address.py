"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .addressgeofence import AddressGeofence, AddressGeofenceTypedDict
from .contacttinyresponse import ContactTinyResponse, ContactTinyResponseTypedDict
from .tagtinyresponse import TagTinyResponse, TagTinyResponseTypedDict
from datetime import datetime
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AddressTypes(str, Enum):
    YARD = "yard"
    SHORT_HAUL = "shortHaul"
    WORKFORCE_SITE = "workforceSite"
    RISK_ZONE = "riskZone"
    INDUSTRIAL_SITE = "industrialSite"
    ALERTS_ONLY = "alertsOnly"


class ExternalIdsTypedDict(TypedDict):
    r"""The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object."""


class ExternalIds(BaseModel):
    r"""The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object."""


class AddressTypedDict(TypedDict):
    r"""An Address object."""

    formatted_address: str
    r"""The full street address for this address/geofence, as it might be recognized by Google Maps."""
    geofence: AddressGeofenceTypedDict
    r"""The geofence that defines this address and its bounds. This can either be a circle or a polygon, but not both."""
    id: str
    r"""ID of the Address."""
    name: str
    r"""Name of the address."""
    address_types: NotRequired[List[AddressTypes]]
    r"""Reporting location type associated with the address (used for ELD reporting purposes). Valid values: `yard`, `shortHaul`, `workforceSite`, `riskZone`, `industrialSite`, `alertsOnly`."""
    contacts: NotRequired[List[ContactTinyResponseTypedDict]]
    r"""An array Contact mini-objects that are associated the Address."""
    created_at_time: NotRequired[datetime]
    r"""The date and time this address was created in RFC 3339 format."""
    external_ids: NotRequired[ExternalIdsTypedDict]
    r"""The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object."""
    latitude: NotRequired[float]
    r"""Latitude of the address. Will be geocoded from `formattedAddress` if not provided."""
    longitude: NotRequired[float]
    r"""Longitude of the address. Will be geocoded from `formattedAddress` if not provided."""
    notes: NotRequired[str]
    r"""Notes about the address."""
    tags: NotRequired[List[TagTinyResponseTypedDict]]
    r"""An array of all tag mini-objects that are associated with the given address entry."""


class Address(BaseModel):
    r"""An Address object."""

    formatted_address: Annotated[str, pydantic.Field(alias="formattedAddress")]
    r"""The full street address for this address/geofence, as it might be recognized by Google Maps."""

    geofence: AddressGeofence
    r"""The geofence that defines this address and its bounds. This can either be a circle or a polygon, but not both."""

    id: str
    r"""ID of the Address."""

    name: str
    r"""Name of the address."""

    address_types: Annotated[
        Optional[List[AddressTypes]], pydantic.Field(alias="addressTypes")
    ] = None
    r"""Reporting location type associated with the address (used for ELD reporting purposes). Valid values: `yard`, `shortHaul`, `workforceSite`, `riskZone`, `industrialSite`, `alertsOnly`."""

    contacts: Optional[List[ContactTinyResponse]] = None
    r"""An array Contact mini-objects that are associated the Address."""

    created_at_time: Annotated[
        Optional[datetime], pydantic.Field(alias="createdAtTime")
    ] = None
    r"""The date and time this address was created in RFC 3339 format."""

    external_ids: Annotated[
        Optional[ExternalIds], pydantic.Field(alias="externalIds")
    ] = None
    r"""The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object."""

    latitude: Optional[float] = None
    r"""Latitude of the address. Will be geocoded from `formattedAddress` if not provided."""

    longitude: Optional[float] = None
    r"""Longitude of the address. Will be geocoded from `formattedAddress` if not provided."""

    notes: Optional[str] = None
    r"""Notes about the address."""

    tags: Optional[List[TagTinyResponse]] = None
    r"""An array of all tag mini-objects that are associated with the given address entry."""
