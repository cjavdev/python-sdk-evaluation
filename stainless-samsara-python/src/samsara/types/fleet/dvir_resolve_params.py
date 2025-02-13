# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DvirResolveParams"]


class DvirResolveParams(TypedDict, total=False):
    author_id: Required[Annotated[str, PropertyInfo(alias="authorId")]]
    """The user who is resolving the dvir."""

    is_resolved: Required[Annotated[bool, PropertyInfo(alias="isResolved")]]
    """Resolves the DVIR. Must be `true`."""

    mechanic_notes: Annotated[str, PropertyInfo(alias="mechanicNotes")]
    """The mechanics notes on the DVIR."""

    signed_at_time: Annotated[str, PropertyInfo(alias="signedAtTime")]
    """Time when user signed this DVIR.

    Defaults to now. UTC timestamp in RFC 3339 format. Example:
    `2020-01-27T07:06:25Z`.
    """
