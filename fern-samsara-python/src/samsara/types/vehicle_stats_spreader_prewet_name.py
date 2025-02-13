# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .time import Time
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class VehicleStatsSpreaderPrewetName(UniversalBaseModel):
    """
    Name of most recent type of prewet material spread, read from the material spreader.
    """

    time: Time
    value: str = pydantic.Field()
    """
    Name of most recent type of prewet material spread, read from the material spreader.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
