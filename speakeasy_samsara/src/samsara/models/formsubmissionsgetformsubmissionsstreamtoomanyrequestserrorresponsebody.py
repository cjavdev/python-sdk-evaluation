"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara import utils
from samsara.types import BaseModel
from typing_extensions import Annotated


class FormSubmissionsGetFormSubmissionsStreamTooManyRequestsErrorResponseBodyData(
    BaseModel
):
    message: str
    r"""Message of error"""

    request_id: Annotated[str, pydantic.Field(alias="requestId")]
    r"""The request ID; used when reaching out to support for issues with requests."""


class FormSubmissionsGetFormSubmissionsStreamTooManyRequestsErrorResponseBody(
    Exception
):
    r"""Too many requests"""

    data: FormSubmissionsGetFormSubmissionsStreamTooManyRequestsErrorResponseBodyData

    def __init__(
        self,
        data: FormSubmissionsGetFormSubmissionsStreamTooManyRequestsErrorResponseBodyData,
    ):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data,
            FormSubmissionsGetFormSubmissionsStreamTooManyRequestsErrorResponseBodyData,
        )
