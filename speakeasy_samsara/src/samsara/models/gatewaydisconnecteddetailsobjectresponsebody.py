"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class GatewayDisconnectedDetailsObjectResponseBodyTypedDict(TypedDict):
    r"""Details specific to Gateway Disconnected"""

    min_duration_milliseconds: int
    r"""The number of milliseconds the trigger needs to stay active before alerting. Can only be either 900000 (15 minutes) or 3600000 (60 min)."""


class GatewayDisconnectedDetailsObjectResponseBody(BaseModel):
    r"""Details specific to Gateway Disconnected"""

    min_duration_milliseconds: Annotated[
        int, pydantic.Field(alias="minDurationMilliseconds")
    ]
    r"""The number of milliseconds the trigger needs to stay active before alerting. Can only be either 900000 (15 minutes) or 3600000 (60 min)."""
