# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .tagged_object import TaggedObject
import pydantic
import typing_extensions
from .tag_all_of_external_ids import TagAllOfExternalIds
from ..core.serialization import FieldMetadata
from .parent_tag import ParentTag
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TagAllOf(UniversalBaseModel):
    addresses: typing.Optional[typing.List[TaggedObject]] = pydantic.Field(default=None)
    """
    The addresses that belong to this tag.
    """

    assets: typing.Optional[typing.List[TaggedObject]] = pydantic.Field(default=None)
    """
    The trailers, unpowered, and powered assets that belong to this tag.
    """

    drivers: typing.Optional[typing.List[TaggedObject]] = pydantic.Field(default=None)
    """
    The drivers that belong to this tag.
    """

    external_ids: typing_extensions.Annotated[
        typing.Optional[TagAllOfExternalIds], FieldMetadata(alias="externalIds")
    ] = pydantic.Field(default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the given object.
    """

    machines: typing.Optional[typing.List[TaggedObject]] = pydantic.Field(default=None)
    """
    The machines that belong to thistag.
    """

    parent_tag: typing_extensions.Annotated[typing.Optional[ParentTag], FieldMetadata(alias="parentTag")] = None
    sensors: typing.Optional[typing.List[TaggedObject]] = pydantic.Field(default=None)
    """
    The sensors that belong to this tag.
    """

    vehicles: typing.Optional[typing.List[TaggedObject]] = pydantic.Field(default=None)
    """
    The vehicles that belong to this tag.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
