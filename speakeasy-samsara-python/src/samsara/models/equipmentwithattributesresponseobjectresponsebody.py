"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .goaattributetinyresponsebody import (
    GoaAttributeTinyResponseBody,
    GoaAttributeTinyResponseBodyTypedDict,
)
from .goagatewaytinyresponseresponsebody import (
    GoaGatewayTinyResponseResponseBody,
    GoaGatewayTinyResponseResponseBodyTypedDict,
)
from .goatagtinyresponseresponsebody import (
    GoaTagTinyResponseResponseBody,
    GoaTagTinyResponseResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class EquipmentWithAttributesResponseObjectResponseBodyTypedDict(TypedDict):
    r"""The equipment object."""

    attributes: NotRequired[List[GoaAttributeTinyResponseBodyTypedDict]]
    r"""List of attributes associated with the entity"""
    equipment_serial_number: NotRequired[str]
    r"""The serial number of the equipment."""
    external_ids: NotRequired[Dict[str, str]]
    r"""A map of external ids"""
    id: NotRequired[str]
    r"""The unique Samsara ID of the Equipment. This is automatically generated when the Equipment object is created. It cannot be changed."""
    installed_gateway: NotRequired[GoaGatewayTinyResponseResponseBodyTypedDict]
    r"""A minified gateway object"""
    name: NotRequired[str]
    r"""The human-readable name of the Equipment. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time."""
    notes: NotRequired[str]
    r"""These are generic notes about the Equipment. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time."""
    tags: NotRequired[List[GoaTagTinyResponseResponseBodyTypedDict]]
    r"""The list of [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting) associated with the Equipment."""


class EquipmentWithAttributesResponseObjectResponseBody(BaseModel):
    r"""The equipment object."""

    attributes: Optional[List[GoaAttributeTinyResponseBody]] = None
    r"""List of attributes associated with the entity"""

    equipment_serial_number: Annotated[
        Optional[str], pydantic.Field(alias="equipmentSerialNumber")
    ] = None
    r"""The serial number of the equipment."""

    external_ids: Annotated[
        Optional[Dict[str, str]], pydantic.Field(alias="externalIds")
    ] = None
    r"""A map of external ids"""

    id: Optional[str] = None
    r"""The unique Samsara ID of the Equipment. This is automatically generated when the Equipment object is created. It cannot be changed."""

    installed_gateway: Annotated[
        Optional[GoaGatewayTinyResponseResponseBody],
        pydantic.Field(alias="installedGateway"),
    ] = None
    r"""A minified gateway object"""

    name: Optional[str] = None
    r"""The human-readable name of the Equipment. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time."""

    notes: Optional[str] = None
    r"""These are generic notes about the Equipment. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time."""

    tags: Optional[List[GoaTagTinyResponseResponseBody]] = None
    r"""The list of [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting) associated with the Equipment."""
