# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RunRetrievebycameraprogramParams"]


class RunRetrievebycameraprogramParams(TypedDict, total=False):
    camera_id: Required[int]

    program_id: Required[int]

    include: str
    """Include is a filter parameter. Accepts 'pass', 'reject' or 'no_read'."""
