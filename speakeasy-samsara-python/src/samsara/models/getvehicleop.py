"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .standarderrorresponse import StandardErrorResponse, StandardErrorResponseTypedDict
from .vehicleresponse import VehicleResponse, VehicleResponseTypedDict
from samsara.types import BaseModel
from samsara.utils import FieldMetadata, PathParamMetadata
from typing import Union
from typing_extensions import Annotated, TypeAliasType, TypedDict


class GetVehicleRequestTypedDict(TypedDict):
    id: str
    r"""ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource, or automatically populated by fields on the vehicle. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `maintenanceId:250020`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.vin:1HGBH41JXMN109186`."""


class GetVehicleRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""ID of the vehicle. This can either be the Samsara-specified ID, or an external ID. External IDs are customer specified key-value pairs created in the POST or PATCH requests of this resource, or automatically populated by fields on the vehicle. To specify an external ID as part of a path parameter, use the following format: `key:value`. For example, `maintenanceId:250020`. Automatically populated external IDs are prefixed with `samsara.`. For example, `samsara.vin:1HGBH41JXMN109186`."""


GetVehicleResponseTypedDict = TypeAliasType(
    "GetVehicleResponseTypedDict",
    Union[VehicleResponseTypedDict, StandardErrorResponseTypedDict],
)


GetVehicleResponse = TypeAliasType(
    "GetVehicleResponse", Union[VehicleResponse, StandardErrorResponse]
)
