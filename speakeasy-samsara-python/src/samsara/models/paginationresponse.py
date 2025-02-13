"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class PaginationResponseTypedDict(TypedDict):
    r"""Pagination parameters."""

    end_cursor: str
    r"""Cursor identifier representing the last element in the response. This value should be used in conjunction with a subsequent request's 'after' query parameter. This may be an empty string if there are no more pages left to view."""
    has_next_page: bool
    r"""True if there are more pages of results immediately available after this endCursor."""


class PaginationResponse(BaseModel):
    r"""Pagination parameters."""

    end_cursor: Annotated[str, pydantic.Field(alias="endCursor")]
    r"""Cursor identifier representing the last element in the response. This value should be used in conjunction with a subsequent request's 'after' query parameter. This may be an empty string if there are no more pages left to view."""

    has_next_page: Annotated[bool, pydantic.Field(alias="hasNextPage")]
    r"""True if there are more pages of results immediately available after this endCursor."""
