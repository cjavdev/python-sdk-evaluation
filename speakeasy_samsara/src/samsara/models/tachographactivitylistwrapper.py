"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .drivertinyresponse import DriverTinyResponse, DriverTinyResponseTypedDict
from .tachographactivity import TachographActivity, TachographActivityTypedDict
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class TachographActivityListWrapperTypedDict(TypedDict):
    activity: NotRequired[List[TachographActivityTypedDict]]
    r"""List of all driver tachograph activities in a specified time range."""
    driver: NotRequired[DriverTinyResponseTypedDict]
    r"""A minified driver object."""


class TachographActivityListWrapper(BaseModel):
    activity: Optional[List[TachographActivity]] = None
    r"""List of all driver tachograph activities in a specified time range."""

    driver: Optional[DriverTinyResponse] = None
    r"""A minified driver object."""
