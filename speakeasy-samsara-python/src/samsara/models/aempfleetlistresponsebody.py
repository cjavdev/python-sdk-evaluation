"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .aempequipmentwithadditionalfieldsresponsebody import (
    AempEquipmentWithAdditionalFieldsResponseBody,
    AempEquipmentWithAdditionalFieldsResponseBodyTypedDict,
)
from .aemplinkresponsebody import AempLinkResponseBody, AempLinkResponseBodyTypedDict
import pydantic
from samsara.types import BaseModel
from typing import List
from typing_extensions import Annotated, TypedDict


class AempFleetListResponseBodyTypedDict(TypedDict):
    r"""Contains a list of equipment objects and links"""

    equipment: List[AempEquipmentWithAdditionalFieldsResponseBodyTypedDict]
    r"""The list of Equipment objects."""
    links: List[AempLinkResponseBodyTypedDict]
    r"""The list of links associated with the current API request."""
    snapshot_time: str
    r"""Date and time at which the snapshot of the fleet was created in RFC 3339 format."""
    version: str
    r"""The version of the ISO/TS 15143-3 standard"""


class AempFleetListResponseBody(BaseModel):
    r"""Contains a list of equipment objects and links"""

    equipment: Annotated[
        List[AempEquipmentWithAdditionalFieldsResponseBody],
        pydantic.Field(alias="Equipment"),
    ]
    r"""The list of Equipment objects."""

    links: Annotated[List[AempLinkResponseBody], pydantic.Field(alias="Links")]
    r"""The list of links associated with the current API request."""

    snapshot_time: Annotated[str, pydantic.Field(alias="snapshotTime")]
    r"""Date and time at which the snapshot of the fleet was created in RFC 3339 format."""

    version: str
    r"""The version of the ISO/TS 15143-3 standard"""
