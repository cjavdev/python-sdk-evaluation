# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RunRetrieveParams"]


class RunRetrieveParams(TypedDict, total=False):
    include: str
    """Include is a filter parameter. Accepts 'pass', 'reject' or 'no_read'."""

    limit: int
    """Limit is an integer value from 1 to 1,000."""

    program_id: int
    """The configured program's ID on the camera."""

    started_at_ms: Annotated[int, PropertyInfo(alias="startedAtMs")]
    """EndMs is an optional param. It will default to the current time."""
