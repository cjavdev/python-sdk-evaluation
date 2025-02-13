# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FuelPurchaseCreateParams", "TransactionPrice"]


class FuelPurchaseCreateParams(TypedDict, total=False):
    fuel_quantity_liters: Required[Annotated[str, PropertyInfo(alias="fuelQuantityLiters")]]
    """The amount of fuel purchased in liters."""

    transaction_location: Required[Annotated[str, PropertyInfo(alias="transactionLocation")]]
    """
    The full street address for the location of the fuel transaction, as it might be
    recognized by Google Maps. Ideal entries should be in accordance with the format
    used by the national postal service of the country concerned (example: 1 De Haro
    St, San Francisco, CA 94107, United States). Alternatively, exact
    latitude/longitude can be provided (example: 40.748441, -73.985664).
    """

    transaction_price: Required[Annotated[TransactionPrice, PropertyInfo(alias="transactionPrice")]]
    """
    The price of the fuel transaction in the currency of the country where the
    transaction occurred.
    """

    transaction_reference: Required[Annotated[str, PropertyInfo(alias="transactionReference")]]
    """The fuel transaction reference.

    This is the transaction identifier. For instance, this can be the Serial Number
    on the invoice.
    """

    transaction_time: Required[Annotated[str, PropertyInfo(alias="transactionTime")]]
    """The time of the fuel transaction in RFC 3339 format.

    Timezone must be specified. For example, 2022-07-13T14:20:50.52-07:00 is a time
    in Pacific Daylight Time.
    """

    ifta_fuel_type: Annotated[
        Literal[
            "Unspecified",
            "A55",
            "Biodiesel",
            "CompressedNaturalGas",
            "Diesel",
            "E85",
            "Electricity",
            "Ethanol",
            "Gasohol",
            "Gasoline",
            "Hydrogen",
            "LiquifiedNaturalGas",
            "M85",
            "Methanol",
            "Propane",
            "Other",
        ],
        PropertyInfo(alias="iftaFuelType"),
    ]
    """The type of fuel purchased supported by IFTA.

    Valid values: `Unspecified`, `A55`, `Biodiesel`, `CompressedNaturalGas`,
    `Diesel`, `E85`, `Electricity`, `Ethanol`, `Gasohol`, `Gasoline`, `Hydrogen`,
    `LiquifiedNaturalGas`, `M85`, `Methanol`, `Propane`, `Other`
    """

    vehicle_id: Annotated[str, PropertyInfo(alias="vehicleId")]
    """Samsara ID of the vehicle that purchased the fuel."""


class TransactionPrice(TypedDict, total=False):
    amount: Required[str]
    """The money amount."""

    currency: Required[Literal["usd", "gbp", "cad", "eur", "chf", "mxn"]]
    """The currency of money.

    This is a 3-letter ISO 4217 currency code. Valid values: `usd`, `gbp`, `cad`,
    `eur`, `chf`, `mxn`
    """
