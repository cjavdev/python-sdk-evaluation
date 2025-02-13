# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["JobDeleteParams"]


class JobDeleteParams(TypedDict, total=False):
    id: Required[str]
    """A jobId or uuid in STRING format.

    JobId must be prefixed with `jobId:`(Examples:
    `"8d218e6c-7a16-4f9f-90f7-cc1d93b9e596"`, `"jobId:98765"`).
    """
