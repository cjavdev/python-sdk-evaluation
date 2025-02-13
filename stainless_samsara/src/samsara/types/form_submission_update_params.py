# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FormSubmissionUpdateParams", "AssignedTo"]


class FormSubmissionUpdateParams(TypedDict, total=False):
    id: Required[str]
    """ID of the form submission."""

    assigned_to: Annotated[AssignedTo, PropertyInfo(alias="assignedTo")]
    """Form submission assignee update object"""

    due_at_time: Annotated[Union[str, datetime], PropertyInfo(alias="dueAtTime", format="iso8601")]
    """Due date of the form submission. UTC timestamp in RFC 3339 format."""

    status: Literal["toDo", "dismissed"]
    """Status of the form submission. Valid values: `toDo`, `dismissed`"""

    title: str
    """Title of the form submission."""


class AssignedTo(TypedDict, total=False):
    id: Required[str]
    """ID of the form submission assignee."""

    type: Required[Literal["driver"]]
    """Type of the form submission assignee. Valid values: `driver`"""
