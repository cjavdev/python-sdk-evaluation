# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DriverEfficiencyDataObjectResponseBody(UniversalBaseModel):
    """
    Driver Efficiency score data. This object is returned by default or when the “score” format is specified in “dataFormats”.
    """

    anticipation_score: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="anticipationScore")] = (
        pydantic.Field(default=None)
    )
    """
    Represents the anticipation score for the driver. The score will be in either number or letter format depending on the organisation config.
    """

    coasting_score: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="coastingScore")] = (
        pydantic.Field(default=None)
    )
    """
    Represents the coasting score for the driver. The score will be in either number or letter format depending on the organisation config.
    """

    cruise_control_score: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cruiseControlScore")
    ] = pydantic.Field(default=None)
    """
    Represents the cruise control score for the driver. The score will be in either number or letter format depending on the organisation config.
    """

    green_band_score: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="greenBandScore")] = (
        pydantic.Field(default=None)
    )
    """
    Represents the green band score for the driver. The score will be in either number or letter format depending on the organisation config.
    """

    high_torque_score: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="highTorqueScore")] = (
        pydantic.Field(default=None)
    )
    """
    Represents the high torque score for the driver. The score will be in either number or letter format depending on the organisation config.
    """

    idling_score: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="idlingScore")] = (
        pydantic.Field(default=None)
    )
    """
    Represents the idling score for the driver.The score will be in either number or letter format depending on the organisation config.
    """

    over_speed_score: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="overSpeedScore")] = (
        pydantic.Field(default=None)
    )
    """
    Represents the over speed score for the driver. The score will be in either number or letter format depending on the organisation config.
    """

    overall_score: typing_extensions.Annotated[str, FieldMetadata(alias="overallScore")] = pydantic.Field()
    """
    Represents the overall score for the driver. The score will be in either number (0-100) as a string or letter format (A-G) depending on the organisation config.
    """

    wear_free_brake_score: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="wearFreeBrakeScore")
    ] = pydantic.Field(default=None)
    """
    Represents the ware-free breaking score for the driver. The score will be in either number or letter format depending on the organisation config.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
