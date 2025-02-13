# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: Samsara) -> None:
        route = client.fleet.dispatch.routes.delete(
            route_id_or_external_id="route_id_or_external_id",
        )
        assert route is None

    @parametrize
    def test_method_delete_with_all_params(self, client: Samsara) -> None:
        route = client.fleet.dispatch.routes.delete(
            route_id_or_external_id="route_id_or_external_id",
            apply_to_future_routes=True,
        )
        assert route is None

    @parametrize
    def test_raw_response_delete(self, client: Samsara) -> None:
        response = client.fleet.dispatch.routes.with_raw_response.delete(
            route_id_or_external_id="route_id_or_external_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert route is None

    @parametrize
    def test_streaming_response_delete(self, client: Samsara) -> None:
        with client.fleet.dispatch.routes.with_streaming_response.delete(
            route_id_or_external_id="route_id_or_external_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert route is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Samsara) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `route_id_or_external_id` but received ''"
        ):
            client.fleet.dispatch.routes.with_raw_response.delete(
                route_id_or_external_id="",
            )


class TestAsyncRoutes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncSamsara) -> None:
        route = await async_client.fleet.dispatch.routes.delete(
            route_id_or_external_id="route_id_or_external_id",
        )
        assert route is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSamsara) -> None:
        route = await async_client.fleet.dispatch.routes.delete(
            route_id_or_external_id="route_id_or_external_id",
            apply_to_future_routes=True,
        )
        assert route is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.dispatch.routes.with_raw_response.delete(
            route_id_or_external_id="route_id_or_external_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert route is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.dispatch.routes.with_streaming_response.delete(
            route_id_or_external_id="route_id_or_external_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert route is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `route_id_or_external_id` but received ''"
        ):
            await async_client.fleet.dispatch.routes.with_raw_response.delete(
                route_id_or_external_id="",
            )
