"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .contactresponse import ContactResponse, ContactResponseTypedDict
from .standarderrorresponse import StandardErrorResponse, StandardErrorResponseTypedDict
from typing import Union
from typing_extensions import TypeAliasType


CreateContactResponseTypedDict = TypeAliasType(
    "CreateContactResponseTypedDict",
    Union[ContactResponseTypedDict, StandardErrorResponseTypedDict],
)


CreateContactResponse = TypeAliasType(
    "CreateContactResponse", Union[ContactResponse, StandardErrorResponse]
)
