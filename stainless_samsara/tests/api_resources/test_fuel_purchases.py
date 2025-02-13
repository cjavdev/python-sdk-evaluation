# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import FuelPurchasePostFuelPurchaseResponseBody

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFuelPurchases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        fuel_purchase = client.fuel_purchases.create(
            fuel_quantity_liters="676.8",
            transaction_location="350 Rhode Island St, San Francisco, CA 94103",
            transaction_price={
                "amount": "640.2",
                "currency": "usd",
            },
            transaction_reference="5454534",
            transaction_time="2022-07-13T14:20:50.52-07:00",
        )
        assert_matches_type(FuelPurchasePostFuelPurchaseResponseBody, fuel_purchase, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        fuel_purchase = client.fuel_purchases.create(
            fuel_quantity_liters="676.8",
            transaction_location="350 Rhode Island St, San Francisco, CA 94103",
            transaction_price={
                "amount": "640.2",
                "currency": "usd",
            },
            transaction_reference="5454534",
            transaction_time="2022-07-13T14:20:50.52-07:00",
            ifta_fuel_type="Unspecified",
            vehicle_id="281474900488527",
        )
        assert_matches_type(FuelPurchasePostFuelPurchaseResponseBody, fuel_purchase, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.fuel_purchases.with_raw_response.create(
            fuel_quantity_liters="676.8",
            transaction_location="350 Rhode Island St, San Francisco, CA 94103",
            transaction_price={
                "amount": "640.2",
                "currency": "usd",
            },
            transaction_reference="5454534",
            transaction_time="2022-07-13T14:20:50.52-07:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fuel_purchase = response.parse()
        assert_matches_type(FuelPurchasePostFuelPurchaseResponseBody, fuel_purchase, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.fuel_purchases.with_streaming_response.create(
            fuel_quantity_liters="676.8",
            transaction_location="350 Rhode Island St, San Francisco, CA 94103",
            transaction_price={
                "amount": "640.2",
                "currency": "usd",
            },
            transaction_reference="5454534",
            transaction_time="2022-07-13T14:20:50.52-07:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fuel_purchase = response.parse()
            assert_matches_type(FuelPurchasePostFuelPurchaseResponseBody, fuel_purchase, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFuelPurchases:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        fuel_purchase = await async_client.fuel_purchases.create(
            fuel_quantity_liters="676.8",
            transaction_location="350 Rhode Island St, San Francisco, CA 94103",
            transaction_price={
                "amount": "640.2",
                "currency": "usd",
            },
            transaction_reference="5454534",
            transaction_time="2022-07-13T14:20:50.52-07:00",
        )
        assert_matches_type(FuelPurchasePostFuelPurchaseResponseBody, fuel_purchase, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        fuel_purchase = await async_client.fuel_purchases.create(
            fuel_quantity_liters="676.8",
            transaction_location="350 Rhode Island St, San Francisco, CA 94103",
            transaction_price={
                "amount": "640.2",
                "currency": "usd",
            },
            transaction_reference="5454534",
            transaction_time="2022-07-13T14:20:50.52-07:00",
            ifta_fuel_type="Unspecified",
            vehicle_id="281474900488527",
        )
        assert_matches_type(FuelPurchasePostFuelPurchaseResponseBody, fuel_purchase, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fuel_purchases.with_raw_response.create(
            fuel_quantity_liters="676.8",
            transaction_location="350 Rhode Island St, San Francisco, CA 94103",
            transaction_price={
                "amount": "640.2",
                "currency": "usd",
            },
            transaction_reference="5454534",
            transaction_time="2022-07-13T14:20:50.52-07:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fuel_purchase = await response.parse()
        assert_matches_type(FuelPurchasePostFuelPurchaseResponseBody, fuel_purchase, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.fuel_purchases.with_streaming_response.create(
            fuel_quantity_liters="676.8",
            transaction_location="350 Rhode Island St, San Francisco, CA 94103",
            transaction_price={
                "amount": "640.2",
                "currency": "usd",
            },
            transaction_reference="5454534",
            transaction_time="2022-07-13T14:20:50.52-07:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fuel_purchase = await response.parse()
            assert_matches_type(FuelPurchasePostFuelPurchaseResponseBody, fuel_purchase, path=["response"])

        assert cast(Any, response.is_closed) is True
