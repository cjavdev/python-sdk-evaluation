# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DutyStatusDurationObjectResponseBody(UniversalBaseModel):
    """
    The currently applied duty status durations on the driver's log.
    """

    active_duration_ms: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activeDurationMs")] = (
        pydantic.Field(default=None)
    )
    """
    Duration the driver was active for in the log period in milliseconds.
    """

    drive_duration_ms: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="driveDurationMs")] = (
        pydantic.Field(default=None)
    )
    """
    Duration the driver was driving for in the log period in milliseconds.
    """

    off_duty_duration_ms: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="offDutyDurationMs")
    ] = pydantic.Field(default=None)
    """
    Duration the driver was off duty for in the log period in milliseconds.
    """

    on_duty_duration_ms: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="onDutyDurationMs")] = (
        pydantic.Field(default=None)
    )
    """
    Duration the driver was on duty for in the log period in milliseconds.
    """

    personal_conveyance_duration_ms: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="personalConveyanceDurationMs")
    ] = pydantic.Field(default=None)
    """
    Duration the driver was driving for personal conveyance for in the log period in milliseconds.
    """

    sleeper_berth_duration_ms: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="sleeperBerthDurationMs")
    ] = pydantic.Field(default=None)
    """
    Duration the driver was in their sleeper berth for in the log period in milliseconds.
    """

    waiting_time_duration_ms: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="waitingTimeDurationMs")
    ] = pydantic.Field(default=None)
    """
    Duration the driver was waiting for in the log period in milliseconds.
    """

    yard_move_duration_ms: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="yardMoveDurationMs")
    ] = pydantic.Field(default=None)
    """
    Duration the driver was driving for yard moves for in the log period in milliseconds.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
