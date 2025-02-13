"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .trainingassignmentresponseobjectresponsebody import (
    TrainingAssignmentResponseObjectResponseBody,
    TrainingAssignmentResponseObjectResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class TrainingAssignmentsPatchTrainingAssignmentsResponseBodyTypedDict(TypedDict):
    data: List[TrainingAssignmentResponseObjectResponseBodyTypedDict]
    r"""List of updated training assignments."""


class TrainingAssignmentsPatchTrainingAssignmentsResponseBody(BaseModel):
    data: List[TrainingAssignmentResponseObjectResponseBody]
    r"""List of updated training assignments."""
