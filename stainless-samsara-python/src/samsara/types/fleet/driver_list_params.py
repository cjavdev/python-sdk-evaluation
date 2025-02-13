# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DriverListParams"]


class DriverListParams(TypedDict, total=False):
    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    attribute_value_ids: Annotated[List[str], PropertyInfo(alias="attributeValueIds")]
    """A filter on the data based on this comma-separated list of attribute value IDs.

    Only entities associated with ALL of the referenced values will be returned
    (i.e. the intersection of the sets of entities with each value). Example:
    `attributeValueIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    """

    created_after_time: Annotated[str, PropertyInfo(alias="createdAfterTime")]
    """
    A filter on data to have a created at time after or equal to this specified time
    in RFC 3339 format. Millisecond precision and timezones are supported.
    (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """

    driver_activation_status: Annotated[Literal["active", "deactivated"], PropertyInfo(alias="driverActivationStatus")]
    """
    If value is `deactivated`, only drivers that are deactivated will appear in the
    response. This parameter will default to `active` if not provided (fetching only
    active drivers).
    """

    limit: int
    """The limit for how many objects will be in the response.

    Default and max for this value is 512 objects.
    """

    parent_tag_ids: Annotated[List[str], PropertyInfo(alias="parentTagIds")]
    """
    A filter on the data based on this comma-separated list of parent tag IDs, for
    use by orgs with tag hierarchies. Specifying a parent tag will implicitly
    include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    """

    tag_ids: Annotated[List[str], PropertyInfo(alias="tagIds")]
    """A filter on the data based on this comma-separated list of tag IDs.

    Example: `tagIds=1234,5678`
    """

    updated_after_time: Annotated[str, PropertyInfo(alias="updatedAfterTime")]
    """
    A filter on data to have an updated at time after or equal to this specified
    time in RFC 3339 format. Millisecond precision and timezones are supported.
    (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """
