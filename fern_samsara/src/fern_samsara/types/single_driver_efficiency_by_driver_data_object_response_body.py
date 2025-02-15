# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .driver_efficiency_difficulty_score_data_object_response_body import (
    DriverEfficiencyDifficultyScoreDataObjectResponseBody,
)
from ..core.serialization import FieldMetadata
import pydantic
from .driver_efficiency_percentage_data_object_response_body import DriverEfficiencyPercentageDataObjectResponseBody
from .driver_efficiency_raw_data_object_response_body import DriverEfficiencyRawDataObjectResponseBody
from .driver_efficiency_data_object_response_body import DriverEfficiencyDataObjectResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SingleDriverEfficiencyByDriverDataObjectResponseBody(UniversalBaseModel):
    """
    singleDriverEfficiencyByDriverDataObject
    """

    difficulty_score: typing_extensions.Annotated[
        typing.Optional[DriverEfficiencyDifficultyScoreDataObjectResponseBody], FieldMetadata(alias="difficultyScore")
    ] = None
    driver_id: typing_extensions.Annotated[str, FieldMetadata(alias="driverId")] = pydantic.Field()
    """
    ID of the driver.
    """

    percentage_data: typing_extensions.Annotated[
        typing.Optional[DriverEfficiencyPercentageDataObjectResponseBody], FieldMetadata(alias="percentageData")
    ] = None
    raw_data: typing_extensions.Annotated[
        typing.Optional[DriverEfficiencyRawDataObjectResponseBody], FieldMetadata(alias="rawData")
    ] = None
    score_data: typing_extensions.Annotated[
        typing.Optional[DriverEfficiencyDataObjectResponseBody], FieldMetadata(alias="scoreData")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
