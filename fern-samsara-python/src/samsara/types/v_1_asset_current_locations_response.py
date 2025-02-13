# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .v_1_asset_cable import V1AssetCable
from .v_1_asset_current_location import V1AssetCurrentLocation
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class V1AssetCurrentLocationsResponse(UniversalBaseModel):
    """
    Basic information of an asset
    """

    asset_serial_number: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assetSerialNumber")] = (
        pydantic.Field(default=None)
    )
    """
    Asset serial number
    """

    cable: typing.Optional[V1AssetCable] = None
    engine_hours: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="engineHours")] = (
        pydantic.Field(default=None)
    )
    """
    Engine hours
    """

    id: int = pydantic.Field()
    """
    Asset ID
    """

    location: typing.Optional[typing.List[V1AssetCurrentLocation]] = pydantic.Field(default=None)
    """
    Current location of an asset
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Asset name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
