"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara import utils
from samsara.types import BaseModel
from typing_extensions import Annotated


class AlertsPatchConfigurationsTooManyRequestsErrorResponseBodyData(BaseModel):
    message: str
    r"""Message of error"""

    request_id: Annotated[str, pydantic.Field(alias="requestId")]
    r"""The request ID; used when reaching out to support for issues with requests."""


class AlertsPatchConfigurationsTooManyRequestsErrorResponseBody(Exception):
    r"""Too many requests"""

    data: AlertsPatchConfigurationsTooManyRequestsErrorResponseBodyData

    def __init__(
        self, data: AlertsPatchConfigurationsTooManyRequestsErrorResponseBodyData
    ):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, AlertsPatchConfigurationsTooManyRequestsErrorResponseBodyData
        )
