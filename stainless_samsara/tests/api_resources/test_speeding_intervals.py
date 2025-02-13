# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import SpeedingIntervalsGetSpeedingIntervalsResponseBody

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpeedingIntervals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_stream(self, client: Samsara) -> None:
        speeding_interval = client.speeding_intervals.stream(
            asset_ids=["string"],
            start_time="startTime",
        )
        assert_matches_type(SpeedingIntervalsGetSpeedingIntervalsResponseBody, speeding_interval, path=["response"])

    @parametrize
    def test_method_stream_with_all_params(self, client: Samsara) -> None:
        speeding_interval = client.speeding_intervals.stream(
            asset_ids=["string"],
            start_time="startTime",
            after="after",
            end_time="endTime",
            include_asset=True,
            include_driver_id=True,
            query_by="updatedAtTime",
            severity_levels=["string"],
        )
        assert_matches_type(SpeedingIntervalsGetSpeedingIntervalsResponseBody, speeding_interval, path=["response"])

    @parametrize
    def test_raw_response_stream(self, client: Samsara) -> None:
        response = client.speeding_intervals.with_raw_response.stream(
            asset_ids=["string"],
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speeding_interval = response.parse()
        assert_matches_type(SpeedingIntervalsGetSpeedingIntervalsResponseBody, speeding_interval, path=["response"])

    @parametrize
    def test_streaming_response_stream(self, client: Samsara) -> None:
        with client.speeding_intervals.with_streaming_response.stream(
            asset_ids=["string"],
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speeding_interval = response.parse()
            assert_matches_type(SpeedingIntervalsGetSpeedingIntervalsResponseBody, speeding_interval, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSpeedingIntervals:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_stream(self, async_client: AsyncSamsara) -> None:
        speeding_interval = await async_client.speeding_intervals.stream(
            asset_ids=["string"],
            start_time="startTime",
        )
        assert_matches_type(SpeedingIntervalsGetSpeedingIntervalsResponseBody, speeding_interval, path=["response"])

    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncSamsara) -> None:
        speeding_interval = await async_client.speeding_intervals.stream(
            asset_ids=["string"],
            start_time="startTime",
            after="after",
            end_time="endTime",
            include_asset=True,
            include_driver_id=True,
            query_by="updatedAtTime",
            severity_levels=["string"],
        )
        assert_matches_type(SpeedingIntervalsGetSpeedingIntervalsResponseBody, speeding_interval, path=["response"])

    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncSamsara) -> None:
        response = await async_client.speeding_intervals.with_raw_response.stream(
            asset_ids=["string"],
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speeding_interval = await response.parse()
        assert_matches_type(SpeedingIntervalsGetSpeedingIntervalsResponseBody, speeding_interval, path=["response"])

    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncSamsara) -> None:
        async with async_client.speeding_intervals.with_streaming_response.stream(
            asset_ids=["string"],
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speeding_interval = await response.parse()
            assert_matches_type(SpeedingIntervalsGetSpeedingIntervalsResponseBody, speeding_interval, path=["response"])

        assert cast(Any, response.is_closed) is True
