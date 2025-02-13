# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CarrierProposedAssignmentListParams"]


class CarrierProposedAssignmentListParams(TypedDict, total=False):
    active_time: Annotated[str, PropertyInfo(alias="activeTime")]
    """If specified, shows assignments that will be active at this time.

    Defaults to now, which would show current active assignments. In RFC 3339
    format. Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    driver_ids: Annotated[List[str], PropertyInfo(alias="driverIds")]
    """
    A filter on the data based on this comma-separated list of driver IDs and
    externalIds. Example: `driverIds=1234,5678,payroll:4841`
    """

    limit: int
    """The limit for how many objects will be in the response.

    Default and max for this value is 512 objects.
    """
