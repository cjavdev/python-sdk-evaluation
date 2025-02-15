"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class AssetsInputsAuxInputResponseBodyTypedDict(TypedDict):
    r"""Auxiliary input metadata"""

    name: str
    r"""Name of the auxiliary input"""


class AssetsInputsAuxInputResponseBody(BaseModel):
    r"""Auxiliary input metadata"""

    name: str
    r"""Name of the auxiliary input"""
