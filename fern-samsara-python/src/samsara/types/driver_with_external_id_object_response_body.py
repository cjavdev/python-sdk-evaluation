# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DriverWithExternalIdObjectResponseBody(UniversalBaseModel):
    """
    A driver object with an id and map of external ids.
    """

    driver_id: typing_extensions.Annotated[str, FieldMetadata(alias="driverId")] = pydantic.Field()
    """
    Samsara ID of the driver.
    """

    external_ids: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="externalIds")
    ] = pydantic.Field(default=None)
    """
    A map of external ids
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
