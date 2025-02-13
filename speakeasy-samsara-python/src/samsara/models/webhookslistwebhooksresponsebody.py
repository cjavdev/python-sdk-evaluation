"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .goapaginationresponseresponsebody import (
    GoaPaginationResponseResponseBody,
    GoaPaginationResponseResponseBodyTypedDict,
)
from .webhookresponseresponsebody import (
    WebhookResponseResponseBody,
    WebhookResponseResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class WebhooksListWebhooksResponseBodyTypedDict(TypedDict):
    data: List[WebhookResponseResponseBodyTypedDict]
    r"""This is a list of Webhooks."""
    pagination: GoaPaginationResponseResponseBodyTypedDict
    r"""Pagination parameters."""


class WebhooksListWebhooksResponseBody(BaseModel):
    data: List[WebhookResponseResponseBody]
    r"""This is a list of Webhooks."""

    pagination: GoaPaginationResponseResponseBody
    r"""Pagination parameters."""
