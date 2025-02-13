"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .driverappnotificationobjectresponsebody import (
    DriverAppNotificationObjectResponseBody,
    DriverAppNotificationObjectResponseBodyTypedDict,
)
from .recipientobjectresponsebody import (
    RecipientObjectResponseBody,
    RecipientObjectResponseBodyTypedDict,
)
from .webhookparamsobjectresponsebody import (
    WebhookParamsObjectResponseBody,
    WebhookParamsObjectResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ActionParamsObjectResponseBodyTypedDict(TypedDict):
    r"""The action type specific details. Set webhookIds for Slack or Webhook actions. Set recipients for Notifications. Set driverAppNotification for Driver App Push. Other action types don't need to set a param."""

    driver_app_notification: NotRequired[
        DriverAppNotificationObjectResponseBodyTypedDict
    ]
    r"""Driver app notification settings"""
    recipients: NotRequired[List[RecipientObjectResponseBodyTypedDict]]
    r"""Recipient of the action."""
    webhooks: NotRequired[WebhookParamsObjectResponseBodyTypedDict]
    r"""The webhook configuration for an Action."""


class ActionParamsObjectResponseBody(BaseModel):
    r"""The action type specific details. Set webhookIds for Slack or Webhook actions. Set recipients for Notifications. Set driverAppNotification for Driver App Push. Other action types don't need to set a param."""

    driver_app_notification: Annotated[
        Optional[DriverAppNotificationObjectResponseBody],
        pydantic.Field(alias="driverAppNotification"),
    ] = None
    r"""Driver app notification settings"""

    recipients: Optional[List[RecipientObjectResponseBody]] = None
    r"""Recipient of the action."""

    webhooks: Optional[WebhookParamsObjectResponseBody] = None
    r"""The webhook configuration for an Action."""
