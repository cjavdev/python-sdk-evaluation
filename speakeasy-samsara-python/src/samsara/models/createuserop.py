"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .standarderrorresponse import StandardErrorResponse, StandardErrorResponseTypedDict
from .userresponse import UserResponse, UserResponseTypedDict
from typing import Union
from typing_extensions import TypeAliasType


CreateUserResponseTypedDict = TypeAliasType(
    "CreateUserResponseTypedDict",
    Union[UserResponseTypedDict, StandardErrorResponseTypedDict],
)


CreateUserResponse = TypeAliasType(
    "CreateUserResponse", Union[UserResponse, StandardErrorResponse]
)
