# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GoaDocumentTinyResponseResponseBody(UniversalBaseModel):
    """
    A minified Document object
    """

    id: str = pydantic.Field()
    """
    Id of the document
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the document
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
