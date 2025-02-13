# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.industrial import (
    InlineResponse200,
    ListIndustrialAssetsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        asset = client.industrial.assets.create(
            name="name",
        )
        assert_matches_type(InlineResponse200, asset, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        asset = client.industrial.assets.create(
            name="name",
            custom_metadata={
                "manufacturer": "Samsara",
                "serialNumber": "123ABC",
            },
            location={
                "formatted_address": "350 Rhode Island St, San Francisco CA, 94103",
                "latitude": 37.765363,
                "longitude": -122.403098,
            },
            location_data_input_id="12345",
            location_type="point",
            parent_id="123abcde-4567-8910-1112-fghi1314jklm",
            running_status_data_input_id="67890",
            tag_ids=["123"],
        )
        assert_matches_type(InlineResponse200, asset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.industrial.assets.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(InlineResponse200, asset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.industrial.assets.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(InlineResponse200, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        asset = client.industrial.assets.update(
            id="id",
        )
        assert_matches_type(InlineResponse200, asset, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        asset = client.industrial.assets.update(
            id="id",
            custom_metadata={
                "manufacturer": "Samsara",
                "serialNumber": "123ABC",
            },
            location={
                "formatted_address": "350 Rhode Island St, San Francisco CA, 94103",
                "latitude": 37.765363,
                "longitude": -122.403098,
            },
            location_data_input_id="12345",
            location_type="point",
            name="name",
            parent_id="",
            running_status_data_input_id="67890",
            tag_ids=["123"],
        )
        assert_matches_type(InlineResponse200, asset, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.industrial.assets.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(InlineResponse200, asset, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.industrial.assets.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(InlineResponse200, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.industrial.assets.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        asset = client.industrial.assets.list()
        assert_matches_type(ListIndustrialAssetsResponse, asset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        asset = client.industrial.assets.list(
            after="after",
            asset_ids=["string"],
            limit=1,
            parent_tag_ids=["string"],
            tag_ids=["string"],
        )
        assert_matches_type(ListIndustrialAssetsResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.industrial.assets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(ListIndustrialAssetsResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.industrial.assets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(ListIndustrialAssetsResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Samsara) -> None:
        asset = client.industrial.assets.delete(
            "id",
        )
        assert_matches_type(str, asset, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Samsara) -> None:
        response = client.industrial.assets.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(str, asset, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Samsara) -> None:
        with client.industrial.assets.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(str, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.industrial.assets.with_raw_response.delete(
                "",
            )


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        asset = await async_client.industrial.assets.create(
            name="name",
        )
        assert_matches_type(InlineResponse200, asset, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        asset = await async_client.industrial.assets.create(
            name="name",
            custom_metadata={
                "manufacturer": "Samsara",
                "serialNumber": "123ABC",
            },
            location={
                "formatted_address": "350 Rhode Island St, San Francisco CA, 94103",
                "latitude": 37.765363,
                "longitude": -122.403098,
            },
            location_data_input_id="12345",
            location_type="point",
            parent_id="123abcde-4567-8910-1112-fghi1314jklm",
            running_status_data_input_id="67890",
            tag_ids=["123"],
        )
        assert_matches_type(InlineResponse200, asset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.industrial.assets.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(InlineResponse200, asset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.industrial.assets.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(InlineResponse200, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        asset = await async_client.industrial.assets.update(
            id="id",
        )
        assert_matches_type(InlineResponse200, asset, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        asset = await async_client.industrial.assets.update(
            id="id",
            custom_metadata={
                "manufacturer": "Samsara",
                "serialNumber": "123ABC",
            },
            location={
                "formatted_address": "350 Rhode Island St, San Francisco CA, 94103",
                "latitude": 37.765363,
                "longitude": -122.403098,
            },
            location_data_input_id="12345",
            location_type="point",
            name="name",
            parent_id="",
            running_status_data_input_id="67890",
            tag_ids=["123"],
        )
        assert_matches_type(InlineResponse200, asset, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.industrial.assets.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(InlineResponse200, asset, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.industrial.assets.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(InlineResponse200, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.industrial.assets.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        asset = await async_client.industrial.assets.list()
        assert_matches_type(ListIndustrialAssetsResponse, asset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        asset = await async_client.industrial.assets.list(
            after="after",
            asset_ids=["string"],
            limit=1,
            parent_tag_ids=["string"],
            tag_ids=["string"],
        )
        assert_matches_type(ListIndustrialAssetsResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.industrial.assets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(ListIndustrialAssetsResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.industrial.assets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(ListIndustrialAssetsResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSamsara) -> None:
        asset = await async_client.industrial.assets.delete(
            "id",
        )
        assert_matches_type(str, asset, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSamsara) -> None:
        response = await async_client.industrial.assets.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(str, asset, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSamsara) -> None:
        async with async_client.industrial.assets.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(str, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.industrial.assets.with_raw_response.delete(
                "",
            )
