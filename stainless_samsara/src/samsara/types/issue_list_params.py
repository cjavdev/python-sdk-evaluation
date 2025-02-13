# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["IssueListParams"]


class IssueListParams(TypedDict, total=False):
    ids: Required[List[str]]
    """A comma-separated list containing up to 100 issue IDs to filter on.

    Can be either a unique Samsara ID or an
    [external ID](https://developers.samsara.com/docs/external-ids) for the issue.
    """

    include: List[str]
    """A comma separated list of additional fields to include on requested objects.

    Valid values: `externalIds`
    """
