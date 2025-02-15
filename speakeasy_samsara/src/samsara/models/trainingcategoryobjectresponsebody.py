"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class TrainingCategoryObjectResponseBodyTypedDict(TypedDict):
    r"""Category of the training course."""

    id: str
    r"""Category ID of the course."""
    name: str
    r"""Category name of the course."""


class TrainingCategoryObjectResponseBody(BaseModel):
    r"""Category of the training course."""

    id: str
    r"""Category ID of the course."""

    name: str
    r"""Category name of the course."""
