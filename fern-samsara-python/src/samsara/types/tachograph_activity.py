# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .tachograph_activity_state import TachographActivityState
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TachographActivity(UniversalBaseModel):
    """
    Tachograph activity
    """

    end_time: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="endTime")] = pydantic.Field(
        default=None
    )
    """
    End time of state in RFC 3339 format.
    """

    is_manual_entry: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isManualEntry")] = (
        pydantic.Field(default=None)
    )
    """
    A flag indicating whether the activity was manually entered by the driver. If this is `true`, the state cannot be "UNKNOWN"
    """

    start_time: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="startTime")] = pydantic.Field(
        default=None
    )
    """
    Start time of state in RFC 3339 format.
    """

    state: typing.Optional[TachographActivityState] = pydantic.Field(default=None)
    """
    Tachograph activity state. Valid values: `BREAK/REST`, `WORK`, `AVAILABILITY`, `DRIVING`, `UNKNOWN`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
