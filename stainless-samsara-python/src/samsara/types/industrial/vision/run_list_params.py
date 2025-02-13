# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    duration_ms: Required[Annotated[int, PropertyInfo(alias="durationMs")]]
    """DurationMs is a required param.

    This works with the EndMs parameter. Indicates the duration in which the
    visionRuns will be fetched
    """

    end_ms: Annotated[int, PropertyInfo(alias="endMs")]
    """EndMs is an optional param. It will default to the current time."""
