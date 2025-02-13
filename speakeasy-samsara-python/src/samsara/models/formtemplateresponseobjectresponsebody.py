"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .formsapprovalconfigobjectresponsebody import (
    FormsApprovalConfigObjectResponseBody,
    FormsApprovalConfigObjectResponseBodyTypedDict,
)
from .formsfielddefinitionobjectresponsebody import (
    FormsFieldDefinitionObjectResponseBody,
    FormsFieldDefinitionObjectResponseBodyTypedDict,
)
from .formspolymorphicuserobjectresponsebody import (
    FormsPolymorphicUserObjectResponseBody,
    FormsPolymorphicUserObjectResponseBodyTypedDict,
)
from .formtemplatesectionobjectresponsebody import (
    FormTemplateSectionObjectResponseBody,
    FormTemplateSectionObjectResponseBodyTypedDict,
)
from datetime import datetime
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class FormTemplateResponseObjectResponseBodyTypedDict(TypedDict):
    r"""Form Template response object."""

    created_at_time: datetime
    r"""Creation time of the form template. UTC timestamp in RFC 3339 format."""
    created_by: FormsPolymorphicUserObjectResponseBodyTypedDict
    r"""User or driver object."""
    description: str
    r"""Description of the form template."""
    fields: List[FormsFieldDefinitionObjectResponseBodyTypedDict]
    r"""List of fields in the form template."""
    id: str
    r"""Unique identifier of the form template."""
    revision_id: str
    r"""Unique identifier of the form template revision."""
    sections: List[FormTemplateSectionObjectResponseBodyTypedDict]
    r"""List of sections in the form template."""
    title: str
    r"""Title of the form template."""
    updated_at_time: datetime
    r"""Update time of the form template. UTC timestamp in RFC 3339 format."""
    updated_by: FormsPolymorphicUserObjectResponseBodyTypedDict
    r"""User or driver object."""
    approval_config: NotRequired[FormsApprovalConfigObjectResponseBodyTypedDict]
    r"""Form Template approval configuration object."""


class FormTemplateResponseObjectResponseBody(BaseModel):
    r"""Form Template response object."""

    created_at_time: Annotated[datetime, pydantic.Field(alias="createdAtTime")]
    r"""Creation time of the form template. UTC timestamp in RFC 3339 format."""

    created_by: Annotated[
        FormsPolymorphicUserObjectResponseBody, pydantic.Field(alias="createdBy")
    ]
    r"""User or driver object."""

    description: str
    r"""Description of the form template."""

    fields: List[FormsFieldDefinitionObjectResponseBody]
    r"""List of fields in the form template."""

    id: str
    r"""Unique identifier of the form template."""

    revision_id: Annotated[str, pydantic.Field(alias="revisionId")]
    r"""Unique identifier of the form template revision."""

    sections: List[FormTemplateSectionObjectResponseBody]
    r"""List of sections in the form template."""

    title: str
    r"""Title of the form template."""

    updated_at_time: Annotated[datetime, pydantic.Field(alias="updatedAtTime")]
    r"""Update time of the form template. UTC timestamp in RFC 3339 format."""

    updated_by: Annotated[
        FormsPolymorphicUserObjectResponseBody, pydantic.Field(alias="updatedBy")
    ]
    r"""User or driver object."""

    approval_config: Annotated[
        Optional[FormsApprovalConfigObjectResponseBody],
        pydantic.Field(alias="approvalConfig"),
    ] = None
    r"""Form Template approval configuration object."""
