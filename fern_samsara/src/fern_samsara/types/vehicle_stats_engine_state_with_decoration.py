# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .vehicle_stats_decorations import VehicleStatsDecorations
from .time import Time
from .vehicle_stats_engine_state_setting import VehicleStatsEngineStateSetting
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class VehicleStatsEngineStateWithDecoration(UniversalBaseModel):
    """
    Vehicle engine state event.
    """

    decorations: typing.Optional[VehicleStatsDecorations] = None
    time: Time
    value: VehicleStatsEngineStateSetting

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
