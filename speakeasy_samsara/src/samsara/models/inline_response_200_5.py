"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v1messageresponse import V1MessageResponse, V1MessageResponseTypedDict
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class InlineResponse2005TypedDict(TypedDict):
    r"""A list of messages."""

    data: NotRequired[List[V1MessageResponseTypedDict]]


class InlineResponse2005(BaseModel):
    r"""A list of messages."""

    data: Optional[List[V1MessageResponse]] = None
