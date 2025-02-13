# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["FormSubmissionListParams"]


class FormSubmissionListParams(TypedDict, total=False):
    ids: Required[List[str]]
    """A comma-separated list containing up to 100 form submission IDs to filter on.

    Can be either a unique Samsara ID or an
    [external ID](https://developers.samsara.com/docs/external-ids) for the form
    submission.
    """

    include: List[str]
    """
    A comma-separated list of strings indicating whether to return additional
    information. Valid values: `externalIds`, `fieldLabels`
    """
