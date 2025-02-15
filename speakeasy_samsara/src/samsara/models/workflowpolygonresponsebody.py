"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .vertexresponsebody import VertexResponseBody, VertexResponseBodyTypedDict
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class WorkflowPolygonResponseBodyTypedDict(TypedDict):
    r"""Information about a polygon geofence. This field is only needed if the geofence is a polygon."""

    vertices: NotRequired[List[VertexResponseBodyTypedDict]]
    r"""The vertices of the polygon geofence. These geofence vertices describe the perimeter of the polygon, and must consist of at least 3 vertices and less than 40."""


class WorkflowPolygonResponseBody(BaseModel):
    r"""Information about a polygon geofence. This field is only needed if the geofence is a polygon."""

    vertices: Optional[List[VertexResponseBody]] = None
    r"""The vertices of the polygon geofence. These geofence vertices describe the perimeter of the polygon, and must consist of at least 3 vertices and less than 40."""
