# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .dvir_signature_signatory_user import DvirSignatureSignatoryUser
from ..core.serialization import FieldMetadata
import pydantic
from .dvir_signature_type import DvirSignatureType
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DvirSignature(UniversalBaseModel):
    """
    DVIR Signure.
    """

    signatory_user: typing_extensions.Annotated[
        typing.Optional[DvirSignatureSignatoryUser], FieldMetadata(alias="signatoryUser")
    ] = None
    signed_at_time: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="signedAtTime")] = (
        pydantic.Field(default=None)
    )
    """
    The time when the DVIR was signed. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`.
    """

    type: typing.Optional[DvirSignatureType] = pydantic.Field(default=None)
    """
    Whether the DVIR was submitted by a `driver` or `mechanic`. Valid values: `driver`, `mechanic`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
