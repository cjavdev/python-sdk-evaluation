"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class AssetsOnRouteLinkConfigObjectTypedDict(TypedDict):
    r"""Configuration details specific to the 'By Recurring Route' Live Sharing Link."""

    recurring_route_id: str
    r"""Samsara ID of the recurring route."""


class AssetsOnRouteLinkConfigObject(BaseModel):
    r"""Configuration details specific to the 'By Recurring Route' Live Sharing Link."""

    recurring_route_id: Annotated[str, pydantic.Field(alias="recurringRouteId")]
    r"""Samsara ID of the recurring route."""
