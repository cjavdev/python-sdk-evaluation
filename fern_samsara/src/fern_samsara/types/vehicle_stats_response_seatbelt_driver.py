# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from .vehicle_stats_response_seatbelt_driver_value import VehicleStatsResponseSeatbeltDriverValue
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class VehicleStatsResponseSeatbeltDriver(UniversalBaseModel):
    """
    Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`.
    """

    time: str = pydantic.Field()
    """
    UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    """

    value: VehicleStatsResponseSeatbeltDriverValue = pydantic.Field()
    """
    Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
