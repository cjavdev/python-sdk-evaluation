# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .time import Time
from .vehicle_stats_tire_pressures import VehicleStatsTirePressures
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class VehicleStatsTirePressure(UniversalBaseModel):
    """
    Vehicle tire pressure readings.
    """

    time: typing.Optional[Time] = None
    value: typing.Optional[VehicleStatsTirePressures] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
