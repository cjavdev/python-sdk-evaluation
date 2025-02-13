# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from .operational_settings_object_response_body_time_range_type import (
    OperationalSettingsObjectResponseBodyTimeRangeType,
)
from ..core.serialization import FieldMetadata
import pydantic
import typing
from .time_range_object_response_body import TimeRangeObjectResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class OperationalSettingsObjectResponseBody(UniversalBaseModel):
    """
    Settings on when the alert should be operational.
    """

    time_range_type: typing_extensions.Annotated[
        OperationalSettingsObjectResponseBodyTimeRangeType, FieldMetadata(alias="timeRangeType")
    ] = pydantic.Field()
    """
    The type of time ranges.  Valid values: `activeBetween`, `inactiveBetween`
    """

    time_ranges: typing_extensions.Annotated[
        typing.List[TimeRangeObjectResponseBody], FieldMetadata(alias="timeRanges")
    ] = pydantic.Field()
    """
    The time ranges this alert applies to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
