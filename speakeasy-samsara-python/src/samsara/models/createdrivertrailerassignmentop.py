"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .trailerassignmentscreatedrivertrailerassignmentbadrequesterrorresponsebody import (
    TrailerAssignmentsCreateDriverTrailerAssignmentBadRequestErrorResponseBody,
    TrailerAssignmentsCreateDriverTrailerAssignmentBadRequestErrorResponseBodyTypedDict,
)
from .trailerassignmentscreatedrivertrailerassignmentresponsebody import (
    TrailerAssignmentsCreateDriverTrailerAssignmentResponseBody,
    TrailerAssignmentsCreateDriverTrailerAssignmentResponseBodyTypedDict,
)
from typing import Union
from typing_extensions import TypeAliasType


CreateDriverTrailerAssignmentResponseTypedDict = TypeAliasType(
    "CreateDriverTrailerAssignmentResponseTypedDict",
    Union[
        TrailerAssignmentsCreateDriverTrailerAssignmentResponseBodyTypedDict,
        TrailerAssignmentsCreateDriverTrailerAssignmentBadRequestErrorResponseBodyTypedDict,
    ],
)


CreateDriverTrailerAssignmentResponse = TypeAliasType(
    "CreateDriverTrailerAssignmentResponse",
    Union[
        TrailerAssignmentsCreateDriverTrailerAssignmentResponseBody,
        TrailerAssignmentsCreateDriverTrailerAssignmentBadRequestErrorResponseBody,
    ],
)
