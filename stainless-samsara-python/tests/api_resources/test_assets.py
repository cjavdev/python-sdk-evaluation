# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import (
    AssetListResponse,
    AssetCreateResponse,
    AssetUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        asset = client.assets.create()
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        asset = client.assets.create(
            external_ids={"foo": "string"},
            license_plate="XHK1234",
            make="Bobcat",
            model="S630 T4",
            name="MyAsset-1234",
            notes="These are notes.",
            regulation_mode="mixed",
            serial_number="8V8WD530FLN016251",
            type="uncategorized",
            vin="1FUJBBCKXCLBZ1234",
            year=2015,
        )
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.assets.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.assets.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetCreateResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        asset = client.assets.update(
            id="id",
        )
        assert_matches_type(AssetUpdateResponse, asset, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        asset = client.assets.update(
            id="id",
            external_ids={"foo": "string"},
            license_plate="XHK1234",
            make="Bobcat",
            model="S630 T4",
            name="MyAsset-1234",
            notes="These are notes.",
            regulation_mode="mixed",
            serial_number="8V8WD530FLN016251",
            type="uncategorized",
            vin="1FUJBBCKXCLBZ1234",
            year=2015,
        )
        assert_matches_type(AssetUpdateResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.assets.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetUpdateResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.assets.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetUpdateResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        asset = client.assets.list()
        assert_matches_type(AssetListResponse, asset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        asset = client.assets.list(
            after="after",
            attribute_value_ids="attributeValueIds",
            ids=["string"],
            include_external_ids=True,
            include_tags=True,
            parent_tag_ids="parentTagIds",
            tag_ids="tagIds",
            type="uncategorized",
            updated_after_time="updatedAfterTime",
        )
        assert_matches_type(AssetListResponse, asset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.assets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetListResponse, asset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.assets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetListResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Samsara) -> None:
        asset = client.assets.delete(
            id="id",
        )
        assert asset is None

    @parametrize
    def test_raw_response_delete(self, client: Samsara) -> None:
        response = client.assets.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @parametrize
    def test_streaming_response_delete(self, client: Samsara) -> None:
        with client.assets.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        asset = await async_client.assets.create()
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        asset = await async_client.assets.create(
            external_ids={"foo": "string"},
            license_plate="XHK1234",
            make="Bobcat",
            model="S630 T4",
            name="MyAsset-1234",
            notes="These are notes.",
            regulation_mode="mixed",
            serial_number="8V8WD530FLN016251",
            type="uncategorized",
            vin="1FUJBBCKXCLBZ1234",
            year=2015,
        )
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.assets.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetCreateResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.assets.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetCreateResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        asset = await async_client.assets.update(
            id="id",
        )
        assert_matches_type(AssetUpdateResponse, asset, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        asset = await async_client.assets.update(
            id="id",
            external_ids={"foo": "string"},
            license_plate="XHK1234",
            make="Bobcat",
            model="S630 T4",
            name="MyAsset-1234",
            notes="These are notes.",
            regulation_mode="mixed",
            serial_number="8V8WD530FLN016251",
            type="uncategorized",
            vin="1FUJBBCKXCLBZ1234",
            year=2015,
        )
        assert_matches_type(AssetUpdateResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.assets.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetUpdateResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.assets.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetUpdateResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        asset = await async_client.assets.list()
        assert_matches_type(AssetListResponse, asset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        asset = await async_client.assets.list(
            after="after",
            attribute_value_ids="attributeValueIds",
            ids=["string"],
            include_external_ids=True,
            include_tags=True,
            parent_tag_ids="parentTagIds",
            tag_ids="tagIds",
            type="uncategorized",
            updated_after_time="updatedAfterTime",
        )
        assert_matches_type(AssetListResponse, asset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.assets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetListResponse, asset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.assets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetListResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSamsara) -> None:
        asset = await async_client.assets.delete(
            id="id",
        )
        assert asset is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSamsara) -> None:
        response = await async_client.assets.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSamsara) -> None:
        async with async_client.assets.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True
