# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import (
    GatewaysGetGatewaysResponseBody,
    GatewaysPostGatewayResponseBody,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGateways:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        gateway = client.gateways.list()
        assert_matches_type(GatewaysGetGatewaysResponseBody, gateway, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        gateway = client.gateways.list(
            after="after",
            models=["string"],
        )
        assert_matches_type(GatewaysGetGatewaysResponseBody, gateway, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.gateways.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = response.parse()
        assert_matches_type(GatewaysGetGatewaysResponseBody, gateway, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.gateways.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = response.parse()
            assert_matches_type(GatewaysGetGatewaysResponseBody, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_activate(self, client: Samsara) -> None:
        gateway = client.gateways.activate(
            serial="GFRV-43N-VGX",
        )
        assert_matches_type(GatewaysPostGatewayResponseBody, gateway, path=["response"])

    @parametrize
    def test_raw_response_activate(self, client: Samsara) -> None:
        response = client.gateways.with_raw_response.activate(
            serial="GFRV-43N-VGX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = response.parse()
        assert_matches_type(GatewaysPostGatewayResponseBody, gateway, path=["response"])

    @parametrize
    def test_streaming_response_activate(self, client: Samsara) -> None:
        with client.gateways.with_streaming_response.activate(
            serial="GFRV-43N-VGX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = response.parse()
            assert_matches_type(GatewaysPostGatewayResponseBody, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_deactivate(self, client: Samsara) -> None:
        gateway = client.gateways.deactivate(
            "bFXA-lFw-EV3",
        )
        assert gateway is None

    @parametrize
    def test_raw_response_deactivate(self, client: Samsara) -> None:
        response = client.gateways.with_raw_response.deactivate(
            "bFXA-lFw-EV3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = response.parse()
        assert gateway is None

    @parametrize
    def test_streaming_response_deactivate(self, client: Samsara) -> None:
        with client.gateways.with_streaming_response.deactivate(
            "bFXA-lFw-EV3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = response.parse()
            assert gateway is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_deactivate(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.gateways.with_raw_response.deactivate(
                "",
            )


class TestAsyncGateways:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        gateway = await async_client.gateways.list()
        assert_matches_type(GatewaysGetGatewaysResponseBody, gateway, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        gateway = await async_client.gateways.list(
            after="after",
            models=["string"],
        )
        assert_matches_type(GatewaysGetGatewaysResponseBody, gateway, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.gateways.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = await response.parse()
        assert_matches_type(GatewaysGetGatewaysResponseBody, gateway, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.gateways.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = await response.parse()
            assert_matches_type(GatewaysGetGatewaysResponseBody, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_activate(self, async_client: AsyncSamsara) -> None:
        gateway = await async_client.gateways.activate(
            serial="GFRV-43N-VGX",
        )
        assert_matches_type(GatewaysPostGatewayResponseBody, gateway, path=["response"])

    @parametrize
    async def test_raw_response_activate(self, async_client: AsyncSamsara) -> None:
        response = await async_client.gateways.with_raw_response.activate(
            serial="GFRV-43N-VGX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = await response.parse()
        assert_matches_type(GatewaysPostGatewayResponseBody, gateway, path=["response"])

    @parametrize
    async def test_streaming_response_activate(self, async_client: AsyncSamsara) -> None:
        async with async_client.gateways.with_streaming_response.activate(
            serial="GFRV-43N-VGX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = await response.parse()
            assert_matches_type(GatewaysPostGatewayResponseBody, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_deactivate(self, async_client: AsyncSamsara) -> None:
        gateway = await async_client.gateways.deactivate(
            "bFXA-lFw-EV3",
        )
        assert gateway is None

    @parametrize
    async def test_raw_response_deactivate(self, async_client: AsyncSamsara) -> None:
        response = await async_client.gateways.with_raw_response.deactivate(
            "bFXA-lFw-EV3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = await response.parse()
        assert gateway is None

    @parametrize
    async def test_streaming_response_deactivate(self, async_client: AsyncSamsara) -> None:
        async with async_client.gateways.with_streaming_response.deactivate(
            "bFXA-lFw-EV3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = await response.parse()
            assert gateway is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_deactivate(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.gateways.with_raw_response.deactivate(
                "",
            )
