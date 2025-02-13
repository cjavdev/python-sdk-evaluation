# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class OrganizationInfoCarrierSettings(UniversalBaseModel):
    """
    Carrier for a given organization.
    """

    carrier_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="carrierName")] = (
        pydantic.Field(default=None)
    )
    """
    Carrier for a given organization.
    """

    dot_number: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="dotNumber")] = pydantic.Field(
        default=None
    )
    """
    Carrier US DOT Number for the organization.
    """

    main_office_address: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="mainOfficeAddress")] = (
        pydantic.Field(default=None)
    )
    """
    Main office address for a given organization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
