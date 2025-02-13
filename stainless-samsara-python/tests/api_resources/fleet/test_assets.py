# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet import InlineResponse200_1, V1AssetReeferResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        asset = client.fleet.assets.list()
        assert_matches_type(InlineResponse200_1, asset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.fleet.assets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(InlineResponse200_1, asset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.fleet.assets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(InlineResponse200_1, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_reefer(self, client: Samsara) -> None:
        asset = client.fleet.assets.reefer(
            asset_id=0,
            end_ms=0,
            start_ms=0,
        )
        assert_matches_type(V1AssetReeferResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_reefer(self, client: Samsara) -> None:
        response = client.fleet.assets.with_raw_response.reefer(
            asset_id=0,
            end_ms=0,
            start_ms=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(V1AssetReeferResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_reefer(self, client: Samsara) -> None:
        with client.fleet.assets.with_streaming_response.reefer(
            asset_id=0,
            end_ms=0,
            start_ms=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(V1AssetReeferResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        asset = await async_client.fleet.assets.list()
        assert_matches_type(InlineResponse200_1, asset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.assets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(InlineResponse200_1, asset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.assets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(InlineResponse200_1, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_reefer(self, async_client: AsyncSamsara) -> None:
        asset = await async_client.fleet.assets.reefer(
            asset_id=0,
            end_ms=0,
            start_ms=0,
        )
        assert_matches_type(V1AssetReeferResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_reefer(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.assets.with_raw_response.reefer(
            asset_id=0,
            end_ms=0,
            start_ms=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(V1AssetReeferResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_reefer(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.assets.with_streaming_response.reefer(
            asset_id=0,
            end_ms=0,
            start_ms=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(V1AssetReeferResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True
