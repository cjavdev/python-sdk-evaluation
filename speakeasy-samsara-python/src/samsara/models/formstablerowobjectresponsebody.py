"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .formstablecellobjectresponsebody import (
    FormsTableCellObjectResponseBody,
    FormsTableCellObjectResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class FormsTableRowObjectResponseBodyTypedDict(TypedDict):
    r"""Defines a row in a table form input field."""

    cells: List[FormsTableCellObjectResponseBodyTypedDict]
    r"""List of cells in the row."""
    id: str
    r"""Unique identifier for the row."""


class FormsTableRowObjectResponseBody(BaseModel):
    r"""Defines a row in a table form input field."""

    cells: List[FormsTableCellObjectResponseBody]
    r"""List of cells in the row."""

    id: str
    r"""Unique identifier for the row."""
