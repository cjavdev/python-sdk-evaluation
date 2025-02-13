# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
import datetime as dt
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AlertEventDvirDefectsItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the defect
    """

    created_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="createdAt")] = (
        pydantic.Field(default=None)
    )
    """
    Creation timestamp
    """

    defect_type: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="defectType")] = pydantic.Field(
        default=None
    )
    """
    Type of defect
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    Defect comment
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
