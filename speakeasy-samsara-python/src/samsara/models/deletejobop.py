"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .jobsdeletejobbadrequesterrorresponsebody import (
    JobsDeleteJobBadRequestErrorResponseBody,
    JobsDeleteJobBadRequestErrorResponseBodyTypedDict,
)
from .jobsdeletejobresponsebody import (
    JobsDeleteJobResponseBody,
    JobsDeleteJobResponseBodyTypedDict,
)
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata
from typing import Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class DeleteJobRequestTypedDict(TypedDict):
    id: str
    r"""A jobId or uuid in STRING format. JobId must be prefixed with `jobId:`(Examples: `\"8d218e6c-7a16-4f9f-90f7-cc1d93b9e596\"`, `\"jobId:98765\"`)."""


class DeleteJobRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""A jobId or uuid in STRING format. JobId must be prefixed with `jobId:`(Examples: `\"8d218e6c-7a16-4f9f-90f7-cc1d93b9e596\"`, `\"jobId:98765\"`)."""


DeleteJobResponseTypedDict = TypeAliasType(
    "DeleteJobResponseTypedDict",
    Union[
        JobsDeleteJobResponseBodyTypedDict,
        JobsDeleteJobBadRequestErrorResponseBodyTypedDict,
    ],
)


DeleteJobResponse = TypeAliasType(
    "DeleteJobResponse",
    Union[JobsDeleteJobResponseBody, JobsDeleteJobBadRequestErrorResponseBody],
)
