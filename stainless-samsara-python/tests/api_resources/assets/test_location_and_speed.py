# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.assets import LocationAndSpeedStreamResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLocationAndSpeed:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_stream(self, client: Samsara) -> None:
        location_and_speed = client.assets.location_and_speed.stream()
        assert_matches_type(LocationAndSpeedStreamResponse, location_and_speed, path=["response"])

    @parametrize
    def test_method_stream_with_all_params(self, client: Samsara) -> None:
        location_and_speed = client.assets.location_and_speed.stream(
            after="after",
            end_time="endTime",
            ids=["string"],
            include_external_ids=True,
            include_geofence_lookup=True,
            include_reverse_geo=True,
            include_speed=True,
            limit=1,
            start_time="startTime",
        )
        assert_matches_type(LocationAndSpeedStreamResponse, location_and_speed, path=["response"])

    @parametrize
    def test_raw_response_stream(self, client: Samsara) -> None:
        response = client.assets.location_and_speed.with_raw_response.stream()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location_and_speed = response.parse()
        assert_matches_type(LocationAndSpeedStreamResponse, location_and_speed, path=["response"])

    @parametrize
    def test_streaming_response_stream(self, client: Samsara) -> None:
        with client.assets.location_and_speed.with_streaming_response.stream() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location_and_speed = response.parse()
            assert_matches_type(LocationAndSpeedStreamResponse, location_and_speed, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLocationAndSpeed:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_stream(self, async_client: AsyncSamsara) -> None:
        location_and_speed = await async_client.assets.location_and_speed.stream()
        assert_matches_type(LocationAndSpeedStreamResponse, location_and_speed, path=["response"])

    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncSamsara) -> None:
        location_and_speed = await async_client.assets.location_and_speed.stream(
            after="after",
            end_time="endTime",
            ids=["string"],
            include_external_ids=True,
            include_geofence_lookup=True,
            include_reverse_geo=True,
            include_speed=True,
            limit=1,
            start_time="startTime",
        )
        assert_matches_type(LocationAndSpeedStreamResponse, location_and_speed, path=["response"])

    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncSamsara) -> None:
        response = await async_client.assets.location_and_speed.with_raw_response.stream()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location_and_speed = await response.parse()
        assert_matches_type(LocationAndSpeedStreamResponse, location_and_speed, path=["response"])

    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncSamsara) -> None:
        async with async_client.assets.location_and_speed.with_streaming_response.stream() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location_and_speed = await response.parse()
            assert_matches_type(LocationAndSpeedStreamResponse, location_and_speed, path=["response"])

        assert cast(Any, response.is_closed) is True
