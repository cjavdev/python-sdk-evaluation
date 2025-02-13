"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara import utils
from samsara.types import BaseModel
from typing_extensions import Annotated


class TrainingAssignmentsDeleteTrainingAssignmentsNotImplementedErrorResponseBodyData(
    BaseModel
):
    message: str
    r"""Message of error"""

    request_id: Annotated[str, pydantic.Field(alias="requestId")]
    r"""The request ID; used when reaching out to support for issues with requests."""


class TrainingAssignmentsDeleteTrainingAssignmentsNotImplementedErrorResponseBody(
    Exception
):
    r"""Requested endpoint is not yet implemented"""

    data: (
        TrainingAssignmentsDeleteTrainingAssignmentsNotImplementedErrorResponseBodyData
    )

    def __init__(
        self,
        data: TrainingAssignmentsDeleteTrainingAssignmentsNotImplementedErrorResponseBodyData,
    ):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data,
            TrainingAssignmentsDeleteTrainingAssignmentsNotImplementedErrorResponseBodyData,
        )
