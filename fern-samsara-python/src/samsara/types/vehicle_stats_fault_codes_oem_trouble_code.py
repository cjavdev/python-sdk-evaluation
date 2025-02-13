# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class VehicleStatsFaultCodesOemTroubleCode(UniversalBaseModel):
    """
    Proprietary diagnostic trouble code for some OEM vehicles.
    """

    code_description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="codeDescription")] = (
        pydantic.Field(default=None)
    )
    """
    The OEM code description.
    """

    code_identifier: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="codeIdentifier")] = (
        pydantic.Field(default=None)
    )
    """
    The OEM code identifier.
    """

    code_severity: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="codeSeverity")] = (
        pydantic.Field(default=None)
    )
    """
    The OEM code severity.
    """

    code_source: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="codeSource")] = pydantic.Field(
        default=None
    )
    """
    The OEM code source.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
