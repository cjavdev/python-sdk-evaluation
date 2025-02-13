# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class ScheduledMaintenanceByEngineHoursDetailsObjectResponseBody(UniversalBaseModel):
    """
    Details specific to Scheduled Maintenance By Engine Hours
    """

    due_in_hours: typing_extensions.Annotated[int, FieldMetadata(alias="dueInHours")] = pydantic.Field()
    """
    Alert when maintenance is due in the specified number of hours.
    """

    schedule_id: typing_extensions.Annotated[str, FieldMetadata(alias="scheduleId")] = pydantic.Field()
    """
    The id of the maintenance schedule.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
