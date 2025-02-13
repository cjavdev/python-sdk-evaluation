# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet import V1AssetLocationResponse
from samsara.types.fleet.assets import LocationListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLocations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        location = client.fleet.assets.locations.retrieve(
            asset_id=0,
            end_ms=0,
            start_ms=0,
        )
        assert_matches_type(V1AssetLocationResponse, location, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.fleet.assets.locations.with_raw_response.retrieve(
            asset_id=0,
            end_ms=0,
            start_ms=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(V1AssetLocationResponse, location, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.fleet.assets.locations.with_streaming_response.retrieve(
            asset_id=0,
            end_ms=0,
            start_ms=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(V1AssetLocationResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        location = client.fleet.assets.locations.list()
        assert_matches_type(LocationListResponse, location, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        location = client.fleet.assets.locations.list(
            ending_before="endingBefore",
            limit=0,
            starting_after="startingAfter",
        )
        assert_matches_type(LocationListResponse, location, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.fleet.assets.locations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(LocationListResponse, location, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.fleet.assets.locations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(LocationListResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLocations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        location = await async_client.fleet.assets.locations.retrieve(
            asset_id=0,
            end_ms=0,
            start_ms=0,
        )
        assert_matches_type(V1AssetLocationResponse, location, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.assets.locations.with_raw_response.retrieve(
            asset_id=0,
            end_ms=0,
            start_ms=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(V1AssetLocationResponse, location, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.assets.locations.with_streaming_response.retrieve(
            asset_id=0,
            end_ms=0,
            start_ms=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(V1AssetLocationResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        location = await async_client.fleet.assets.locations.list()
        assert_matches_type(LocationListResponse, location, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        location = await async_client.fleet.assets.locations.list(
            ending_before="endingBefore",
            limit=0,
            starting_after="startingAfter",
        )
        assert_matches_type(LocationListResponse, location, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.assets.locations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(LocationListResponse, location, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.assets.locations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(LocationListResponse, location, path=["response"])

        assert cast(Any, response.is_closed) is True
