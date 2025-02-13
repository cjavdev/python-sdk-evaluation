"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .patchtagrequest import PatchTagRequest, PatchTagRequestTypedDict
from .standarderrorresponse import StandardErrorResponse, StandardErrorResponseTypedDict
from .tagresponse import TagResponse, TagResponseTypedDict
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class PatchTagRequest1TypedDict(TypedDict):
    id: str
    r"""ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.name:ELD-exempt`."""
    patch_tag_request: PatchTagRequestTypedDict


class PatchTagRequest1(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the Tag. This can either be the Samsara-provided ID or an external ID. External IDs are customer-specified key-value pairs created in the POST or PATCH requests of this resource. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `crmId:abc123`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.name:ELD-exempt`."""

    patch_tag_request: Annotated[
        PatchTagRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


PatchTagResponseTypedDict = TypeAliasType(
    "PatchTagResponseTypedDict",
    Union[TagResponseTypedDict, StandardErrorResponseTypedDict],
)


PatchTagResponse = TypeAliasType(
    "PatchTagResponse", Union[TagResponse, StandardErrorResponse]
)
