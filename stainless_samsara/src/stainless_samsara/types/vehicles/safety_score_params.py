# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SafetyScoreParams"]


class SafetyScoreParams(TypedDict, total=False):
    end_ms: Required[Annotated[int, PropertyInfo(alias="endMs")]]
    """Timestamp in milliseconds representing the end of the period to fetch,
    inclusive.

    Used in combination with startMs. Total duration (endMs - startMs) must be
    greater than or equal to 1 hour.
    """

    start_ms: Required[Annotated[int, PropertyInfo(alias="startMs")]]
    """
    Timestamp in milliseconds representing the start of the period to fetch,
    inclusive. Used in combination with endMs. Total duration (endMs - startMs) must
    be greater than or equal to 1 hour.
    """
