# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class EngineImmobilizerGetEngineImmobilizerStatesUnauthorizedErrorResponseBody(UniversalBaseModel):
    """
    Unauthorized
    """

    message: str = pydantic.Field()
    """
    Message of error
    """

    request_id: typing_extensions.Annotated[str, FieldMetadata(alias="requestId")] = pydantic.Field()
    """
    The request ID; used when reaching out to support for issues with requests.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
