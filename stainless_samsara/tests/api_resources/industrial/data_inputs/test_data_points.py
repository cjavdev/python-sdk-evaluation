# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.industrial.data_inputs import (
    DataInputListResponse,
    DataInputSnapshotResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataPoints:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        data_point = client.industrial.data_inputs.data_points.retrieve()
        assert_matches_type(DataInputSnapshotResponse, data_point, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Samsara) -> None:
        data_point = client.industrial.data_inputs.data_points.retrieve(
            after="after",
            asset_ids=["string"],
            data_input_ids=["string"],
            parent_tag_ids=["string"],
            tag_ids=["string"],
        )
        assert_matches_type(DataInputSnapshotResponse, data_point, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.industrial.data_inputs.data_points.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_point = response.parse()
        assert_matches_type(DataInputSnapshotResponse, data_point, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.industrial.data_inputs.data_points.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_point = response.parse()
            assert_matches_type(DataInputSnapshotResponse, data_point, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_feed(self, client: Samsara) -> None:
        data_point = client.industrial.data_inputs.data_points.feed()
        assert_matches_type(DataInputListResponse, data_point, path=["response"])

    @parametrize
    def test_method_feed_with_all_params(self, client: Samsara) -> None:
        data_point = client.industrial.data_inputs.data_points.feed(
            after="after",
            asset_ids=["string"],
            data_input_ids=["string"],
            parent_tag_ids=["string"],
            tag_ids=["string"],
        )
        assert_matches_type(DataInputListResponse, data_point, path=["response"])

    @parametrize
    def test_raw_response_feed(self, client: Samsara) -> None:
        response = client.industrial.data_inputs.data_points.with_raw_response.feed()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_point = response.parse()
        assert_matches_type(DataInputListResponse, data_point, path=["response"])

    @parametrize
    def test_streaming_response_feed(self, client: Samsara) -> None:
        with client.industrial.data_inputs.data_points.with_streaming_response.feed() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_point = response.parse()
            assert_matches_type(DataInputListResponse, data_point, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_history(self, client: Samsara) -> None:
        data_point = client.industrial.data_inputs.data_points.history(
            end_time="endTime",
            start_time="startTime",
        )
        assert_matches_type(DataInputListResponse, data_point, path=["response"])

    @parametrize
    def test_method_history_with_all_params(self, client: Samsara) -> None:
        data_point = client.industrial.data_inputs.data_points.history(
            end_time="endTime",
            start_time="startTime",
            after="after",
            asset_ids=["string"],
            data_input_ids=["string"],
            parent_tag_ids=["string"],
            tag_ids=["string"],
        )
        assert_matches_type(DataInputListResponse, data_point, path=["response"])

    @parametrize
    def test_raw_response_history(self, client: Samsara) -> None:
        response = client.industrial.data_inputs.data_points.with_raw_response.history(
            end_time="endTime",
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_point = response.parse()
        assert_matches_type(DataInputListResponse, data_point, path=["response"])

    @parametrize
    def test_streaming_response_history(self, client: Samsara) -> None:
        with client.industrial.data_inputs.data_points.with_streaming_response.history(
            end_time="endTime",
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_point = response.parse()
            assert_matches_type(DataInputListResponse, data_point, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDataPoints:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        data_point = await async_client.industrial.data_inputs.data_points.retrieve()
        assert_matches_type(DataInputSnapshotResponse, data_point, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSamsara) -> None:
        data_point = await async_client.industrial.data_inputs.data_points.retrieve(
            after="after",
            asset_ids=["string"],
            data_input_ids=["string"],
            parent_tag_ids=["string"],
            tag_ids=["string"],
        )
        assert_matches_type(DataInputSnapshotResponse, data_point, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.industrial.data_inputs.data_points.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_point = await response.parse()
        assert_matches_type(DataInputSnapshotResponse, data_point, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.industrial.data_inputs.data_points.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_point = await response.parse()
            assert_matches_type(DataInputSnapshotResponse, data_point, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_feed(self, async_client: AsyncSamsara) -> None:
        data_point = await async_client.industrial.data_inputs.data_points.feed()
        assert_matches_type(DataInputListResponse, data_point, path=["response"])

    @parametrize
    async def test_method_feed_with_all_params(self, async_client: AsyncSamsara) -> None:
        data_point = await async_client.industrial.data_inputs.data_points.feed(
            after="after",
            asset_ids=["string"],
            data_input_ids=["string"],
            parent_tag_ids=["string"],
            tag_ids=["string"],
        )
        assert_matches_type(DataInputListResponse, data_point, path=["response"])

    @parametrize
    async def test_raw_response_feed(self, async_client: AsyncSamsara) -> None:
        response = await async_client.industrial.data_inputs.data_points.with_raw_response.feed()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_point = await response.parse()
        assert_matches_type(DataInputListResponse, data_point, path=["response"])

    @parametrize
    async def test_streaming_response_feed(self, async_client: AsyncSamsara) -> None:
        async with async_client.industrial.data_inputs.data_points.with_streaming_response.feed() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_point = await response.parse()
            assert_matches_type(DataInputListResponse, data_point, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_history(self, async_client: AsyncSamsara) -> None:
        data_point = await async_client.industrial.data_inputs.data_points.history(
            end_time="endTime",
            start_time="startTime",
        )
        assert_matches_type(DataInputListResponse, data_point, path=["response"])

    @parametrize
    async def test_method_history_with_all_params(self, async_client: AsyncSamsara) -> None:
        data_point = await async_client.industrial.data_inputs.data_points.history(
            end_time="endTime",
            start_time="startTime",
            after="after",
            asset_ids=["string"],
            data_input_ids=["string"],
            parent_tag_ids=["string"],
            tag_ids=["string"],
        )
        assert_matches_type(DataInputListResponse, data_point, path=["response"])

    @parametrize
    async def test_raw_response_history(self, async_client: AsyncSamsara) -> None:
        response = await async_client.industrial.data_inputs.data_points.with_raw_response.history(
            end_time="endTime",
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_point = await response.parse()
        assert_matches_type(DataInputListResponse, data_point, path=["response"])

    @parametrize
    async def test_streaming_response_history(self, async_client: AsyncSamsara) -> None:
        async with async_client.industrial.data_inputs.data_points.with_streaming_response.history(
            end_time="endTime",
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_point = await response.parse()
            assert_matches_type(DataInputListResponse, data_point, path=["response"])

        assert cast(Any, response.is_closed) is True
