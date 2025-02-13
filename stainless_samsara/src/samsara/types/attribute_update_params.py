# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AttributeUpdateParams", "Entity"]


class AttributeUpdateParams(TypedDict, total=False):
    entity_type: Required[Annotated[Literal["driver", "asset"], PropertyInfo(alias="entityType")]]
    """Denotes the type of entity, driver or asset."""

    attribute_type: Annotated[Literal["string", "number"], PropertyInfo(alias="attributeType")]
    """Denotes the data type of the attribute's values.

    Valid values: `string`, `number`.
    """

    attribute_value_quantity: Annotated[Literal["single", "multi"], PropertyInfo(alias="attributeValueQuantity")]
    """
    Defines whether or not this attribute can be used on the same entity many times
    (with different values). Denotes the type of entity, driver or asset. Valid
    values: `driver`, `asset`.
    """

    entities: Iterable[Entity]
    """Entities that will be applied to this attribute"""

    name: str
    """Name"""

    number_values: Annotated[Iterable[float], PropertyInfo(alias="numberValues")]
    """Number values that can be associated with this attribute"""

    string_values: Annotated[List[str], PropertyInfo(alias="stringValues")]
    """String values that can be associated with this attribute"""


class Entity(TypedDict, total=False):
    entity_id: Annotated[str, PropertyInfo(alias="entityId")]
    """Entity id, based on the entity type."""

    external_ids: Annotated[Dict[str, str], PropertyInfo(alias="externalIds")]
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    number_values: Annotated[Iterable[float], PropertyInfo(alias="numberValues")]
    """Number values that can be associated with this attribute"""

    string_values: Annotated[List[str], PropertyInfo(alias="stringValues")]
    """String values that can be associated with this attribute"""
