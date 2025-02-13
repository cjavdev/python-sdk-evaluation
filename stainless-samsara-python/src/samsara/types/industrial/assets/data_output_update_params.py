# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DataOutputUpdateParams"]


class DataOutputUpdateParams(TypedDict, total=False):
    values: Required[object]
    """A map of data output IDs to values.

    All data outputs must belong to the same asset. Only the specified IDs will be
    written to.
    """
