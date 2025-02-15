# This file was auto-generated by Fern from our API Definition.

from .tiny_tag import TinyTag
from .tag_all_of import TagAllOf
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class Tag(TinyTag, TagAllOf):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
