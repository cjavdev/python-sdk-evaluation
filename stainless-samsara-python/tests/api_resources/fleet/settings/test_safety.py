# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet.settings import SafetySettingsGetSafetySettingsResponseBody

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSafety:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        safety = client.fleet.settings.safety.retrieve()
        assert_matches_type(SafetySettingsGetSafetySettingsResponseBody, safety, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.fleet.settings.safety.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        safety = response.parse()
        assert_matches_type(SafetySettingsGetSafetySettingsResponseBody, safety, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.fleet.settings.safety.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            safety = response.parse()
            assert_matches_type(SafetySettingsGetSafetySettingsResponseBody, safety, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSafety:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        safety = await async_client.fleet.settings.safety.retrieve()
        assert_matches_type(SafetySettingsGetSafetySettingsResponseBody, safety, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.settings.safety.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        safety = await response.parse()
        assert_matches_type(SafetySettingsGetSafetySettingsResponseBody, safety, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.settings.safety.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            safety = await response.parse()
            assert_matches_type(SafetySettingsGetSafetySettingsResponseBody, safety, path=["response"])

        assert cast(Any, response.is_closed) is True
