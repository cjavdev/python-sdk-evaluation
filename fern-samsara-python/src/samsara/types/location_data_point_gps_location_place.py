# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class LocationDataPointGpsLocationPlace(UniversalBaseModel):
    """
    Address of the location
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    City
    """

    house_number: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="houseNumber")] = (
        pydantic.Field(default=None)
    )
    """
    House number
    """

    neighborhood: typing.Optional[str] = pydantic.Field(default=None)
    """
    Neighborhood
    """

    poi: typing.Optional[str] = pydantic.Field(default=None)
    """
    POI
    """

    postcode: typing.Optional[str] = pydantic.Field(default=None)
    """
    Postcode
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    State
    """

    street: typing.Optional[str] = pydantic.Field(default=None)
    """
    Street
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
