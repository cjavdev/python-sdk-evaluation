"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .trainingassignmentnearduedatetriggerassignmentgroupobjectresponsebody import (
    TrainingAssignmentNearDueDateTriggerAssignmentGroupObjectResponseBody,
    TrainingAssignmentNearDueDateTriggerAssignmentGroupObjectResponseBodyTypedDict,
)
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ConditionUnits(str, Enum):
    r"""Whether the trigger is configured in days or weeks.  Valid values: `DAYS`, `WEEKS`"""

    DAYS = "DAYS"
    WEEKS = "WEEKS"


class TrainingAssignmentNearDueDateTriggerDetailsObjectResponseBodyTypedDict(TypedDict):
    r"""Details specific to Training Assignment Near Due Date"""

    condition_units: ConditionUnits
    r"""Whether the trigger is configured in days or weeks.  Valid values: `DAYS`, `WEEKS`"""
    condition_value: int
    r"""The number of days or weeks near the due date to trigger on."""
    timezone: str
    r"""The timezone that the alert will be set up in."""
    assignment_groups: NotRequired[
        List[
            TrainingAssignmentNearDueDateTriggerAssignmentGroupObjectResponseBodyTypedDict
        ]
    ]
    r"""The assignment groups the trigger is configured for."""


class TrainingAssignmentNearDueDateTriggerDetailsObjectResponseBody(BaseModel):
    r"""Details specific to Training Assignment Near Due Date"""

    condition_units: Annotated[ConditionUnits, pydantic.Field(alias="conditionUnits")]
    r"""Whether the trigger is configured in days or weeks.  Valid values: `DAYS`, `WEEKS`"""

    condition_value: Annotated[int, pydantic.Field(alias="conditionValue")]
    r"""The number of days or weeks near the due date to trigger on."""

    timezone: str
    r"""The timezone that the alert will be set up in."""

    assignment_groups: Annotated[
        Optional[
            List[TrainingAssignmentNearDueDateTriggerAssignmentGroupObjectResponseBody]
        ],
        pydantic.Field(alias="assignmentGroups"),
    ] = None
    r"""The assignment groups the trigger is configured for."""
