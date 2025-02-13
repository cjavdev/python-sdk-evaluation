# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TagUpdateParams"]


class TagUpdateParams(TypedDict, total=False):
    addresses: List[str]
    """The addresses that belong to this tag."""

    assets: List[str]
    """The trailers, unpowered, and powered assets that belong to this tag."""

    drivers: List[str]
    """The drivers that belong to this tag."""

    machines: List[str]
    """The machines that belong to this tag."""

    name: str
    """Name of this tag."""

    parent_tag_id: Annotated[str, PropertyInfo(alias="parentTagId")]
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """

    sensors: List[str]
    """The sensors that belong to this tag."""

    vehicles: List[str]
    """The vehicles that belong to this tag."""
