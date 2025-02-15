"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .signatoryuserobjectresponsebody import (
    SignatoryUserObjectResponseBody,
    SignatoryUserObjectResponseBodyTypedDict,
)
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class AuthorSignatureObjectResponseBodyType(str, Enum):
    r"""Whether the DVIR was submitted by a driver or mechanic.  Valid values: `driver`, `mechanic`"""

    DRIVER = "driver"
    MECHANIC = "mechanic"


class AuthorSignatureObjectResponseBodyTypedDict(TypedDict):
    r"""An author signature for DVIRs with a signed time."""

    signatory_user: SignatoryUserObjectResponseBodyTypedDict
    r"""The user who signed the DVIR."""
    signed_at_time: str
    r"""The time when the DVIR was signed. UTC timestamp in RFC 3339 format."""
    type: AuthorSignatureObjectResponseBodyType
    r"""Whether the DVIR was submitted by a driver or mechanic.  Valid values: `driver`, `mechanic`"""


class AuthorSignatureObjectResponseBody(BaseModel):
    r"""An author signature for DVIRs with a signed time."""

    signatory_user: Annotated[
        SignatoryUserObjectResponseBody, pydantic.Field(alias="signatoryUser")
    ]
    r"""The user who signed the DVIR."""

    signed_at_time: Annotated[str, pydantic.Field(alias="signedAtTime")]
    r"""The time when the DVIR was signed. UTC timestamp in RFC 3339 format."""

    type: AuthorSignatureObjectResponseBodyType
    r"""Whether the DVIR was submitted by a driver or mechanic.  Valid values: `driver`, `mechanic`"""
