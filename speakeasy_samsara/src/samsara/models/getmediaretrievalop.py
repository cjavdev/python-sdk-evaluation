"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .mediaretrievalgetmediaretrievalbadrequesterrorresponsebody import (
    MediaRetrievalGetMediaRetrievalBadRequestErrorResponseBody,
    MediaRetrievalGetMediaRetrievalBadRequestErrorResponseBodyTypedDict,
)
from .mediaretrievalgetmediaretrievalresponsebody import (
    MediaRetrievalGetMediaRetrievalResponseBody,
    MediaRetrievalGetMediaRetrievalResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata
from typing import Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class GetMediaRetrievalRequestTypedDict(TypedDict):
    retrieval_id: str
    r"""Retrieval ID associated with this media capture request. Examples: 2308cec4-82e0-46f1-8b3c-a3592e5cc21e"""


class GetMediaRetrievalRequest(BaseModel):
    retrieval_id: Annotated[
        str,
        pydantic.Field(alias="retrievalId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Retrieval ID associated with this media capture request. Examples: 2308cec4-82e0-46f1-8b3c-a3592e5cc21e"""


GetMediaRetrievalResponseTypedDict = TypeAliasType(
    "GetMediaRetrievalResponseTypedDict",
    Union[
        MediaRetrievalGetMediaRetrievalResponseBodyTypedDict,
        MediaRetrievalGetMediaRetrievalBadRequestErrorResponseBodyTypedDict,
    ],
)


GetMediaRetrievalResponse = TypeAliasType(
    "GetMediaRetrievalResponse",
    Union[
        MediaRetrievalGetMediaRetrievalResponseBody,
        MediaRetrievalGetMediaRetrievalBadRequestErrorResponseBody,
    ],
)
