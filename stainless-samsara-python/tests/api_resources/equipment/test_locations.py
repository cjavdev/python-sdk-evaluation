# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.equipment import (
    LocationFeedResponse,
    LocationHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLocations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_feed(self, client: Samsara) -> None:
        location = client.equipment.locations.feed()
        assert_matches_type(LocationFeedResponse, location, path=["response"])

    @parametrize
    def test_method_feed_with_all_params(self, client: Samsara) -> None:
        location = client.equipment.locations.feed(
            after="after",
            equipment_ids=["string"],
            parent_tag_ids=["string"],
            tag_ids=["string"],
        )
        assert_matches_type(LocationFeedResponse, location, path=["response"])

    @parametrize
    def test_raw_response_feed(self, client: Samsara) -> None:
        response = client.equipment.locations.with_raw_response.feed()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(LocationFeedResponse, location, path=["response"])

    @parametrize
    def test_streaming_response_feed(self, client: Samsara) -> None:
        with client.equipment.locations.with_streaming_response.feed() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(LocationFeedResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_history(self, client: Samsara) -> None:
        location = client.equipment.locations.history(
            end_time="endTime",
            start_time="startTime",
        )
        assert_matches_type(LocationHistoryResponse, location, path=["response"])

    @parametrize
    def test_method_history_with_all_params(self, client: Samsara) -> None:
        location = client.equipment.locations.history(
            end_time="endTime",
            start_time="startTime",
            after="after",
            equipment_ids=["string"],
            parent_tag_ids=["string"],
            tag_ids=["string"],
        )
        assert_matches_type(LocationHistoryResponse, location, path=["response"])

    @parametrize
    def test_raw_response_history(self, client: Samsara) -> None:
        response = client.equipment.locations.with_raw_response.history(
            end_time="endTime",
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(LocationHistoryResponse, location, path=["response"])

    @parametrize
    def test_streaming_response_history(self, client: Samsara) -> None:
        with client.equipment.locations.with_streaming_response.history(
            end_time="endTime",
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(LocationHistoryResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLocations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_feed(self, async_client: AsyncSamsara) -> None:
        location = await async_client.equipment.locations.feed()
        assert_matches_type(LocationFeedResponse, location, path=["response"])

    @parametrize
    async def test_method_feed_with_all_params(self, async_client: AsyncSamsara) -> None:
        location = await async_client.equipment.locations.feed(
            after="after",
            equipment_ids=["string"],
            parent_tag_ids=["string"],
            tag_ids=["string"],
        )
        assert_matches_type(LocationFeedResponse, location, path=["response"])

    @parametrize
    async def test_raw_response_feed(self, async_client: AsyncSamsara) -> None:
        response = await async_client.equipment.locations.with_raw_response.feed()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(LocationFeedResponse, location, path=["response"])

    @parametrize
    async def test_streaming_response_feed(self, async_client: AsyncSamsara) -> None:
        async with async_client.equipment.locations.with_streaming_response.feed() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(LocationFeedResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_history(self, async_client: AsyncSamsara) -> None:
        location = await async_client.equipment.locations.history(
            end_time="endTime",
            start_time="startTime",
        )
        assert_matches_type(LocationHistoryResponse, location, path=["response"])

    @parametrize
    async def test_method_history_with_all_params(self, async_client: AsyncSamsara) -> None:
        location = await async_client.equipment.locations.history(
            end_time="endTime",
            start_time="startTime",
            after="after",
            equipment_ids=["string"],
            parent_tag_ids=["string"],
            tag_ids=["string"],
        )
        assert_matches_type(LocationHistoryResponse, location, path=["response"])

    @parametrize
    async def test_raw_response_history(self, async_client: AsyncSamsara) -> None:
        response = await async_client.equipment.locations.with_raw_response.history(
            end_time="endTime",
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(LocationHistoryResponse, location, path=["response"])

    @parametrize
    async def test_streaming_response_history(self, async_client: AsyncSamsara) -> None:
        async with async_client.equipment.locations.with_streaming_response.history(
            end_time="endTime",
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(LocationHistoryResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True
