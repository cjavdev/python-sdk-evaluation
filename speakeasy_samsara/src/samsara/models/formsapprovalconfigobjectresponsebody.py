"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .formssingleapprovalconfigobjectresponsebody import (
    FormsSingleApprovalConfigObjectResponseBody,
    FormsSingleApprovalConfigObjectResponseBodyTypedDict,
)
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class FormsApprovalConfigObjectResponseBodyType(str, Enum):
    r"""Type of approval.  Valid values: `singleApproval`"""

    SINGLE_APPROVAL = "singleApproval"


class FormsApprovalConfigObjectResponseBodyTypedDict(TypedDict):
    r"""Form Template approval configuration object."""

    type: FormsApprovalConfigObjectResponseBodyType
    r"""Type of approval.  Valid values: `singleApproval`"""
    single_approval_config: NotRequired[
        FormsSingleApprovalConfigObjectResponseBodyTypedDict
    ]
    r"""Single approval configuration object."""


class FormsApprovalConfigObjectResponseBody(BaseModel):
    r"""Form Template approval configuration object."""

    type: FormsApprovalConfigObjectResponseBodyType
    r"""Type of approval.  Valid values: `singleApproval`"""

    single_approval_config: Annotated[
        Optional[FormsSingleApprovalConfigObjectResponseBody],
        pydantic.Field(alias="singleApprovalConfig"),
    ] = None
    r"""Single approval configuration object."""
