"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class DefectPhotoResponseResponseBodyTypedDict(TypedDict):
    r"""Defect's photo object"""

    created_at_time: str
    r"""Time when defect's photo was created in RFC 3339 format."""
    url: str
    r"""The URL to the defect's photo. Note: the link is available only for 24 hours after it's sent"""


class DefectPhotoResponseResponseBody(BaseModel):
    r"""Defect's photo object"""

    created_at_time: Annotated[str, pydantic.Field(alias="createdAtTime")]
    r"""Time when defect's photo was created in RFC 3339 format."""

    url: str
    r"""The URL to the defect's photo. Note: the link is available only for 24 hours after it's sent"""
