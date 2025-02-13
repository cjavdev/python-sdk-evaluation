# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from .training_assignment_near_due_date_trigger_assignment_group_object_request_body_assignment_group_type import (
    TrainingAssignmentNearDueDateTriggerAssignmentGroupObjectRequestBodyAssignmentGroupType,
)
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class TrainingAssignmentNearDueDateTriggerAssignmentGroupObjectRequestBody(UniversalBaseModel):
    """
    An assignment group of a specific course or a category can be selected for an alert.
    """

    assignment_group_type: typing_extensions.Annotated[
        TrainingAssignmentNearDueDateTriggerAssignmentGroupObjectRequestBodyAssignmentGroupType,
        FieldMetadata(alias="assignmentGroupType"),
    ] = pydantic.Field()
    """
    Assignment group type.  Valid values: `CATEGORY`, `COURSE`
    """

    assignment_group_uuid: typing_extensions.Annotated[str, FieldMetadata(alias="assignmentGroupUuid")] = (
        pydantic.Field()
    )
    """
    The unique ID of the assignment group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
