"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara import utils
from samsara.types import BaseModel
from typing_extensions import Annotated


class CoachingSessionsGetCoachingSessionsTooManyRequestsErrorResponseBodyData(
    BaseModel
):
    message: str
    r"""Message of error"""

    request_id: Annotated[str, pydantic.Field(alias="requestId")]
    r"""The request ID; used when reaching out to support for issues with requests."""


class CoachingSessionsGetCoachingSessionsTooManyRequestsErrorResponseBody(Exception):
    r"""Too many requests"""

    data: CoachingSessionsGetCoachingSessionsTooManyRequestsErrorResponseBodyData

    def __init__(
        self,
        data: CoachingSessionsGetCoachingSessionsTooManyRequestsErrorResponseBodyData,
    ):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data,
            CoachingSessionsGetCoachingSessionsTooManyRequestsErrorResponseBodyData,
        )
