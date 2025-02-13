# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import (
    LiveShareListResponse,
    LiveShareCreateResponse,
    LiveShareUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLiveShares:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        live_share = client.live_shares.create(
            name="Example Live Sharing Link name",
            type="assetsLocation",
        )
        assert_matches_type(LiveShareCreateResponse, live_share, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        live_share = client.live_shares.create(
            name="Example Live Sharing Link name",
            type="assetsLocation",
            assets_location_link_config={
                "asset_id": "1234",
                "location": {
                    "formatted_address": "1990 Alameda Street, San Francisco, CA 94103",
                    "latitude": 37.456345,
                    "longitude": 34.5633749,
                    "name": "Suburbs",
                },
            },
            assets_near_location_link_config={"address_id": "1234"},
            assets_on_route_link_config={"recurring_route_id": "1234"},
            description="Sample description",
            expires_at_time="2020-01-27T07:06:25Z",
        )
        assert_matches_type(LiveShareCreateResponse, live_share, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.live_shares.with_raw_response.create(
            name="Example Live Sharing Link name",
            type="assetsLocation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_share = response.parse()
        assert_matches_type(LiveShareCreateResponse, live_share, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.live_shares.with_streaming_response.create(
            name="Example Live Sharing Link name",
            type="assetsLocation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_share = response.parse()
            assert_matches_type(LiveShareCreateResponse, live_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        live_share = client.live_shares.update(
            id="id",
            name="Example Live Sharing Link name",
        )
        assert_matches_type(LiveShareUpdateResponse, live_share, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        live_share = client.live_shares.update(
            id="id",
            name="Example Live Sharing Link name",
            description="Sample description",
            expires_at_time="2020-01-27T07:06:25Z",
        )
        assert_matches_type(LiveShareUpdateResponse, live_share, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.live_shares.with_raw_response.update(
            id="id",
            name="Example Live Sharing Link name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_share = response.parse()
        assert_matches_type(LiveShareUpdateResponse, live_share, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.live_shares.with_streaming_response.update(
            id="id",
            name="Example Live Sharing Link name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_share = response.parse()
            assert_matches_type(LiveShareUpdateResponse, live_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        live_share = client.live_shares.list()
        assert_matches_type(LiveShareListResponse, live_share, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        live_share = client.live_shares.list(
            after="after",
            ids=["string"],
            limit=1,
            type="all",
        )
        assert_matches_type(LiveShareListResponse, live_share, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.live_shares.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_share = response.parse()
        assert_matches_type(LiveShareListResponse, live_share, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.live_shares.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_share = response.parse()
            assert_matches_type(LiveShareListResponse, live_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Samsara) -> None:
        live_share = client.live_shares.delete(
            id="id",
        )
        assert live_share is None

    @parametrize
    def test_raw_response_delete(self, client: Samsara) -> None:
        response = client.live_shares.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_share = response.parse()
        assert live_share is None

    @parametrize
    def test_streaming_response_delete(self, client: Samsara) -> None:
        with client.live_shares.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_share = response.parse()
            assert live_share is None

        assert cast(Any, response.is_closed) is True


class TestAsyncLiveShares:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        live_share = await async_client.live_shares.create(
            name="Example Live Sharing Link name",
            type="assetsLocation",
        )
        assert_matches_type(LiveShareCreateResponse, live_share, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        live_share = await async_client.live_shares.create(
            name="Example Live Sharing Link name",
            type="assetsLocation",
            assets_location_link_config={
                "asset_id": "1234",
                "location": {
                    "formatted_address": "1990 Alameda Street, San Francisco, CA 94103",
                    "latitude": 37.456345,
                    "longitude": 34.5633749,
                    "name": "Suburbs",
                },
            },
            assets_near_location_link_config={"address_id": "1234"},
            assets_on_route_link_config={"recurring_route_id": "1234"},
            description="Sample description",
            expires_at_time="2020-01-27T07:06:25Z",
        )
        assert_matches_type(LiveShareCreateResponse, live_share, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.live_shares.with_raw_response.create(
            name="Example Live Sharing Link name",
            type="assetsLocation",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_share = await response.parse()
        assert_matches_type(LiveShareCreateResponse, live_share, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.live_shares.with_streaming_response.create(
            name="Example Live Sharing Link name",
            type="assetsLocation",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_share = await response.parse()
            assert_matches_type(LiveShareCreateResponse, live_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        live_share = await async_client.live_shares.update(
            id="id",
            name="Example Live Sharing Link name",
        )
        assert_matches_type(LiveShareUpdateResponse, live_share, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        live_share = await async_client.live_shares.update(
            id="id",
            name="Example Live Sharing Link name",
            description="Sample description",
            expires_at_time="2020-01-27T07:06:25Z",
        )
        assert_matches_type(LiveShareUpdateResponse, live_share, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.live_shares.with_raw_response.update(
            id="id",
            name="Example Live Sharing Link name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_share = await response.parse()
        assert_matches_type(LiveShareUpdateResponse, live_share, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.live_shares.with_streaming_response.update(
            id="id",
            name="Example Live Sharing Link name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_share = await response.parse()
            assert_matches_type(LiveShareUpdateResponse, live_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        live_share = await async_client.live_shares.list()
        assert_matches_type(LiveShareListResponse, live_share, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        live_share = await async_client.live_shares.list(
            after="after",
            ids=["string"],
            limit=1,
            type="all",
        )
        assert_matches_type(LiveShareListResponse, live_share, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.live_shares.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_share = await response.parse()
        assert_matches_type(LiveShareListResponse, live_share, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.live_shares.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_share = await response.parse()
            assert_matches_type(LiveShareListResponse, live_share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSamsara) -> None:
        live_share = await async_client.live_shares.delete(
            id="id",
        )
        assert live_share is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSamsara) -> None:
        response = await async_client.live_shares.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        live_share = await response.parse()
        assert live_share is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSamsara) -> None:
        async with async_client.live_shares.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            live_share = await response.parse()
            assert live_share is None

        assert cast(Any, response.is_closed) is True
