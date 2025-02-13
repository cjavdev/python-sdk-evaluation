# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1AssetLocationResponse", "V1AssetLocationResponseItem"]


class V1AssetLocationResponseItem(BaseModel):
    latitude: Optional[float] = None
    """The latitude of the location in degrees."""

    location: Optional[str] = None
    """The best effort (street,city,state) for the latitude and longitude."""

    longitude: Optional[float] = None
    """The longitude of the location in degrees."""

    speed_miles_per_hour: Optional[float] = FieldInfo(alias="speedMilesPerHour", default=None)
    """
    The speed calculated from GPS that the asset was traveling at in miles per hour.
    """

    time: Optional[float] = None
    """Time in Unix milliseconds since epoch when the asset was at the location."""


V1AssetLocationResponse: TypeAlias = List[V1AssetLocationResponseItem]
