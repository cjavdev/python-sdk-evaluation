# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet import DvirCreateResponse, DvirResolveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDvirs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        dvir = client.fleet.dvirs.create(
            author_id="11",
            safety_status="safe",
            type="mechanic",
        )
        assert_matches_type(DvirCreateResponse, dvir, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        dvir = client.fleet.dvirs.create(
            author_id="11",
            safety_status="safe",
            type="mechanic",
            license_plate="XHK1234",
            location="350 Rhode Island St Ste. 400S, San Francisco, CA 94103",
            mechanic_notes="Replaced headlight on passenger side.",
            odometer_meters=14010293,
            resolved_defect_ids=["string"],
            trailer_id="11",
            vehicle_id="10",
        )
        assert_matches_type(DvirCreateResponse, dvir, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.fleet.dvirs.with_raw_response.create(
            author_id="11",
            safety_status="safe",
            type="mechanic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dvir = response.parse()
        assert_matches_type(DvirCreateResponse, dvir, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.fleet.dvirs.with_streaming_response.create(
            author_id="11",
            safety_status="safe",
            type="mechanic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dvir = response.parse()
            assert_matches_type(DvirCreateResponse, dvir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_resolve(self, client: Samsara) -> None:
        dvir = client.fleet.dvirs.resolve(
            id="id",
            author_id="11",
            is_resolved=True,
        )
        assert_matches_type(DvirResolveResponse, dvir, path=["response"])

    @parametrize
    def test_method_resolve_with_all_params(self, client: Samsara) -> None:
        dvir = client.fleet.dvirs.resolve(
            id="id",
            author_id="11",
            is_resolved=True,
            mechanic_notes="Replaced headlight on passenger side.",
            signed_at_time="2020-01-27T07:06:25Z",
        )
        assert_matches_type(DvirResolveResponse, dvir, path=["response"])

    @parametrize
    def test_raw_response_resolve(self, client: Samsara) -> None:
        response = client.fleet.dvirs.with_raw_response.resolve(
            id="id",
            author_id="11",
            is_resolved=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dvir = response.parse()
        assert_matches_type(DvirResolveResponse, dvir, path=["response"])

    @parametrize
    def test_streaming_response_resolve(self, client: Samsara) -> None:
        with client.fleet.dvirs.with_streaming_response.resolve(
            id="id",
            author_id="11",
            is_resolved=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dvir = response.parse()
            assert_matches_type(DvirResolveResponse, dvir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resolve(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fleet.dvirs.with_raw_response.resolve(
                id="",
                author_id="11",
                is_resolved=True,
            )


class TestAsyncDvirs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        dvir = await async_client.fleet.dvirs.create(
            author_id="11",
            safety_status="safe",
            type="mechanic",
        )
        assert_matches_type(DvirCreateResponse, dvir, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        dvir = await async_client.fleet.dvirs.create(
            author_id="11",
            safety_status="safe",
            type="mechanic",
            license_plate="XHK1234",
            location="350 Rhode Island St Ste. 400S, San Francisco, CA 94103",
            mechanic_notes="Replaced headlight on passenger side.",
            odometer_meters=14010293,
            resolved_defect_ids=["string"],
            trailer_id="11",
            vehicle_id="10",
        )
        assert_matches_type(DvirCreateResponse, dvir, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.dvirs.with_raw_response.create(
            author_id="11",
            safety_status="safe",
            type="mechanic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dvir = await response.parse()
        assert_matches_type(DvirCreateResponse, dvir, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.dvirs.with_streaming_response.create(
            author_id="11",
            safety_status="safe",
            type="mechanic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dvir = await response.parse()
            assert_matches_type(DvirCreateResponse, dvir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_resolve(self, async_client: AsyncSamsara) -> None:
        dvir = await async_client.fleet.dvirs.resolve(
            id="id",
            author_id="11",
            is_resolved=True,
        )
        assert_matches_type(DvirResolveResponse, dvir, path=["response"])

    @parametrize
    async def test_method_resolve_with_all_params(self, async_client: AsyncSamsara) -> None:
        dvir = await async_client.fleet.dvirs.resolve(
            id="id",
            author_id="11",
            is_resolved=True,
            mechanic_notes="Replaced headlight on passenger side.",
            signed_at_time="2020-01-27T07:06:25Z",
        )
        assert_matches_type(DvirResolveResponse, dvir, path=["response"])

    @parametrize
    async def test_raw_response_resolve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.dvirs.with_raw_response.resolve(
            id="id",
            author_id="11",
            is_resolved=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dvir = await response.parse()
        assert_matches_type(DvirResolveResponse, dvir, path=["response"])

    @parametrize
    async def test_streaming_response_resolve(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.dvirs.with_streaming_response.resolve(
            id="id",
            author_id="11",
            is_resolved=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dvir = await response.parse()
            assert_matches_type(DvirResolveResponse, dvir, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resolve(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fleet.dvirs.with_raw_response.resolve(
                id="",
                author_id="11",
                is_resolved=True,
            )
