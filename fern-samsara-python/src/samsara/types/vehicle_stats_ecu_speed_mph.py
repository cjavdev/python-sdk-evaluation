# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .time import Time
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class VehicleStatsEcuSpeedMph(UniversalBaseModel):
    """
    The speed of the vehicle in miles per hour, as reported by the ECU.
    """

    time: Time
    value: float = pydantic.Field()
    """
    The speed of the vehicle in miles per hour.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
