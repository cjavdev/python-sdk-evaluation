# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import (
    Door,
    Cargo,
    Sensor,
    Humidity,
    Temperature,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSensors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        sensor = client.sensors.list()
        assert_matches_type(Sensor, sensor, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.sensors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert_matches_type(Sensor, sensor, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.sensors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert_matches_type(Sensor, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_createcargostatus(self, client: Samsara) -> None:
        sensor = client.sensors.createcargostatus(
            sensors=[122],
        )
        assert_matches_type(Cargo, sensor, path=["response"])

    @parametrize
    def test_raw_response_createcargostatus(self, client: Samsara) -> None:
        response = client.sensors.with_raw_response.createcargostatus(
            sensors=[122],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert_matches_type(Cargo, sensor, path=["response"])

    @parametrize
    def test_streaming_response_createcargostatus(self, client: Samsara) -> None:
        with client.sensors.with_streaming_response.createcargostatus(
            sensors=[122],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert_matches_type(Cargo, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_createdoorstatus(self, client: Samsara) -> None:
        sensor = client.sensors.createdoorstatus(
            sensors=[122],
        )
        assert_matches_type(Door, sensor, path=["response"])

    @parametrize
    def test_raw_response_createdoorstatus(self, client: Samsara) -> None:
        response = client.sensors.with_raw_response.createdoorstatus(
            sensors=[122],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert_matches_type(Door, sensor, path=["response"])

    @parametrize
    def test_streaming_response_createdoorstatus(self, client: Samsara) -> None:
        with client.sensors.with_streaming_response.createdoorstatus(
            sensors=[122],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert_matches_type(Door, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_humidity(self, client: Samsara) -> None:
        sensor = client.sensors.humidity(
            sensors=[122],
        )
        assert_matches_type(Humidity, sensor, path=["response"])

    @parametrize
    def test_raw_response_humidity(self, client: Samsara) -> None:
        response = client.sensors.with_raw_response.humidity(
            sensors=[122],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert_matches_type(Humidity, sensor, path=["response"])

    @parametrize
    def test_streaming_response_humidity(self, client: Samsara) -> None:
        with client.sensors.with_streaming_response.humidity(
            sensors=[122],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert_matches_type(Humidity, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_temperature(self, client: Samsara) -> None:
        sensor = client.sensors.temperature(
            sensors=[122],
        )
        assert_matches_type(Temperature, sensor, path=["response"])

    @parametrize
    def test_raw_response_temperature(self, client: Samsara) -> None:
        response = client.sensors.with_raw_response.temperature(
            sensors=[122],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = response.parse()
        assert_matches_type(Temperature, sensor, path=["response"])

    @parametrize
    def test_streaming_response_temperature(self, client: Samsara) -> None:
        with client.sensors.with_streaming_response.temperature(
            sensors=[122],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = response.parse()
            assert_matches_type(Temperature, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSensors:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        sensor = await async_client.sensors.list()
        assert_matches_type(Sensor, sensor, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.sensors.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert_matches_type(Sensor, sensor, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.sensors.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert_matches_type(Sensor, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_createcargostatus(self, async_client: AsyncSamsara) -> None:
        sensor = await async_client.sensors.createcargostatus(
            sensors=[122],
        )
        assert_matches_type(Cargo, sensor, path=["response"])

    @parametrize
    async def test_raw_response_createcargostatus(self, async_client: AsyncSamsara) -> None:
        response = await async_client.sensors.with_raw_response.createcargostatus(
            sensors=[122],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert_matches_type(Cargo, sensor, path=["response"])

    @parametrize
    async def test_streaming_response_createcargostatus(self, async_client: AsyncSamsara) -> None:
        async with async_client.sensors.with_streaming_response.createcargostatus(
            sensors=[122],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert_matches_type(Cargo, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_createdoorstatus(self, async_client: AsyncSamsara) -> None:
        sensor = await async_client.sensors.createdoorstatus(
            sensors=[122],
        )
        assert_matches_type(Door, sensor, path=["response"])

    @parametrize
    async def test_raw_response_createdoorstatus(self, async_client: AsyncSamsara) -> None:
        response = await async_client.sensors.with_raw_response.createdoorstatus(
            sensors=[122],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert_matches_type(Door, sensor, path=["response"])

    @parametrize
    async def test_streaming_response_createdoorstatus(self, async_client: AsyncSamsara) -> None:
        async with async_client.sensors.with_streaming_response.createdoorstatus(
            sensors=[122],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert_matches_type(Door, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_humidity(self, async_client: AsyncSamsara) -> None:
        sensor = await async_client.sensors.humidity(
            sensors=[122],
        )
        assert_matches_type(Humidity, sensor, path=["response"])

    @parametrize
    async def test_raw_response_humidity(self, async_client: AsyncSamsara) -> None:
        response = await async_client.sensors.with_raw_response.humidity(
            sensors=[122],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert_matches_type(Humidity, sensor, path=["response"])

    @parametrize
    async def test_streaming_response_humidity(self, async_client: AsyncSamsara) -> None:
        async with async_client.sensors.with_streaming_response.humidity(
            sensors=[122],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert_matches_type(Humidity, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_temperature(self, async_client: AsyncSamsara) -> None:
        sensor = await async_client.sensors.temperature(
            sensors=[122],
        )
        assert_matches_type(Temperature, sensor, path=["response"])

    @parametrize
    async def test_raw_response_temperature(self, async_client: AsyncSamsara) -> None:
        response = await async_client.sensors.with_raw_response.temperature(
            sensors=[122],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sensor = await response.parse()
        assert_matches_type(Temperature, sensor, path=["response"])

    @parametrize
    async def test_streaming_response_temperature(self, async_client: AsyncSamsara) -> None:
        async with async_client.sensors.with_streaming_response.temperature(
            sensors=[122],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sensor = await response.parse()
            assert_matches_type(Temperature, sensor, path=["response"])

        assert cast(Any, response.is_closed) is True
