# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IssueUpdateParams", "AssignedTo"]


class IssueUpdateParams(TypedDict, total=False):
    id: Required[str]
    """ID of the issue.

    Can be either a unique Samsara ID or an
    [external ID](https://developers.samsara.com/docs/external-ids) for the issue.
    """

    assigned_to: Annotated[AssignedTo, PropertyInfo(alias="assignedTo")]
    """Issue assignee update object"""

    due_date: Annotated[Union[str, datetime], PropertyInfo(alias="dueDate", format="iso8601")]
    """Due date of the issue. UTC timestamp in RFC 3339 format."""

    external_ids: Annotated[Dict[str, str], PropertyInfo(alias="externalIds")]
    """A map of external ids"""

    status: Literal["open", "inProgress", "resolved", "dismissed"]
    """Status of the issue.

    Valid values: `open`, `inProgress`, `resolved`, `dismissed`
    """


class AssignedTo(TypedDict, total=False):
    id: Required[str]
    """ID of the issue assignee."""

    type: Required[Literal["user"]]
    """Type of the issue assignee. Valid values: `user`"""
