"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .trainingassignmentspatchtrainingassignmentsbadrequesterrorresponsebody import (
    TrainingAssignmentsPatchTrainingAssignmentsBadRequestErrorResponseBody,
    TrainingAssignmentsPatchTrainingAssignmentsBadRequestErrorResponseBodyTypedDict,
)
from .trainingassignmentspatchtrainingassignmentsresponsebody import (
    TrainingAssignmentsPatchTrainingAssignmentsResponseBody,
    TrainingAssignmentsPatchTrainingAssignmentsResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata
from typing import List, Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class PatchTrainingAssignmentsRequestTypedDict(TypedDict):
    ids: List[str]
    r"""String of comma separated assignments IDs. Max value for this value is 100 objects .Example: `ids=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`"""
    due_at_time: str
    r"""Due date of the training assignment in RFC 3339 format. Millisecond precision and timezones are supported."""


class PatchTrainingAssignmentsRequest(BaseModel):
    ids: Annotated[
        List[str], FieldMetadata(query=QueryParamMetadata(style="form", explode=False))
    ]
    r"""String of comma separated assignments IDs. Max value for this value is 100 objects .Example: `ids=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`"""

    due_at_time: Annotated[
        str,
        pydantic.Field(alias="dueAtTime"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Due date of the training assignment in RFC 3339 format. Millisecond precision and timezones are supported."""


PatchTrainingAssignmentsResponseTypedDict = TypeAliasType(
    "PatchTrainingAssignmentsResponseTypedDict",
    Union[
        TrainingAssignmentsPatchTrainingAssignmentsResponseBodyTypedDict,
        TrainingAssignmentsPatchTrainingAssignmentsBadRequestErrorResponseBodyTypedDict,
    ],
)


PatchTrainingAssignmentsResponse = TypeAliasType(
    "PatchTrainingAssignmentsResponse",
    Union[
        TrainingAssignmentsPatchTrainingAssignmentsResponseBody,
        TrainingAssignmentsPatchTrainingAssignmentsBadRequestErrorResponseBody,
    ],
)
