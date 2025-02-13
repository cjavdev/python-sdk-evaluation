# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LiveShareUpdateParams"]


class LiveShareUpdateParams(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the Live Sharing Link."""

    name: Required[str]
    """Name of the Live Sharing Link."""

    description: str
    """
    Description for the Live Sharing Link (not applicable for 'assetsOnRoute' type).
    """

    expires_at_time: Annotated[str, PropertyInfo(alias="expiresAtTime")]
    """Date that this link expires in RFC 3339 format.

    Can't be set in the past. If not provided then link will never expire.
    """
