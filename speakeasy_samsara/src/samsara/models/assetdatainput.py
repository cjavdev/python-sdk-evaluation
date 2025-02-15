"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .assetdatainput_lastpoint import (
    AssetDataInputLastPoint,
    AssetDataInputLastPointTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AssetDataInputTypedDict(TypedDict):
    data_group: NotRequired[str]
    r"""Name of the data group that the data input is associated with"""
    id: NotRequired[str]
    r"""ID of the data input"""
    last_point: NotRequired[AssetDataInputLastPointTypedDict]
    r"""The last reported point of a data input."""
    name: NotRequired[str]
    r"""Name of the data input"""
    units: NotRequired[str]
    r"""Units of data for this data input"""


class AssetDataInput(BaseModel):
    data_group: Annotated[Optional[str], pydantic.Field(alias="dataGroup")] = None
    r"""Name of the data group that the data input is associated with"""

    id: Optional[str] = None
    r"""ID of the data input"""

    last_point: Annotated[
        Optional[AssetDataInputLastPoint], pydantic.Field(alias="lastPoint")
    ] = None
    r"""The last reported point of a data input."""

    name: Optional[str] = None
    r"""Name of the data input"""

    units: Optional[str] = None
    r"""Units of data for this data input"""
