# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GatewayTiny(UniversalBaseModel):
    """
    A minified gateway including serial number and model.
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    The gateway model
    """

    serial: typing.Optional[str] = pydantic.Field(default=None)
    """
    The serial number of the gateway.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
