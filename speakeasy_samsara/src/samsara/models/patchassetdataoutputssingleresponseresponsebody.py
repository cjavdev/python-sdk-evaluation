"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PatchAssetDataOutputsSingleResponseResponseBodyTypedDict(TypedDict):
    r"""A response that corresponds to an element in the original request body."""

    id: str
    r"""The data output ID."""
    status_code: int
    r"""The status code of the request. 200 indicates the request succeeded for this data output. 500 indicates an internal server error."""
    error_message: NotRequired[str]
    r"""If the request failed, this displays the error message."""


class PatchAssetDataOutputsSingleResponseResponseBody(BaseModel):
    r"""A response that corresponds to an element in the original request body."""

    id: str
    r"""The data output ID."""

    status_code: Annotated[int, pydantic.Field(alias="statusCode")]
    r"""The status code of the request. 200 indicates the request succeeded for this data output. 500 indicates an internal server error."""

    error_message: Annotated[Optional[str], pydantic.Field(alias="errorMessage")] = None
    r"""If the request failed, this displays the error message."""
