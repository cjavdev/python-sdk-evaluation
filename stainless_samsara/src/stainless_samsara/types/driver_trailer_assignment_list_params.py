# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DriverTrailerAssignmentListParams"]


class DriverTrailerAssignmentListParams(TypedDict, total=False):
    driver_ids: Required[Annotated[List[str], PropertyInfo(alias="driverIds")]]
    """
    A filter on the data based on this comma-separated list of driver IDs and
    externalIds. Example: `driverIds=1234,5678,payroll:4841`
    """

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    include_external_ids: Annotated[bool, PropertyInfo(alias="includeExternalIds")]
    """
    Optional boolean indicating whether to return external IDs on supported entities
    """
