# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .vehicle_stats_decorations import VehicleStatsDecorations
from .time import Time
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class VehicleStatsEvAverageBatteryTemperatureMilliCelsiusWithDecoration(UniversalBaseModel):
    """
    Battery temperature for electric and hybrid vehicles in milli celsius. Not all EV and HEVs may report this field.
    """

    decorations: typing.Optional[VehicleStatsDecorations] = None
    time: Time
    value: int = pydantic.Field()
    """
    Battery temperature for electric and hybrid vehicles in milli celsius.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
