# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InlineResponse200_5", "Data", "DataSender"]


class DataSender(BaseModel):
    name: str
    """Name of user that is sending the message."""

    type: str
    """Type of user that is sending the message. It will be either dispatch or driver."""


class Data(BaseModel):
    driver_id: int = FieldInfo(alias="driverId")
    """ID of the driver for whom the message is sent to or sent by."""

    is_read: bool = FieldInfo(alias="isRead")
    """True if the message was read by the recipient."""

    sender: DataSender

    sent_at_ms: int = FieldInfo(alias="sentAtMs")
    """The time in Unix epoch milliseconds that the message is sent to the recipient."""

    text: str
    """The text sent in the message."""


class InlineResponse200_5(BaseModel):
    data: Optional[List[Data]] = None
