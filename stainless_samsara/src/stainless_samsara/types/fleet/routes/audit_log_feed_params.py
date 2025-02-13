# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AuditLogFeedParams"]


class AuditLogFeedParams(TypedDict, total=False):
    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    expand: Literal["route"]
    """Expands the specified value(s) in the response object.

    Expansion populates additional fields in an object, if supported. Unsupported
    fields are ignored. To expand multiple fields, input a comma-separated list.

    Valid value: `route` Valid values: `route`
    """
