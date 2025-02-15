"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .livesharinglinksupdatelivesharinglinkbadrequesterrorresponsebody import (
    LiveSharingLinksUpdateLiveSharingLinkBadRequestErrorResponseBody,
    LiveSharingLinksUpdateLiveSharingLinkBadRequestErrorResponseBodyTypedDict,
)
from .livesharinglinksupdatelivesharinglinkrequestbody import (
    LiveSharingLinksUpdateLiveSharingLinkRequestBody,
    LiveSharingLinksUpdateLiveSharingLinkRequestBodyTypedDict,
)
from .livesharinglinksupdatelivesharinglinkresponsebody import (
    LiveSharingLinksUpdateLiveSharingLinkResponseBody,
    LiveSharingLinksUpdateLiveSharingLinkResponseBodyTypedDict,
)
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, QueryParamMetadata, RequestMetadata
from typing import Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class UpdateLiveSharingLinkRequestTypedDict(TypedDict):
    id: str
    r"""Unique identifier for the Live Sharing Link."""
    live_sharing_links_update_live_sharing_link_request_body: (
        LiveSharingLinksUpdateLiveSharingLinkRequestBodyTypedDict
    )


class UpdateLiveSharingLinkRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Unique identifier for the Live Sharing Link."""

    live_sharing_links_update_live_sharing_link_request_body: Annotated[
        LiveSharingLinksUpdateLiveSharingLinkRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


UpdateLiveSharingLinkResponseTypedDict = TypeAliasType(
    "UpdateLiveSharingLinkResponseTypedDict",
    Union[
        LiveSharingLinksUpdateLiveSharingLinkResponseBodyTypedDict,
        LiveSharingLinksUpdateLiveSharingLinkBadRequestErrorResponseBodyTypedDict,
    ],
)


UpdateLiveSharingLinkResponse = TypeAliasType(
    "UpdateLiveSharingLinkResponse",
    Union[
        LiveSharingLinksUpdateLiveSharingLinkResponseBody,
        LiveSharingLinksUpdateLiveSharingLinkBadRequestErrorResponseBody,
    ],
)
