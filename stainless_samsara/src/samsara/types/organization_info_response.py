# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OrganizationInfoResponse", "Data", "DataCarrierSettings"]


class DataCarrierSettings(BaseModel):
    carrier_name: Optional[str] = FieldInfo(alias="carrierName", default=None)
    """Carrier for a given organization."""

    dot_number: Optional[int] = FieldInfo(alias="dotNumber", default=None)
    """Carrier US DOT Number for the organization."""

    main_office_address: Optional[str] = FieldInfo(alias="mainOfficeAddress", default=None)
    """Main office address for a given organization."""


class Data(BaseModel):
    id: Optional[str] = None
    """ID of the organization."""

    carrier_settings: Optional[DataCarrierSettings] = FieldInfo(alias="carrierSettings", default=None)
    """Carrier for a given organization."""

    name: Optional[str] = None
    """Name of organization."""


class OrganizationInfoResponse(BaseModel):
    data: Optional[Data] = None
    """Information about your organization."""
