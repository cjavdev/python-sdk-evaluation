# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SafetyHarshEventParams"]


class SafetyHarshEventParams(TypedDict, total=False):
    timestamp: Required[int]
    """Timestamp in milliseconds representing the timestamp of a harsh event."""
