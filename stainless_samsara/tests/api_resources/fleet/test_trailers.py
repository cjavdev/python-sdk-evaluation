# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet import (
    TrailersListTrailersResponseBody,
    TrailersCreateTrailerResponseBody,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrailers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        trailer = client.fleet.trailers.create(
            name="Trailer-123",
        )
        assert_matches_type(TrailersCreateTrailerResponseBody, trailer, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        trailer = client.fleet.trailers.create(
            name="Trailer-123",
            attributes=[
                {
                    "id": "494123",
                    "name": "Compliance/ELD",
                    "number_values": [867, 5309],
                    "string_values": ["HQ", "Leased"],
                }
            ],
            enabled_for_mobile=True,
            external_ids={"foo": "string"},
            license_plate="7TYP290",
            notes="These are my trailer notes",
            tag_ids=["Delectus alias molestiae.", "Nam ut.", "Eum ut qui aut voluptas soluta.", "Quia corrupti."],
            trailer_serial_number="8V8WD530FLN016251",
        )
        assert_matches_type(TrailersCreateTrailerResponseBody, trailer, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.fleet.trailers.with_raw_response.create(
            name="Trailer-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trailer = response.parse()
        assert_matches_type(TrailersCreateTrailerResponseBody, trailer, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.fleet.trailers.with_streaming_response.create(
            name="Trailer-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trailer = response.parse()
            assert_matches_type(TrailersCreateTrailerResponseBody, trailer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        trailer = client.fleet.trailers.list()
        assert_matches_type(TrailersListTrailersResponseBody, trailer, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        trailer = client.fleet.trailers.list(
            after="after",
            limit=1,
            parent_tag_ids="parentTagIds",
            tag_ids="tagIds",
        )
        assert_matches_type(TrailersListTrailersResponseBody, trailer, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.fleet.trailers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trailer = response.parse()
        assert_matches_type(TrailersListTrailersResponseBody, trailer, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.fleet.trailers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trailer = response.parse()
            assert_matches_type(TrailersListTrailersResponseBody, trailer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTrailers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        trailer = await async_client.fleet.trailers.create(
            name="Trailer-123",
        )
        assert_matches_type(TrailersCreateTrailerResponseBody, trailer, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        trailer = await async_client.fleet.trailers.create(
            name="Trailer-123",
            attributes=[
                {
                    "id": "494123",
                    "name": "Compliance/ELD",
                    "number_values": [867, 5309],
                    "string_values": ["HQ", "Leased"],
                }
            ],
            enabled_for_mobile=True,
            external_ids={"foo": "string"},
            license_plate="7TYP290",
            notes="These are my trailer notes",
            tag_ids=["Delectus alias molestiae.", "Nam ut.", "Eum ut qui aut voluptas soluta.", "Quia corrupti."],
            trailer_serial_number="8V8WD530FLN016251",
        )
        assert_matches_type(TrailersCreateTrailerResponseBody, trailer, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.trailers.with_raw_response.create(
            name="Trailer-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trailer = await response.parse()
        assert_matches_type(TrailersCreateTrailerResponseBody, trailer, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.trailers.with_streaming_response.create(
            name="Trailer-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trailer = await response.parse()
            assert_matches_type(TrailersCreateTrailerResponseBody, trailer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        trailer = await async_client.fleet.trailers.list()
        assert_matches_type(TrailersListTrailersResponseBody, trailer, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        trailer = await async_client.fleet.trailers.list(
            after="after",
            limit=1,
            parent_tag_ids="parentTagIds",
            tag_ids="tagIds",
        )
        assert_matches_type(TrailersListTrailersResponseBody, trailer, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.trailers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trailer = await response.parse()
        assert_matches_type(TrailersListTrailersResponseBody, trailer, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.trailers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trailer = await response.parse()
            assert_matches_type(TrailersListTrailersResponseBody, trailer, path=["response"])

        assert cast(Any, response.is_closed) is True
