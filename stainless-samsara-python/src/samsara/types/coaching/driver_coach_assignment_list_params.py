# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DriverCoachAssignmentListParams"]


class DriverCoachAssignmentListParams(TypedDict, total=False):
    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    coach_ids: Annotated[List[str], PropertyInfo(alias="coachIds")]
    """Optional string of comma separated IDs of the coaches."""

    driver_ids: Annotated[List[str], PropertyInfo(alias="driverIds")]
    """Optional string of comma separated IDs of the drivers.

    This can be either a unique Samsara driver ID or an external ID for the driver.
    """

    include_external_ids: Annotated[bool, PropertyInfo(alias="includeExternalIds")]
    """
    Optional boolean indicating whether to return external IDs on supported entities
    """
