# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConfigurationListParams"]


class ConfigurationListParams(TypedDict, total=False):
    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    ids: List[str]
    """Filter by the IDs. Returns all if no ids are provided."""

    include_external_ids: Annotated[bool, PropertyInfo(alias="includeExternalIds")]
    """
    Optional boolean indicating whether to return external IDs on supported entities
    """

    status: Literal["all", "enabled", "disabled"]
    """The status of the alert configuration.

    Valid values: `all`, `enabled`, `disabled`
    """
