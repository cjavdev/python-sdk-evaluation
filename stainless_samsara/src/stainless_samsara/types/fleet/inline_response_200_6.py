# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InlineResponse200_6", "Data"]


class Data(BaseModel):
    driver_id: int = FieldInfo(alias="driverId")
    """ID of the driver for whom the message is sent to or sent by."""

    text: str
    """The text sent in the message."""


class InlineResponse200_6(BaseModel):
    data: Optional[List[Data]] = None
