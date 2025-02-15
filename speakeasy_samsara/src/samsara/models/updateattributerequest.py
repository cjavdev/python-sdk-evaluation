"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createattributerequest_entities import (
    CreateAttributeRequestEntities,
    CreateAttributeRequestEntitiesTypedDict,
)
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateAttributeRequestAttributeType(str, Enum):
    r"""Denotes the data type of the attribute's values. Valid values: `string`, `number`."""

    STRING = "string"
    NUMBER = "number"


class UpdateAttributeRequestAttributeValueQuantity(str, Enum):
    r"""Defines whether or not this attribute can be used on the same entity many times (with different values). Denotes the type of entity, driver or asset. Valid values: `driver`, `asset`."""

    SINGLE = "single"
    MULTI = "multi"


class UpdateAttributeRequestEntityType(str, Enum):
    r"""Denotes the type of entity, driver or asset."""

    DRIVER = "driver"
    ASSET = "asset"


class UpdateAttributeRequestTypedDict(TypedDict):
    r"""A request body to update an Attribute."""

    entity_type: UpdateAttributeRequestEntityType
    r"""Denotes the type of entity, driver or asset."""
    attribute_type: NotRequired[UpdateAttributeRequestAttributeType]
    r"""Denotes the data type of the attribute's values. Valid values: `string`, `number`."""
    attribute_value_quantity: NotRequired[UpdateAttributeRequestAttributeValueQuantity]
    r"""Defines whether or not this attribute can be used on the same entity many times (with different values). Denotes the type of entity, driver or asset. Valid values: `driver`, `asset`."""
    entities: NotRequired[List[CreateAttributeRequestEntitiesTypedDict]]
    r"""Entities that will be applied to this attribute"""
    name: NotRequired[str]
    r"""Name"""
    number_values: NotRequired[List[float]]
    r"""Number values that can be associated with this attribute"""
    string_values: NotRequired[List[str]]
    r"""String values that can be associated with this attribute"""


class UpdateAttributeRequest(BaseModel):
    r"""A request body to update an Attribute."""

    entity_type: Annotated[
        UpdateAttributeRequestEntityType, pydantic.Field(alias="entityType")
    ]
    r"""Denotes the type of entity, driver or asset."""

    attribute_type: Annotated[
        Optional[UpdateAttributeRequestAttributeType],
        pydantic.Field(alias="attributeType"),
    ] = UpdateAttributeRequestAttributeType.STRING
    r"""Denotes the data type of the attribute's values. Valid values: `string`, `number`."""

    attribute_value_quantity: Annotated[
        Optional[UpdateAttributeRequestAttributeValueQuantity],
        pydantic.Field(alias="attributeValueQuantity"),
    ] = UpdateAttributeRequestAttributeValueQuantity.MULTI
    r"""Defines whether or not this attribute can be used on the same entity many times (with different values). Denotes the type of entity, driver or asset. Valid values: `driver`, `asset`."""

    entities: Optional[List[CreateAttributeRequestEntities]] = None
    r"""Entities that will be applied to this attribute"""

    name: Optional[str] = None
    r"""Name"""

    number_values: Annotated[
        Optional[List[float]], pydantic.Field(alias="numberValues")
    ] = None
    r"""Number values that can be associated with this attribute"""

    string_values: Annotated[
        Optional[List[str]], pydantic.Field(alias="stringValues")
    ] = None
    r"""String values that can be associated with this attribute"""
