# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AttributeRetrieveParams"]


class AttributeRetrieveParams(TypedDict, total=False):
    entity_type: Required[Annotated[Literal["driver", "asset"], PropertyInfo(alias="entityType")]]
    """Denotes the type of entity, driver or asset."""
