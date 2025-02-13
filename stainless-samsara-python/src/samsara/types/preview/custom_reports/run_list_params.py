# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    custom_report_ids: Annotated[List[str], PropertyInfo(alias="customReportIds")]
    """Required array of custom report IDs for the custom report runs wanted.

    Only one of customReportIds or ids is allowed.
    """

    ids: List[str]
    """Required array of custom report run IDs to fetch.

    Only one of ids or customReportIds is allowed.
    """
