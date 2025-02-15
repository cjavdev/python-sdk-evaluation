# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .assets_location_link_config_object_response_body import AssetsLocationLinkConfigObjectResponseBody
from ..core.serialization import FieldMetadata
from .assets_near_location_link_config_object_response_body import AssetsNearLocationLinkConfigObjectResponseBody
from .assets_on_route_link_config_object_response_body import AssetsOnRouteLinkConfigObjectResponseBody
import pydantic
from .live_sharing_link_full_response_object_response_body_type import LiveSharingLinkFullResponseObjectResponseBodyType
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class LiveSharingLinkFullResponseObjectResponseBody(UniversalBaseModel):
    """
    Live Sharing Link object
    """

    assets_location_link_config: typing_extensions.Annotated[
        typing.Optional[AssetsLocationLinkConfigObjectResponseBody], FieldMetadata(alias="assetsLocationLinkConfig")
    ] = None
    assets_near_location_link_config: typing_extensions.Annotated[
        typing.Optional[AssetsNearLocationLinkConfigObjectResponseBody],
        FieldMetadata(alias="assetsNearLocationLinkConfig"),
    ] = None
    assets_on_route_link_config: typing_extensions.Annotated[
        typing.Optional[AssetsOnRouteLinkConfigObjectResponseBody], FieldMetadata(alias="assetsOnRouteLinkConfig")
    ] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description for the Live Sharing Link (not applicable for 'assetsOnRoute' type).
    """

    expires_at_time: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="expiresAtTime")] = (
        pydantic.Field(default=None)
    )
    """
    Date that this link expires, in RFC 3339 format.
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the Live Sharing Link.
    """

    live_sharing_url: typing_extensions.Annotated[str, FieldMetadata(alias="liveSharingUrl")] = pydantic.Field()
    """
    The shareable URL of the vehicle's location.
    """

    name: str = pydantic.Field()
    """
    Name of the Live Sharing Link.
    """

    type: LiveSharingLinkFullResponseObjectResponseBodyType = pydantic.Field()
    """
    Type of the Live Sharing Link.  Valid values: `assetsLocation`, `assetsNearLocation`, `assetsOnRoute`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
