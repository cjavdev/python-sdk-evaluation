"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .assetdatainput import AssetDataInput, AssetDataInputTypedDict
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AssetDataOutputTypedDict(TypedDict):
    data_group: NotRequired[str]
    r"""Name of the data group that the data output is associated with"""
    data_input: NotRequired[AssetDataInputTypedDict]
    device_id: NotRequired[str]
    r"""ID of the device that the data output is configured on"""
    id: NotRequired[str]
    r"""ID of the data output"""
    name: NotRequired[str]
    r"""Name of the data output"""


class AssetDataOutput(BaseModel):
    data_group: Annotated[Optional[str], pydantic.Field(alias="dataGroup")] = None
    r"""Name of the data group that the data output is associated with"""

    data_input: Annotated[
        Optional[AssetDataInput], pydantic.Field(alias="dataInput")
    ] = None

    device_id: Annotated[Optional[str], pydantic.Field(alias="deviceId")] = None
    r"""ID of the device that the data output is configured on"""

    id: Optional[str] = None
    r"""ID of the data output"""

    name: Optional[str] = None
    r"""Name of the data output"""
