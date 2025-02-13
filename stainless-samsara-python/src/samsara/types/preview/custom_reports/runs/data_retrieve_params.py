# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DataRetrieveParams"]


class DataRetrieveParams(TypedDict, total=False):
    id: str
    """The ID of the specified run for the requested custom report."""

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """
