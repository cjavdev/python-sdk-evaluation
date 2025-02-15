# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .vertex_response_body import VertexResponseBody
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SettingsResponseBody(UniversalBaseModel):
    """
    Information about a geofence settings.
    """

    show_addresses: typing_extensions.Annotated[
        typing.Optional[typing.List[VertexResponseBody]], FieldMetadata(alias="showAddresses")
    ] = pydantic.Field(default=None)
    """
    The geofence setting. If this setting set to true, then underlying geofence addresses will be shown in reports instead of a geofence's name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
