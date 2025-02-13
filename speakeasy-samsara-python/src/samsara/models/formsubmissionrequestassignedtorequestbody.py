"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from samsara.types import BaseModel
from typing_extensions import TypedDict


class FormSubmissionRequestAssignedToRequestBodyType(str, Enum):
    r"""Type of the form submission assignee.  Valid values: `driver`, `user`"""

    DRIVER = "driver"
    USER = "user"


class FormSubmissionRequestAssignedToRequestBodyTypedDict(TypedDict):
    r"""Form submission assignee update object"""

    id: str
    r"""ID of the form submission assignee."""
    type: FormSubmissionRequestAssignedToRequestBodyType
    r"""Type of the form submission assignee.  Valid values: `driver`, `user`"""


class FormSubmissionRequestAssignedToRequestBody(BaseModel):
    r"""Form submission assignee update object"""

    id: str
    r"""ID of the form submission assignee."""

    type: FormSubmissionRequestAssignedToRequestBodyType
    r"""Type of the form submission assignee.  Valid values: `driver`, `user`"""
