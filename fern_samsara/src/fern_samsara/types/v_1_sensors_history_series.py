# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .v_1_sensors_history_series_field import V1SensorsHistorySeriesField
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class V1SensorsHistorySeries(UniversalBaseModel):
    """
    V1Sensor ID and field to query.
    """

    field: V1SensorsHistorySeriesField = pydantic.Field()
    """
    Field to query.
    """

    widget_id: typing_extensions.Annotated[int, FieldMetadata(alias="widgetId")] = pydantic.Field()
    """
    V1Sensor ID to query.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
