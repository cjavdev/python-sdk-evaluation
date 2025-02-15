# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class VehicleStatsFaultCodesValueObdiiConfirmedDtcs(UniversalBaseModel):
    """
    Passenger vehicle DTC information
    """

    dtc_description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="dtcDescription")] = (
        pydantic.Field(default=None)
    )
    """
    The DTC description, if available.
    """

    dtc_id: typing_extensions.Annotated[int, FieldMetadata(alias="dtcId")] = pydantic.Field()
    """
    The DTC identifier.
    """

    dtc_short_code: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="dtcShortCode")] = (
        pydantic.Field(default=None)
    )
    """
    The DTC short code, if available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
