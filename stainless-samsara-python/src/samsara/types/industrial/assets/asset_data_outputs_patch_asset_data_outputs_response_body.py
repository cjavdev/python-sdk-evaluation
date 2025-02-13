# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AssetDataOutputsPatchAssetDataOutputsResponseBody", "Data"]


class Data(BaseModel):
    id: str
    """The data output ID."""

    status_code: int = FieldInfo(alias="statusCode")
    """The status code of the request.

    200 indicates the request succeeded for this data output. 500 indicates an
    internal server error.
    """

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """If the request failed, this displays the error message."""


class AssetDataOutputsPatchAssetDataOutputsResponseBody(BaseModel):
    data: List[Data]
    """List of responses for each data output from the original request."""
