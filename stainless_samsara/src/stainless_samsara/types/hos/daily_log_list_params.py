# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DailyLogListParams"]


class DailyLogListParams(TypedDict, total=False):
    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    driver_activation_status: Annotated[Literal["active", "deactivated"], PropertyInfo(alias="driverActivationStatus")]
    """
    If value is `deactivated`, only drivers that are deactivated will appear in the
    response. This parameter will default to `active` if not provided (fetching only
    active drivers). Valid values: `active`, `deactivated`
    """

    driver_ids: Annotated[List[str], PropertyInfo(alias="driverIds")]
    """
    A filter on the data based on this comma-separated list of driver IDs and
    externalIds. Example: `driverIds=1234,5678,payroll:4841`
    """

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """An end date in YYYY-MM-DD.

    This is a date only without an associated time. Must be greater than or equal to
    the start date. Example: `2019-07-21`. This is a required field
    """

    expand: Literal["vehicle"]
    """Expands the specified value(s) in the response object.

    Expansion populates additional fields in an object, if supported. Unsupported
    fields are ignored. To expand multiple fields, input a comma-separated list.

    Valid value: `vehicle` Valid values: `vehicle`
    """

    parent_tag_ids: Annotated[str, PropertyInfo(alias="parentTagIds")]
    """
    A filter on the data based on this comma-separated list of parent tag IDs, for
    use by orgs with tag hierarchies. Specifying a parent tag will implicitly
    include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    """

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """A start date in YYYY-MM-DD.

    This is a date only without an associated time. Example: `2019-06-13`. This is a
    required field
    """

    tag_ids: Annotated[str, PropertyInfo(alias="tagIds")]
    """A filter on the data based on this comma-separated list of tag IDs.

    Example: `tagIds=1234,5678`
    """
