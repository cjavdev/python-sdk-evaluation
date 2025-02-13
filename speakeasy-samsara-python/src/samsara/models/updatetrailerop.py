"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .trailersupdatetrailerbadrequesterrorresponsebody import (
    TrailersUpdateTrailerBadRequestErrorResponseBody,
    TrailersUpdateTrailerBadRequestErrorResponseBodyTypedDict,
)
from .trailersupdatetrailerrequestbody import (
    TrailersUpdateTrailerRequestBody,
    TrailersUpdateTrailerRequestBodyTypedDict,
)
from .trailersupdatetrailerresponsebody import (
    TrailersUpdateTrailerResponseBody,
    TrailersUpdateTrailerResponseBodyTypedDict,
)
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class UpdateTrailerRequestTypedDict(TypedDict):
    id: str
    r"""ID of the trailer. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the trailer."""
    trailers_update_trailer_request_body: TrailersUpdateTrailerRequestBodyTypedDict


class UpdateTrailerRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the trailer. Can be either unique Samsara ID or an [external ID](https://developers.samsara.com/docs/external-ids) for the trailer."""

    trailers_update_trailer_request_body: Annotated[
        TrailersUpdateTrailerRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


UpdateTrailerResponseTypedDict = TypeAliasType(
    "UpdateTrailerResponseTypedDict",
    Union[
        TrailersUpdateTrailerResponseBodyTypedDict,
        TrailersUpdateTrailerBadRequestErrorResponseBodyTypedDict,
    ],
)


UpdateTrailerResponse = TypeAliasType(
    "UpdateTrailerResponse",
    Union[
        TrailersUpdateTrailerResponseBody,
        TrailersUpdateTrailerBadRequestErrorResponseBody,
    ],
)
