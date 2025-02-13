# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet.reports import VehicleIdlingListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVehicleIdling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        vehicle_idling = client.fleet.reports.vehicle_idling.list(
            end_time="endTime",
            start_time="startTime",
        )
        assert_matches_type(VehicleIdlingListResponse, vehicle_idling, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        vehicle_idling = client.fleet.reports.vehicle_idling.list(
            end_time="endTime",
            start_time="startTime",
            after="after",
            is_pto_active=True,
            limit=1,
            min_idling_duration_minutes=1,
            parent_tag_ids="parentTagIds",
            tag_ids="tagIds",
            vehicle_ids="vehicleIds",
        )
        assert_matches_type(VehicleIdlingListResponse, vehicle_idling, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.fleet.reports.vehicle_idling.with_raw_response.list(
            end_time="endTime",
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle_idling = response.parse()
        assert_matches_type(VehicleIdlingListResponse, vehicle_idling, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.fleet.reports.vehicle_idling.with_streaming_response.list(
            end_time="endTime",
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle_idling = response.parse()
            assert_matches_type(VehicleIdlingListResponse, vehicle_idling, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVehicleIdling:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        vehicle_idling = await async_client.fleet.reports.vehicle_idling.list(
            end_time="endTime",
            start_time="startTime",
        )
        assert_matches_type(VehicleIdlingListResponse, vehicle_idling, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        vehicle_idling = await async_client.fleet.reports.vehicle_idling.list(
            end_time="endTime",
            start_time="startTime",
            after="after",
            is_pto_active=True,
            limit=1,
            min_idling_duration_minutes=1,
            parent_tag_ids="parentTagIds",
            tag_ids="tagIds",
            vehicle_ids="vehicleIds",
        )
        assert_matches_type(VehicleIdlingListResponse, vehicle_idling, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.reports.vehicle_idling.with_raw_response.list(
            end_time="endTime",
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicle_idling = await response.parse()
        assert_matches_type(VehicleIdlingListResponse, vehicle_idling, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.reports.vehicle_idling.with_streaming_response.list(
            end_time="endTime",
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicle_idling = await response.parse()
            assert_matches_type(VehicleIdlingListResponse, vehicle_idling, path=["response"])

        assert cast(Any, response.is_closed) is True
