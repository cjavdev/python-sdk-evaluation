# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class VehicleStatsResponseEvAverageBatteryTemperatureMilliCelsius(UniversalBaseModel):
    """
    Battery temperature for electric and hybrid vehicles in milli celsius. Not all EV and HEVs may report this field.
    """

    time: str = pydantic.Field()
    """
    UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    """

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
