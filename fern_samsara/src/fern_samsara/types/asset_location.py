# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .latitude import Latitude
from .longitude import Longitude
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AssetLocation(UniversalBaseModel):
    """
    For locationType "point", latitude and longitude are required. For "address", formattedAddress must be provided, and lat/long can be optionally included for displaying a dot on the assets map. For "dataInput", this object should not be passed in.
    """

    formatted_address: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="formattedAddress")] = (
        pydantic.Field(default=None)
    )
    """
    Formatted address of the location
    """

    latitude: typing.Optional[Latitude] = None
    longitude: typing.Optional[Longitude] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
