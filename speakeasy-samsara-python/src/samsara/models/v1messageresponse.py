"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v1messagesender import V1MessageSender, V1MessageSenderTypedDict
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class V1MessageResponseTypedDict(TypedDict):
    driver_id: int
    r"""ID of the driver for whom the message is sent to or sent by."""
    is_read: bool
    r"""True if the message was read by the recipient."""
    sender: V1MessageSenderTypedDict
    sent_at_ms: int
    r"""The time in Unix epoch milliseconds that the message is sent to the recipient."""
    text: str
    r"""The text sent in the message."""


class V1MessageResponse(BaseModel):
    driver_id: Annotated[int, pydantic.Field(alias="driverId")]
    r"""ID of the driver for whom the message is sent to or sent by."""

    is_read: Annotated[bool, pydantic.Field(alias="isRead")]
    r"""True if the message was read by the recipient."""

    sender: V1MessageSender

    sent_at_ms: Annotated[int, pydantic.Field(alias="sentAtMs")]
    r"""The time in Unix epoch milliseconds that the message is sent to the recipient."""

    text: str
    r"""The text sent in the message."""
