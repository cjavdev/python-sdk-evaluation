"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .jobspatchjobbadrequesterrorresponsebody import (
    JobsPatchJobBadRequestErrorResponseBody,
    JobsPatchJobBadRequestErrorResponseBodyTypedDict,
)
from .jobspatchjobrequestbody import (
    JobsPatchJobRequestBody,
    JobsPatchJobRequestBodyTypedDict,
)
from .jobspatchjobresponsebody import (
    JobsPatchJobResponseBody,
    JobsPatchJobResponseBodyTypedDict,
)
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata, RequestMetadata
from typing import Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class PatchJobRequestTypedDict(TypedDict):
    id: str
    r"""A jobId or uuid in STRING format. JobId must be prefixed with `jobId:`(Examples: `\"8d218e6c-7a16-4f9f-90f7-cc1d93b9e596\"`, `\"jobId:98765\"`)."""
    jobs_patch_job_request_body: JobsPatchJobRequestBodyTypedDict


class PatchJobRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""A jobId or uuid in STRING format. JobId must be prefixed with `jobId:`(Examples: `\"8d218e6c-7a16-4f9f-90f7-cc1d93b9e596\"`, `\"jobId:98765\"`)."""

    jobs_patch_job_request_body: Annotated[
        JobsPatchJobRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


PatchJobResponseTypedDict = TypeAliasType(
    "PatchJobResponseTypedDict",
    Union[
        JobsPatchJobBadRequestErrorResponseBodyTypedDict,
        JobsPatchJobResponseBodyTypedDict,
    ],
)


PatchJobResponse = TypeAliasType(
    "PatchJobResponse",
    Union[JobsPatchJobBadRequestErrorResponseBody, JobsPatchJobResponseBody],
)
