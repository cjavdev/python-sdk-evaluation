# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .time import Time
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class VehicleStatsGpsOdometerMeters(UniversalBaseModel):
    """
    Vehicle GPS odometer event.
    """

    time: Time
    value: int = pydantic.Field()
    """
    Number of meters the vehicle has traveled according to the GPS calculations and the manually-specified odometer reading.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
