# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara._utils import parse_datetime
from samsara.types.fleet import (
    RouteListResponse,
    RouteCreateResponse,
    RouteRetrieveResponse,
    RoutesPatchRouteResponseBody,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        route = client.fleet.routes.create(
            name="Bid 123",
            stops=[{}, {}],
        )
        assert_matches_type(RouteCreateResponse, route, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        route = client.fleet.routes.create(
            name="Bid 123",
            stops=[
                {
                    "address_id": "45934",
                    "external_ids": {"foo": "string"},
                    "name": "Stop #1",
                    "notes": "These are my notes",
                    "ontime_window_after_arrival_ms": 300000,
                    "ontime_window_before_arrival_ms": 300000,
                    "scheduled_arrival_time": parse_datetime("2019-06-13T19:08:25Z"),
                    "scheduled_departure_time": parse_datetime("2019-06-13T19:08:25Z"),
                    "single_use_location": {
                        "latitude": 123.456,
                        "longitude": 37.459,
                        "address": "1234 Main St, San Jose, CA",
                    },
                },
                {
                    "address_id": "45934",
                    "external_ids": {"foo": "string"},
                    "name": "Stop #1",
                    "notes": "These are my notes",
                    "ontime_window_after_arrival_ms": 300000,
                    "ontime_window_before_arrival_ms": 300000,
                    "scheduled_arrival_time": parse_datetime("2019-06-13T19:08:25Z"),
                    "scheduled_departure_time": parse_datetime("2019-06-13T19:08:25Z"),
                    "single_use_location": {
                        "latitude": 123.456,
                        "longitude": 37.459,
                        "address": "1234 Main St, San Jose, CA",
                    },
                },
            ],
            driver_id="1234",
            external_ids={"foo": "string"},
            notes="These are my notes",
            settings={
                "route_completion_condition": "arriveLastStop",
                "route_starting_condition": "departFirstStop",
            },
            vehicle_id="453546",
        )
        assert_matches_type(RouteCreateResponse, route, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.fleet.routes.with_raw_response.create(
            name="Bid 123",
            stops=[{}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteCreateResponse, route, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.fleet.routes.with_streaming_response.create(
            name="Bid 123",
            stops=[{}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteCreateResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        route = client.fleet.routes.retrieve(
            "id",
        )
        assert_matches_type(RouteRetrieveResponse, route, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.fleet.routes.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteRetrieveResponse, route, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.fleet.routes.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteRetrieveResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fleet.routes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        route = client.fleet.routes.update(
            id="id",
        )
        assert_matches_type(RoutesPatchRouteResponseBody, route, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        route = client.fleet.routes.update(
            id="id",
            driver_id="1234",
            external_ids={"foo": "string"},
            name="Bid 123",
            notes="These are my notes",
            settings={
                "route_completion_condition": "arriveLastStop",
                "route_starting_condition": "departFirstStop",
            },
            stops=[
                {
                    "id": "4125",
                    "address_id": "45934",
                    "external_ids": {"foo": "string"},
                    "name": "Stop #1",
                    "notes": "These are my notes",
                    "ontime_window_after_arrival_ms": 300000,
                    "ontime_window_before_arrival_ms": 300000,
                    "scheduled_arrival_time": parse_datetime("2019-06-13T19:08:25Z"),
                    "scheduled_departure_time": parse_datetime("2019-06-13T19:08:25Z"),
                    "single_use_location": {
                        "latitude": 123.456,
                        "longitude": 37.459,
                        "address": "1234 Main St, San Jose, CA",
                    },
                }
            ],
            vehicle_id="453546",
        )
        assert_matches_type(RoutesPatchRouteResponseBody, route, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.fleet.routes.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RoutesPatchRouteResponseBody, route, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.fleet.routes.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RoutesPatchRouteResponseBody, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fleet.routes.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        route = client.fleet.routes.list(
            end_time="endTime",
            start_time="startTime",
        )
        assert_matches_type(RouteListResponse, route, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        route = client.fleet.routes.list(
            end_time="endTime",
            start_time="startTime",
            after="after",
            limit=1,
        )
        assert_matches_type(RouteListResponse, route, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.fleet.routes.with_raw_response.list(
            end_time="endTime",
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert_matches_type(RouteListResponse, route, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.fleet.routes.with_streaming_response.list(
            end_time="endTime",
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert_matches_type(RouteListResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Samsara) -> None:
        route = client.fleet.routes.delete(
            "id",
        )
        assert route is None

    @parametrize
    def test_raw_response_delete(self, client: Samsara) -> None:
        response = client.fleet.routes.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = response.parse()
        assert route is None

    @parametrize
    def test_streaming_response_delete(self, client: Samsara) -> None:
        with client.fleet.routes.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = response.parse()
            assert route is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fleet.routes.with_raw_response.delete(
                "",
            )


class TestAsyncRoutes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        route = await async_client.fleet.routes.create(
            name="Bid 123",
            stops=[{}, {}],
        )
        assert_matches_type(RouteCreateResponse, route, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        route = await async_client.fleet.routes.create(
            name="Bid 123",
            stops=[
                {
                    "address_id": "45934",
                    "external_ids": {"foo": "string"},
                    "name": "Stop #1",
                    "notes": "These are my notes",
                    "ontime_window_after_arrival_ms": 300000,
                    "ontime_window_before_arrival_ms": 300000,
                    "scheduled_arrival_time": parse_datetime("2019-06-13T19:08:25Z"),
                    "scheduled_departure_time": parse_datetime("2019-06-13T19:08:25Z"),
                    "single_use_location": {
                        "latitude": 123.456,
                        "longitude": 37.459,
                        "address": "1234 Main St, San Jose, CA",
                    },
                },
                {
                    "address_id": "45934",
                    "external_ids": {"foo": "string"},
                    "name": "Stop #1",
                    "notes": "These are my notes",
                    "ontime_window_after_arrival_ms": 300000,
                    "ontime_window_before_arrival_ms": 300000,
                    "scheduled_arrival_time": parse_datetime("2019-06-13T19:08:25Z"),
                    "scheduled_departure_time": parse_datetime("2019-06-13T19:08:25Z"),
                    "single_use_location": {
                        "latitude": 123.456,
                        "longitude": 37.459,
                        "address": "1234 Main St, San Jose, CA",
                    },
                },
            ],
            driver_id="1234",
            external_ids={"foo": "string"},
            notes="These are my notes",
            settings={
                "route_completion_condition": "arriveLastStop",
                "route_starting_condition": "departFirstStop",
            },
            vehicle_id="453546",
        )
        assert_matches_type(RouteCreateResponse, route, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.routes.with_raw_response.create(
            name="Bid 123",
            stops=[{}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteCreateResponse, route, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.routes.with_streaming_response.create(
            name="Bid 123",
            stops=[{}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteCreateResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        route = await async_client.fleet.routes.retrieve(
            "id",
        )
        assert_matches_type(RouteRetrieveResponse, route, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.routes.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteRetrieveResponse, route, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.routes.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteRetrieveResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fleet.routes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        route = await async_client.fleet.routes.update(
            id="id",
        )
        assert_matches_type(RoutesPatchRouteResponseBody, route, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        route = await async_client.fleet.routes.update(
            id="id",
            driver_id="1234",
            external_ids={"foo": "string"},
            name="Bid 123",
            notes="These are my notes",
            settings={
                "route_completion_condition": "arriveLastStop",
                "route_starting_condition": "departFirstStop",
            },
            stops=[
                {
                    "id": "4125",
                    "address_id": "45934",
                    "external_ids": {"foo": "string"},
                    "name": "Stop #1",
                    "notes": "These are my notes",
                    "ontime_window_after_arrival_ms": 300000,
                    "ontime_window_before_arrival_ms": 300000,
                    "scheduled_arrival_time": parse_datetime("2019-06-13T19:08:25Z"),
                    "scheduled_departure_time": parse_datetime("2019-06-13T19:08:25Z"),
                    "single_use_location": {
                        "latitude": 123.456,
                        "longitude": 37.459,
                        "address": "1234 Main St, San Jose, CA",
                    },
                }
            ],
            vehicle_id="453546",
        )
        assert_matches_type(RoutesPatchRouteResponseBody, route, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.routes.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RoutesPatchRouteResponseBody, route, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.routes.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RoutesPatchRouteResponseBody, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fleet.routes.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        route = await async_client.fleet.routes.list(
            end_time="endTime",
            start_time="startTime",
        )
        assert_matches_type(RouteListResponse, route, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        route = await async_client.fleet.routes.list(
            end_time="endTime",
            start_time="startTime",
            after="after",
            limit=1,
        )
        assert_matches_type(RouteListResponse, route, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.routes.with_raw_response.list(
            end_time="endTime",
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert_matches_type(RouteListResponse, route, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.routes.with_streaming_response.list(
            end_time="endTime",
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert_matches_type(RouteListResponse, route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSamsara) -> None:
        route = await async_client.fleet.routes.delete(
            "id",
        )
        assert route is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.routes.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        route = await response.parse()
        assert route is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.routes.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            route = await response.parse()
            assert route is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fleet.routes.with_raw_response.delete(
                "",
            )
