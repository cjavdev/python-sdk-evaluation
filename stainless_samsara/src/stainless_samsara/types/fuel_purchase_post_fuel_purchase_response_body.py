# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["FuelPurchasePostFuelPurchaseResponseBody", "Data"]


class Data(BaseModel):
    uuid: str
    """Universally unique identifier for the fuel purchase."""


class FuelPurchasePostFuelPurchaseResponseBody(BaseModel):
    data: Data
    """Response after successfully adding a Fuel Purchase transaction"""
