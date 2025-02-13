# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ReeferListParams"]


class ReeferListParams(TypedDict, total=False):
    end_ms: Required[Annotated[int, PropertyInfo(alias="endMs")]]
    """Timestamp in milliseconds representing the end of the period to fetch,
    inclusive.

    Used in combination with startMs.
    """

    start_ms: Required[Annotated[int, PropertyInfo(alias="startMs")]]
    """
    Timestamp in milliseconds representing the start of the period to fetch,
    inclusive. Used in combination with endMs.
    """

    ending_before: Annotated[str, PropertyInfo(alias="endingBefore")]
    """Pagination parameter indicating the cursor position to return results before.

    Used in conjunction with the 'limit' parameter. Mutually exclusive with
    'startingAfter' parameter.
    """

    limit: float
    """Pagination parameter indicating the number of results to return in this request.

    Used in conjunction with either 'startingAfter' or 'endingBefore'.
    """

    starting_after: Annotated[str, PropertyInfo(alias="startingAfter")]
    """
    Pagination parameter indicating the cursor position to continue returning
    results after. Used in conjunction with the 'limit' parameter. Mutually
    exclusive with 'endingBefore' parameter.
    """
