"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class EntryType(str, Enum):
    r"""The type of entry for the asset.  Valid values: `tracked`, `untracked`"""

    TRACKED = "tracked"
    UNTRACKED = "untracked"


class FormsAssetObjectResponseBodyTypedDict(TypedDict):
    r"""Tracked or untracked (i.e. manually entered) asset object."""

    entry_type: EntryType
    r"""The type of entry for the asset.  Valid values: `tracked`, `untracked`"""
    id: NotRequired[str]
    r"""ID of a tracked asset. Included if 'entryType' is 'tracked'."""
    name: NotRequired[str]
    r"""Name of an untracked (i.e. manually entered) asset."""


class FormsAssetObjectResponseBody(BaseModel):
    r"""Tracked or untracked (i.e. manually entered) asset object."""

    entry_type: Annotated[EntryType, pydantic.Field(alias="entryType")]
    r"""The type of entry for the asset.  Valid values: `tracked`, `untracked`"""

    id: Optional[str] = None
    r"""ID of a tracked asset. Included if 'entryType' is 'tracked'."""

    name: Optional[str] = None
    r"""Name of an untracked (i.e. manually entered) asset."""
