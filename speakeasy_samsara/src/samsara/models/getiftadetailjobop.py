"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .iftagetiftadetailjobbadrequesterrorresponsebody import (
    IFTAGetIFTADetailJobBadRequestErrorResponseBody,
    IFTAGetIFTADetailJobBadRequestErrorResponseBodyTypedDict,
)
from .iftagetiftadetailjobresponsebody import (
    IFTAGetIFTADetailJobResponseBody,
    IFTAGetIFTADetailJobResponseBodyTypedDict,
)
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, PathParamMetadata
from typing import Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class GetIftaDetailJobRequestTypedDict(TypedDict):
    id: str
    r"""ID of the requested job."""


class GetIftaDetailJobRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the requested job."""


GetIftaDetailJobResponseTypedDict = TypeAliasType(
    "GetIftaDetailJobResponseTypedDict",
    Union[
        IFTAGetIFTADetailJobResponseBodyTypedDict,
        IFTAGetIFTADetailJobBadRequestErrorResponseBodyTypedDict,
    ],
)


GetIftaDetailJobResponse = TypeAliasType(
    "GetIftaDetailJobResponse",
    Union[
        IFTAGetIFTADetailJobResponseBody,
        IFTAGetIFTADetailJobBadRequestErrorResponseBody,
    ],
)
