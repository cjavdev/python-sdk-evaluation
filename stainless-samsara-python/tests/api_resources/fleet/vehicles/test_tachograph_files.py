# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet.vehicles import TachographVehicleFilesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTachographFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_history(self, client: Samsara) -> None:
        tachograph_file = client.fleet.vehicles.tachograph_files.history(
            end_time="endTime",
            start_time="startTime",
        )
        assert_matches_type(TachographVehicleFilesResponse, tachograph_file, path=["response"])

    @parametrize
    def test_method_history_with_all_params(self, client: Samsara) -> None:
        tachograph_file = client.fleet.vehicles.tachograph_files.history(
            end_time="endTime",
            start_time="startTime",
            after="after",
            parent_tag_ids=["string"],
            tag_ids=["string"],
            vehicle_ids=["string"],
        )
        assert_matches_type(TachographVehicleFilesResponse, tachograph_file, path=["response"])

    @parametrize
    def test_raw_response_history(self, client: Samsara) -> None:
        response = client.fleet.vehicles.tachograph_files.with_raw_response.history(
            end_time="endTime",
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tachograph_file = response.parse()
        assert_matches_type(TachographVehicleFilesResponse, tachograph_file, path=["response"])

    @parametrize
    def test_streaming_response_history(self, client: Samsara) -> None:
        with client.fleet.vehicles.tachograph_files.with_streaming_response.history(
            end_time="endTime",
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tachograph_file = response.parse()
            assert_matches_type(TachographVehicleFilesResponse, tachograph_file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTachographFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_history(self, async_client: AsyncSamsara) -> None:
        tachograph_file = await async_client.fleet.vehicles.tachograph_files.history(
            end_time="endTime",
            start_time="startTime",
        )
        assert_matches_type(TachographVehicleFilesResponse, tachograph_file, path=["response"])

    @parametrize
    async def test_method_history_with_all_params(self, async_client: AsyncSamsara) -> None:
        tachograph_file = await async_client.fleet.vehicles.tachograph_files.history(
            end_time="endTime",
            start_time="startTime",
            after="after",
            parent_tag_ids=["string"],
            tag_ids=["string"],
            vehicle_ids=["string"],
        )
        assert_matches_type(TachographVehicleFilesResponse, tachograph_file, path=["response"])

    @parametrize
    async def test_raw_response_history(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.vehicles.tachograph_files.with_raw_response.history(
            end_time="endTime",
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tachograph_file = await response.parse()
        assert_matches_type(TachographVehicleFilesResponse, tachograph_file, path=["response"])

    @parametrize
    async def test_streaming_response_history(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.vehicles.tachograph_files.with_streaming_response.history(
            end_time="endTime",
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tachograph_file = await response.parse()
            assert_matches_type(TachographVehicleFilesResponse, tachograph_file, path=["response"])

        assert cast(Any, response.is_closed) is True
