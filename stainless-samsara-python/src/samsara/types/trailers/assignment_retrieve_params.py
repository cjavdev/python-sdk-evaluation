# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AssignmentRetrieveParams"]


class AssignmentRetrieveParams(TypedDict, total=False):
    end_ms: Annotated[int, PropertyInfo(alias="endMs")]
    """Timestamp in Unix epoch milliseconds representing the end of the period to
    fetch.

    Omitting endMs sets endMs as the current time
    """

    start_ms: Annotated[int, PropertyInfo(alias="startMs")]
    """
    Timestamp in Unix epoch milliseconds representing the start of the period to
    fetch. Omitting both startMs and endMs only returns current assignments.
    """
