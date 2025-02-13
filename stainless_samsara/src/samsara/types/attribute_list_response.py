# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AttributeListResponse", "Data", "DataValue", "Pagination"]


class DataValue(BaseModel):
    id: Optional[str] = None
    """The samsara id of this value object."""

    string_value: Optional[str] = FieldInfo(alias="stringValue", default=None)
    """The human-readable string for this value."""


class Data(BaseModel):
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


class Pagination(BaseModel):
    end_cursor: str = FieldInfo(alias="endCursor")
    """Cursor identifier representing the last element in the response.

    This value should be used in conjunction with a subsequent request's 'after'
    query parameter. This may be an empty string if there are no more pages left to
    view.
    """

    has_next_page: bool = FieldInfo(alias="hasNextPage")
    """
    True if there are more pages of results immediately available after this
    endCursor.
    """


class AttributeListResponse(BaseModel):
    data: Optional[List[Data]] = None

    pagination: Optional[Pagination] = None
    """Pagination parameters."""
