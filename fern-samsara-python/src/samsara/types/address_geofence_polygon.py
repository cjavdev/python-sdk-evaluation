# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .address_geofence_polygon_vertices import AddressGeofencePolygonVertices
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AddressGeofencePolygon(UniversalBaseModel):
    """
    Information about a polygon geofence. This field is only needed if the geofence is a polygon.
    """

    vertices: typing.List[AddressGeofencePolygonVertices] = pydantic.Field()
    """
    The vertices of the polygon geofence. These geofence vertices describe the perimeter of the polygon, and must consist of at least 3 vertices and less than 40.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
