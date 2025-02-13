"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .drivertinyresponse import DriverTinyResponse, DriverTinyResponseTypedDict
from .tachographdriverfile import TachographDriverFile, TachographDriverFileTypedDict
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class TachographDriverFileListWrapperTypedDict(TypedDict):
    driver: NotRequired[DriverTinyResponseTypedDict]
    r"""A minified driver object."""
    files: NotRequired[List[TachographDriverFileTypedDict]]
    r"""List of all tachograph driver files in a specified time range."""


class TachographDriverFileListWrapper(BaseModel):
    driver: Optional[DriverTinyResponse] = None
    r"""A minified driver object."""

    files: Optional[List[TachographDriverFile]] = None
    r"""List of all tachograph driver files in a specified time range."""
