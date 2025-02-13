# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AlertEventDevice(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    ID of the Vehicle or Asset
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the Vehicle or Asset
    """

    serial: typing.Optional[str] = pydantic.Field(default=None)
    """
    Device serial number
    """

    vin: typing.Optional[str] = pydantic.Field(default=None)
    """
    VIN if the gateway is tied to a vehicle
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
