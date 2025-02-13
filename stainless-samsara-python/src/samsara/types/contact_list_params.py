# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ContactListParams"]


class ContactListParams(TypedDict, total=False):
    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    limit: int
    """The limit for how many objects will be in the response.

    Default and max for this value is 512 objects.
    """
