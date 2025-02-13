# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .training_assignment_near_due_date_trigger_assignment_group_object_response_body import (
    TrainingAssignmentNearDueDateTriggerAssignmentGroupObjectResponseBody,
)
from ..core.serialization import FieldMetadata
import pydantic
from .training_assignment_near_due_date_trigger_details_object_response_body_condition_units import (
    TrainingAssignmentNearDueDateTriggerDetailsObjectResponseBodyConditionUnits,
)
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TrainingAssignmentNearDueDateTriggerDetailsObjectResponseBody(UniversalBaseModel):
    """
    Details specific to Training Assignment Near Due Date
    """

    assignment_groups: typing_extensions.Annotated[
        typing.Optional[typing.List[TrainingAssignmentNearDueDateTriggerAssignmentGroupObjectResponseBody]],
        FieldMetadata(alias="assignmentGroups"),
    ] = pydantic.Field(default=None)
    """
    The assignment groups the trigger is configured for.
    """

    condition_units: typing_extensions.Annotated[
        TrainingAssignmentNearDueDateTriggerDetailsObjectResponseBodyConditionUnits,
        FieldMetadata(alias="conditionUnits"),
    ] = pydantic.Field()
    """
    Whether the trigger is configured in days or weeks.  Valid values: `DAYS`, `WEEKS`
    """

    condition_value: typing_extensions.Annotated[int, FieldMetadata(alias="conditionValue")] = pydantic.Field()
    """
    The number of days or weeks near the due date to trigger on.
    """

    timezone: str = pydantic.Field()
    """
    The timezone that the alert will be set up in.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
