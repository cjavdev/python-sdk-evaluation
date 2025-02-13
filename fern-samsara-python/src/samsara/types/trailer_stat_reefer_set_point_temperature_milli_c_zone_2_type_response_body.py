# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class TrailerStatReeferSetPointTemperatureMilliCZone2TypeResponseBody(UniversalBaseModel):
    """
    Set point temperature of zone 2 of the reefer.
    """

    time: str = pydantic.Field()
    """
    UTC timestamp in RFC 3339 format.
    """

    value: int = pydantic.Field()
    """
    The set point temperature reading in millidegree Celsius.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
