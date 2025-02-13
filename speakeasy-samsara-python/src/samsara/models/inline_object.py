"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class InlineObjectTypedDict(TypedDict):
    apply_to_future_routes: NotRequired[bool]
    r"""This is only for a recurring route.  If set to true, delete all following runs of the route.  If set to false, only delete the current route."""


class InlineObject(BaseModel):
    apply_to_future_routes: Optional[bool] = None
    r"""This is only for a recurring route.  If set to true, delete all following runs of the route.  If set to false, only delete the current route."""
