# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.industrial.assets import AssetDataOutputsPatchAssetDataOutputsResponseBody

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataOutputs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        data_output = client.industrial.assets.data_outputs.update(
            id="id",
            values="",
        )
        assert_matches_type(AssetDataOutputsPatchAssetDataOutputsResponseBody, data_output, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.industrial.assets.data_outputs.with_raw_response.update(
            id="id",
            values="",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_output = response.parse()
        assert_matches_type(AssetDataOutputsPatchAssetDataOutputsResponseBody, data_output, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.industrial.assets.data_outputs.with_streaming_response.update(
            id="id",
            values="",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_output = response.parse()
            assert_matches_type(AssetDataOutputsPatchAssetDataOutputsResponseBody, data_output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.industrial.assets.data_outputs.with_raw_response.update(
                id="",
                values="",
            )


class TestAsyncDataOutputs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        data_output = await async_client.industrial.assets.data_outputs.update(
            id="id",
            values="",
        )
        assert_matches_type(AssetDataOutputsPatchAssetDataOutputsResponseBody, data_output, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.industrial.assets.data_outputs.with_raw_response.update(
            id="id",
            values="",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_output = await response.parse()
        assert_matches_type(AssetDataOutputsPatchAssetDataOutputsResponseBody, data_output, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.industrial.assets.data_outputs.with_streaming_response.update(
            id="id",
            values="",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_output = await response.parse()
            assert_matches_type(AssetDataOutputsPatchAssetDataOutputsResponseBody, data_output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.industrial.assets.data_outputs.with_raw_response.update(
                id="",
                values="",
            )
