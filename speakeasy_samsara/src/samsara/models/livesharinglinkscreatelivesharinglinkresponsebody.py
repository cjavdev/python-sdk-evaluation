"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .livesharinglinkfullresponseobjectresponsebody import (
    LiveSharingLinkFullResponseObjectResponseBody,
    LiveSharingLinkFullResponseObjectResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing_extensions import TypedDict


class LiveSharingLinksCreateLiveSharingLinkResponseBodyTypedDict(TypedDict):
    data: LiveSharingLinkFullResponseObjectResponseBodyTypedDict
    r"""Live Sharing Link object"""


class LiveSharingLinksCreateLiveSharingLinkResponseBody(BaseModel):
    data: LiveSharingLinkFullResponseObjectResponseBody
    r"""Live Sharing Link object"""
