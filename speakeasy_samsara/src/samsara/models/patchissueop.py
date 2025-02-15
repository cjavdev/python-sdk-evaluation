"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .issuespatchissuebadrequesterrorresponsebody import (
    IssuesPatchIssueBadRequestErrorResponseBody,
    IssuesPatchIssueBadRequestErrorResponseBodyTypedDict,
)
from .issuespatchissueresponsebody import (
    IssuesPatchIssueResponseBody,
    IssuesPatchIssueResponseBodyTypedDict,
)
from typing import Union
from typing_extensions import TypeAliasType


PatchIssueResponseTypedDict = TypeAliasType(
    "PatchIssueResponseTypedDict",
    Union[
        IssuesPatchIssueResponseBodyTypedDict,
        IssuesPatchIssueBadRequestErrorResponseBodyTypedDict,
    ],
)


PatchIssueResponse = TypeAliasType(
    "PatchIssueResponse",
    Union[IssuesPatchIssueResponseBody, IssuesPatchIssueBadRequestErrorResponseBody],
)
