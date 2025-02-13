# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["DefectTypeListParams"]


class DefectTypeListParams(TypedDict, total=False):
    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    ids: List[str]
    """A filter on the data based on this comma-separated list of defect type IDs."""

    limit: int
    """The limit for how many objects will be in the response.

    Default and max for this value is 512 objects.
    """
