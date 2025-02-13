# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DataPointRetrieveParams"]


class DataPointRetrieveParams(TypedDict, total=False):
    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    asset_ids: Annotated[List[str], PropertyInfo(alias="assetIds")]
    """A comma-separated list of industrial asset UUIDs.

    Example:
    `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`
    """

    data_input_ids: Annotated[List[str], PropertyInfo(alias="dataInputIds")]
    """A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678`"""

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
