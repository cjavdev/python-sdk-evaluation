"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara import utils
from samsara.types import BaseModel
from typing_extensions import Annotated


class WebhooksDeleteWebhookUnauthorizedErrorResponseBodyData(BaseModel):
    message: str
    r"""Message of error"""

    request_id: Annotated[str, pydantic.Field(alias="requestId")]
    r"""The request ID; used when reaching out to support for issues with requests."""


class WebhooksDeleteWebhookUnauthorizedErrorResponseBody(Exception):
    r"""Unauthorized"""

    data: WebhooksDeleteWebhookUnauthorizedErrorResponseBodyData

    def __init__(self, data: WebhooksDeleteWebhookUnauthorizedErrorResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, WebhooksDeleteWebhookUnauthorizedErrorResponseBodyData
        )
