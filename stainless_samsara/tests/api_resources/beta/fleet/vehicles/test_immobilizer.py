# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImmobilizer:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        immobilizer = client.beta.fleet.vehicles.immobilizer.update(
            id=0,
            relay_states=[
                {
                    "id": "relay1",
                    "is_open": True,
                }
            ],
        )
        assert immobilizer is None

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.beta.fleet.vehicles.immobilizer.with_raw_response.update(
            id=0,
            relay_states=[
                {
                    "id": "relay1",
                    "is_open": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        immobilizer = response.parse()
        assert immobilizer is None

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.beta.fleet.vehicles.immobilizer.with_streaming_response.update(
            id=0,
            relay_states=[
                {
                    "id": "relay1",
                    "is_open": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            immobilizer = response.parse()
            assert immobilizer is None

        assert cast(Any, response.is_closed) is True


class TestAsyncImmobilizer:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        immobilizer = await async_client.beta.fleet.vehicles.immobilizer.update(
            id=0,
            relay_states=[
                {
                    "id": "relay1",
                    "is_open": True,
                }
            ],
        )
        assert immobilizer is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.beta.fleet.vehicles.immobilizer.with_raw_response.update(
            id=0,
            relay_states=[
                {
                    "id": "relay1",
                    "is_open": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        immobilizer = await response.parse()
        assert immobilizer is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.beta.fleet.vehicles.immobilizer.with_streaming_response.update(
            id=0,
            relay_states=[
                {
                    "id": "relay1",
                    "is_open": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            immobilizer = await response.parse()
            assert immobilizer is None

        assert cast(Any, response.is_closed) is True
