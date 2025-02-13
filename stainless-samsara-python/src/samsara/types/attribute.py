# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Attribute", "Data", "DataEntity", "DataEntityValue", "DataValue"]


class DataEntityValue(BaseModel):
    id: Optional[str] = None
    """The samsara id of this value object."""

    string_value: Optional[str] = FieldInfo(alias="stringValue", default=None)
    """The human-readable string for this value."""


class DataEntity(BaseModel):
    entity_id: Optional[int] = FieldInfo(alias="entityId", default=None)

    external_ids: Optional[object] = FieldInfo(alias="externalIds", default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    name: Optional[str] = None

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """Number values that are associated with this attribute."""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """String values that are associated with this attribute."""

    values: Optional[List[DataEntityValue]] = None
    """Representation of values that includes ids."""


class DataValue(BaseModel):
    id: Optional[str] = None
    """The samsara id of this value object."""

    string_value: Optional[str] = FieldInfo(alias="stringValue", default=None)
    """The human-readable string for this value."""


class Data(BaseModel):
    entities: List[DataEntity]
    """Entities that this attribute is applied onto"""

    id: Optional[str] = None
    """The samsara id of the attribute object."""

    attribute_type: Optional[Literal["string", "number"]] = FieldInfo(alias="attributeType", default=None)
    """Denotes the data type of the attribute's values.

    Valid values: `string`, `number`.
    """

    attribute_value_quantity: Optional[Literal["single", "multi"]] = FieldInfo(
        alias="attributeValueQuantity", default=None
    )
    """
    Defines whether or not this attribute can be used on the same entity many times
    (with different values). Valid values: `single`, `multi`.
    """

    entity_type: Optional[Literal["driver", "asset"]] = FieldInfo(alias="entityType", default=None)
    """Denotes the type of entity, driver or asset. Valid values: `driver`, `asset`."""

    name: Optional[str] = None
    """Name of attribute."""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """Number values that can be associated with this attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """String values that can be associated with this attribute"""

    values: Optional[List[DataValue]] = None
    """Representation of values that includes ids."""


class Attribute(BaseModel):
    data: Optional[Data] = None
