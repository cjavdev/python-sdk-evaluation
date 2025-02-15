"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .singleapprovalrequirementsobjectresponsebody import (
    SingleApprovalRequirementsObjectResponseBody,
    SingleApprovalRequirementsObjectResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class FormsSingleApprovalConfigObjectResponseBodyTypedDict(TypedDict):
    r"""Single approval configuration object."""

    allow_manual_approver_selection: bool
    r"""Indicates whether approver can be manually selected. True by default."""
    requirements: SingleApprovalRequirementsObjectResponseBodyTypedDict
    r"""Single approval requirements object."""


class FormsSingleApprovalConfigObjectResponseBody(BaseModel):
    r"""Single approval configuration object."""

    allow_manual_approver_selection: Annotated[
        bool, pydantic.Field(alias="allowManualApproverSelection")
    ]
    r"""Indicates whether approver can be manually selected. True by default."""

    requirements: SingleApprovalRequirementsObjectResponseBody
    r"""Single approval requirements object."""
