"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .standarderrorresponse import StandardErrorResponse, StandardErrorResponseTypedDict
from .tagresponse import TagResponse, TagResponseTypedDict
from typing import Union
from typing_extensions import TypeAliasType


CreateTagResponseTypedDict = TypeAliasType(
    "CreateTagResponseTypedDict",
    Union[TagResponseTypedDict, StandardErrorResponseTypedDict],
)


CreateTagResponse = TypeAliasType(
    "CreateTagResponse", Union[TagResponse, StandardErrorResponse]
)
