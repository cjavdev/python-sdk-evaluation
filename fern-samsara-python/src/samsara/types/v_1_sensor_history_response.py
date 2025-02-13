# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .v_1_sensor_history_response_results import V1SensorHistoryResponseResults
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class V1SensorHistoryResponse(UniversalBaseModel):
    """
    Contains the results for a sensor history request. Each result contains a timestamp and datapoint for each requested (sensor, field) pair.
    """

    results: typing.Optional[typing.List[V1SensorHistoryResponseResults]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
