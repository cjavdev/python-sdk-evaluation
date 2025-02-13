# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DriverTrailerAssignmentUpdateParams"]


class DriverTrailerAssignmentUpdateParams(TypedDict, total=False):
    id: Required[str]
    """Samsara ID for the assignment."""

    end_time: Required[Annotated[str, PropertyInfo(alias="endTime")]]
    """The end time in RFC 3339 format. The end time should not be in the future"""
