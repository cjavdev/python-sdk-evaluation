# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .goa_attribute_tiny_response_body import GoaAttributeTinyResponseBody
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from .goa_gateway_tiny_response_response_body import GoaGatewayTinyResponseResponseBody
from .goa_tag_tiny_response_response_body import GoaTagTinyResponseResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class EquipmentWithAttributesResponseObjectResponseBody(UniversalBaseModel):
    """
    The equipment object.
    """

    attributes: typing.Optional[typing.List[GoaAttributeTinyResponseBody]] = pydantic.Field(default=None)
    """
    List of attributes associated with the entity
    """

    equipment_serial_number: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="equipmentSerialNumber")
    ] = pydantic.Field(default=None)
    """
    The serial number of the equipment.
    """

    external_ids: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="externalIds")
    ] = pydantic.Field(default=None)
    """
    A map of external ids
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique Samsara ID of the Equipment. This is automatically generated when the Equipment object is created. It cannot be changed.
    """

    installed_gateway: typing_extensions.Annotated[
        typing.Optional[GoaGatewayTinyResponseResponseBody], FieldMetadata(alias="installedGateway")
    ] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-readable name of the Equipment. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time.
    """

    notes: typing.Optional[str] = pydantic.Field(default=None)
    """
    These are generic notes about the Equipment. Empty by default. Can be set or updated through the Samsara Dashboard or the API at any time.
    """

    tags: typing.Optional[typing.List[GoaTagTinyResponseResponseBody]] = pydantic.Field(default=None)
    """
    The list of [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting) associated with the Equipment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
