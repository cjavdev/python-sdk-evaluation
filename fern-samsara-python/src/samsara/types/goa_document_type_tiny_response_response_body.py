# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GoaDocumentTypeTinyResponseResponseBody(UniversalBaseModel):
    """
    A minified document type object
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the document type.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the document type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
