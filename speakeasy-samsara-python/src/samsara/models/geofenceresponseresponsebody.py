"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GeofenceResponseResponseBodyTypedDict(TypedDict):
    r"""Closest geofence based on 1000 meter radial search."""

    external_ids: NotRequired[Dict[str, str]]
    r"""A map of external ids"""
    id: NotRequired[str]
    r"""Unique ID of the geofence object."""


class GeofenceResponseResponseBody(BaseModel):
    r"""Closest geofence based on 1000 meter radial search."""

    external_ids: Annotated[
        Optional[Dict[str, str]], pydantic.Field(alias="externalIds")
    ] = None
    r"""A map of external ids"""

    id: Optional[str] = None
    r"""Unique ID of the geofence object."""
