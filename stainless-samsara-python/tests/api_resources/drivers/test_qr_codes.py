# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.drivers import (
    QrCodeListResponse,
    QrCodeCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQrCodes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        qr_code = client.drivers.qr_codes.create(
            driver_id=494123,
        )
        assert_matches_type(QrCodeCreateResponse, qr_code, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.drivers.qr_codes.with_raw_response.create(
            driver_id=494123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qr_code = response.parse()
        assert_matches_type(QrCodeCreateResponse, qr_code, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.drivers.qr_codes.with_streaming_response.create(
            driver_id=494123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qr_code = response.parse()
            assert_matches_type(QrCodeCreateResponse, qr_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        qr_code = client.drivers.qr_codes.list(
            driver_ids=["string"],
        )
        assert_matches_type(QrCodeListResponse, qr_code, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.drivers.qr_codes.with_raw_response.list(
            driver_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qr_code = response.parse()
        assert_matches_type(QrCodeListResponse, qr_code, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.drivers.qr_codes.with_streaming_response.list(
            driver_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qr_code = response.parse()
            assert_matches_type(QrCodeListResponse, qr_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_revoke(self, client: Samsara) -> None:
        qr_code = client.drivers.qr_codes.revoke(
            driver_id=494123,
        )
        assert qr_code is None

    @parametrize
    def test_raw_response_revoke(self, client: Samsara) -> None:
        response = client.drivers.qr_codes.with_raw_response.revoke(
            driver_id=494123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qr_code = response.parse()
        assert qr_code is None

    @parametrize
    def test_streaming_response_revoke(self, client: Samsara) -> None:
        with client.drivers.qr_codes.with_streaming_response.revoke(
            driver_id=494123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qr_code = response.parse()
            assert qr_code is None

        assert cast(Any, response.is_closed) is True


class TestAsyncQrCodes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        qr_code = await async_client.drivers.qr_codes.create(
            driver_id=494123,
        )
        assert_matches_type(QrCodeCreateResponse, qr_code, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.drivers.qr_codes.with_raw_response.create(
            driver_id=494123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qr_code = await response.parse()
        assert_matches_type(QrCodeCreateResponse, qr_code, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.drivers.qr_codes.with_streaming_response.create(
            driver_id=494123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qr_code = await response.parse()
            assert_matches_type(QrCodeCreateResponse, qr_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        qr_code = await async_client.drivers.qr_codes.list(
            driver_ids=["string"],
        )
        assert_matches_type(QrCodeListResponse, qr_code, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.drivers.qr_codes.with_raw_response.list(
            driver_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qr_code = await response.parse()
        assert_matches_type(QrCodeListResponse, qr_code, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.drivers.qr_codes.with_streaming_response.list(
            driver_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qr_code = await response.parse()
            assert_matches_type(QrCodeListResponse, qr_code, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_revoke(self, async_client: AsyncSamsara) -> None:
        qr_code = await async_client.drivers.qr_codes.revoke(
            driver_id=494123,
        )
        assert qr_code is None

    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncSamsara) -> None:
        response = await async_client.drivers.qr_codes.with_raw_response.revoke(
            driver_id=494123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        qr_code = await response.parse()
        assert qr_code is None

    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncSamsara) -> None:
        async with async_client.drivers.qr_codes.with_streaming_response.revoke(
            driver_id=494123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            qr_code = await response.parse()
            assert qr_code is None

        assert cast(Any, response.is_closed) is True
