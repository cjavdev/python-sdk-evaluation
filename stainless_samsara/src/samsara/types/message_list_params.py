# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    duration_ms: Annotated[int, PropertyInfo(alias="durationMs")]
    """Time in milliseconds that represents the duration before endMs to query.

    Defaults to 24 hours.
    """

    end_ms: Annotated[int, PropertyInfo(alias="endMs")]
    """
    Time in unix milliseconds that represents the end of time range of messages to
    return. Used in combination with durationMs. Defaults to now.
    """
