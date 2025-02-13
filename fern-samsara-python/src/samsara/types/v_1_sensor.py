# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class V1Sensor(UniversalBaseModel):
    """
    Contains information about a sensor.
    """

    id: int = pydantic.Field()
    """
    ID of the sensor.
    """

    mac_address: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="macAddress")] = pydantic.Field(
        default=None
    )
    """
    MAC address of the sensor.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the sensor.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
