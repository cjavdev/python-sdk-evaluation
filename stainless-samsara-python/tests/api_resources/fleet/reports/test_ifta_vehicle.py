# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet.reports import IftaVehicleListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIftaVehicle:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        ifta_vehicle = client.fleet.reports.ifta_vehicle.list(
            year=2015,
        )
        assert_matches_type(IftaVehicleListResponse, ifta_vehicle, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        ifta_vehicle = client.fleet.reports.ifta_vehicle.list(
            year=2015,
            after="after",
            fuel_type="Unspecified",
            jurisdictions="jurisdictions",
            month="January",
            parent_tag_ids="parentTagIds",
            quarter="Q1",
            tag_ids="tagIds",
            vehicle_ids="vehicleIds",
        )
        assert_matches_type(IftaVehicleListResponse, ifta_vehicle, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.fleet.reports.ifta_vehicle.with_raw_response.list(
            year=2015,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ifta_vehicle = response.parse()
        assert_matches_type(IftaVehicleListResponse, ifta_vehicle, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.fleet.reports.ifta_vehicle.with_streaming_response.list(
            year=2015,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ifta_vehicle = response.parse()
            assert_matches_type(IftaVehicleListResponse, ifta_vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIftaVehicle:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        ifta_vehicle = await async_client.fleet.reports.ifta_vehicle.list(
            year=2015,
        )
        assert_matches_type(IftaVehicleListResponse, ifta_vehicle, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        ifta_vehicle = await async_client.fleet.reports.ifta_vehicle.list(
            year=2015,
            after="after",
            fuel_type="Unspecified",
            jurisdictions="jurisdictions",
            month="January",
            parent_tag_ids="parentTagIds",
            quarter="Q1",
            tag_ids="tagIds",
            vehicle_ids="vehicleIds",
        )
        assert_matches_type(IftaVehicleListResponse, ifta_vehicle, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.reports.ifta_vehicle.with_raw_response.list(
            year=2015,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ifta_vehicle = await response.parse()
        assert_matches_type(IftaVehicleListResponse, ifta_vehicle, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.reports.ifta_vehicle.with_streaming_response.list(
            year=2015,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ifta_vehicle = await response.parse()
            assert_matches_type(IftaVehicleListResponse, ifta_vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True
