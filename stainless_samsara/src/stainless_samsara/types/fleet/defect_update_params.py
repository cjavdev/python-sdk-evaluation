# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DefectUpdateParams", "ResolvedBy"]


class DefectUpdateParams(TypedDict, total=False):
    is_resolved: Annotated[bool, PropertyInfo(alias="isResolved")]
    """Resolves the defect. Must be `true`."""

    mechanic_notes: Annotated[str, PropertyInfo(alias="mechanicNotes")]
    """The mechanics notes on the defect."""

    resolved_at_time: Annotated[str, PropertyInfo(alias="resolvedAtTime")]
    """Time when defect was resolved.

    Defaults to now if not provided. UTC timestamp in RFC 3339 format. Example:
    `2020-01-27T07:06:25Z`.
    """

    resolved_by: Annotated[ResolvedBy, PropertyInfo(alias="resolvedBy")]
    """Information about the user who is resolving a defect."""


class ResolvedBy(TypedDict, total=False):
    id: Required[str]
    """The Id of user who is resolving the defect."""

    type: Required[Literal["mechanic"]]
    """The type of user who is resolving the defect. Must be "mechanic"."""
