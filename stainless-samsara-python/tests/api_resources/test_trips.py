# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import TripsGetTripsResponseBody
from samsara.types.fleet import V1TripResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrips:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        trip = client.trips.list(
            end_ms=0,
            start_ms=0,
            vehicle_id=0,
        )
        assert_matches_type(V1TripResponse, trip, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.trips.with_raw_response.list(
            end_ms=0,
            start_ms=0,
            vehicle_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trip = response.parse()
        assert_matches_type(V1TripResponse, trip, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.trips.with_streaming_response.list(
            end_ms=0,
            start_ms=0,
            vehicle_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trip = response.parse()
            assert_matches_type(V1TripResponse, trip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stream(self, client: Samsara) -> None:
        trip = client.trips.stream(
            ids=["string"],
            start_time="startTime",
        )
        assert_matches_type(TripsGetTripsResponseBody, trip, path=["response"])

    @parametrize
    def test_method_stream_with_all_params(self, client: Samsara) -> None:
        trip = client.trips.stream(
            ids=["string"],
            start_time="startTime",
            after="after",
            completion_status="inProgress",
            end_time="endTime",
            include_asset=True,
            query_by="updatedAtTime",
        )
        assert_matches_type(TripsGetTripsResponseBody, trip, path=["response"])

    @parametrize
    def test_raw_response_stream(self, client: Samsara) -> None:
        response = client.trips.with_raw_response.stream(
            ids=["string"],
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trip = response.parse()
        assert_matches_type(TripsGetTripsResponseBody, trip, path=["response"])

    @parametrize
    def test_streaming_response_stream(self, client: Samsara) -> None:
        with client.trips.with_streaming_response.stream(
            ids=["string"],
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trip = response.parse()
            assert_matches_type(TripsGetTripsResponseBody, trip, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTrips:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        trip = await async_client.trips.list(
            end_ms=0,
            start_ms=0,
            vehicle_id=0,
        )
        assert_matches_type(V1TripResponse, trip, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.trips.with_raw_response.list(
            end_ms=0,
            start_ms=0,
            vehicle_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trip = await response.parse()
        assert_matches_type(V1TripResponse, trip, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.trips.with_streaming_response.list(
            end_ms=0,
            start_ms=0,
            vehicle_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trip = await response.parse()
            assert_matches_type(V1TripResponse, trip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stream(self, async_client: AsyncSamsara) -> None:
        trip = await async_client.trips.stream(
            ids=["string"],
            start_time="startTime",
        )
        assert_matches_type(TripsGetTripsResponseBody, trip, path=["response"])

    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncSamsara) -> None:
        trip = await async_client.trips.stream(
            ids=["string"],
            start_time="startTime",
            after="after",
            completion_status="inProgress",
            end_time="endTime",
            include_asset=True,
            query_by="updatedAtTime",
        )
        assert_matches_type(TripsGetTripsResponseBody, trip, path=["response"])

    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncSamsara) -> None:
        response = await async_client.trips.with_raw_response.stream(
            ids=["string"],
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trip = await response.parse()
        assert_matches_type(TripsGetTripsResponseBody, trip, path=["response"])

    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncSamsara) -> None:
        async with async_client.trips.with_streaming_response.stream(
            ids=["string"],
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trip = await response.parse()
            assert_matches_type(TripsGetTripsResponseBody, trip, path=["response"])

        assert cast(Any, response.is_closed) is True
