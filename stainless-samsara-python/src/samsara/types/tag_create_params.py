# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TagCreateParams"]


class TagCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of this tag."""

    addresses: List[str]
    """The addresses that belong to this tag."""

    assets: List[str]
    """The trailers, unpowered, and powered assets that belong to this tag."""

    drivers: List[str]
    """The drivers that belong to this tag."""

    external_ids: Annotated[Dict[str, str], PropertyInfo(alias="externalIds")]
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    machines: List[str]
    """The machines that belong to this tag."""

    parent_tag_id: Annotated[str, PropertyInfo(alias="parentTagId")]
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """

    sensors: List[str]
    """The sensors that belong to this tag."""

    vehicles: List[str]
    """The vehicles that belong to this tag."""
