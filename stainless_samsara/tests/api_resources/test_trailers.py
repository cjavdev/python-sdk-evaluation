# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet import TrailersGetTrailerResponseBody, TrailersUpdateTrailerResponseBody

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrailers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        trailer = client.trailers.retrieve(
            "id",
        )
        assert_matches_type(TrailersGetTrailerResponseBody, trailer, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.trailers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trailer = response.parse()
        assert_matches_type(TrailersGetTrailerResponseBody, trailer, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.trailers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trailer = response.parse()
            assert_matches_type(TrailersGetTrailerResponseBody, trailer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.trailers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        trailer = client.trailers.update(
            id="id",
        )
        assert_matches_type(TrailersUpdateTrailerResponseBody, trailer, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        trailer = client.trailers.update(
            id="id",
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
            name="Trailer-123",
            notes="These are my trailer notes",
            odometer_meters=1234,
            tag_ids=["Qui ad et et non.", "Et numquam ut.", "Qui eligendi vel ab ut."],
            trailer_serial_number="8V8WD530FLN016251",
        )
        assert_matches_type(TrailersUpdateTrailerResponseBody, trailer, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.trailers.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trailer = response.parse()
        assert_matches_type(TrailersUpdateTrailerResponseBody, trailer, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.trailers.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trailer = response.parse()
            assert_matches_type(TrailersUpdateTrailerResponseBody, trailer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.trailers.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_delete(self, client: Samsara) -> None:
        trailer = client.trailers.delete(
            "id",
        )
        assert trailer is None

    @parametrize
    def test_raw_response_delete(self, client: Samsara) -> None:
        response = client.trailers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trailer = response.parse()
        assert trailer is None

    @parametrize
    def test_streaming_response_delete(self, client: Samsara) -> None:
        with client.trailers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trailer = response.parse()
            assert trailer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.trailers.with_raw_response.delete(
                "",
            )


class TestAsyncTrailers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        trailer = await async_client.trailers.retrieve(
            "id",
        )
        assert_matches_type(TrailersGetTrailerResponseBody, trailer, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.trailers.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trailer = await response.parse()
        assert_matches_type(TrailersGetTrailerResponseBody, trailer, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.trailers.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trailer = await response.parse()
            assert_matches_type(TrailersGetTrailerResponseBody, trailer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.trailers.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        trailer = await async_client.trailers.update(
            id="id",
        )
        assert_matches_type(TrailersUpdateTrailerResponseBody, trailer, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        trailer = await async_client.trailers.update(
            id="id",
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
            name="Trailer-123",
            notes="These are my trailer notes",
            odometer_meters=1234,
            tag_ids=["Qui ad et et non.", "Et numquam ut.", "Qui eligendi vel ab ut."],
            trailer_serial_number="8V8WD530FLN016251",
        )
        assert_matches_type(TrailersUpdateTrailerResponseBody, trailer, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.trailers.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trailer = await response.parse()
        assert_matches_type(TrailersUpdateTrailerResponseBody, trailer, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.trailers.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trailer = await response.parse()
            assert_matches_type(TrailersUpdateTrailerResponseBody, trailer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.trailers.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncSamsara) -> None:
        trailer = await async_client.trailers.delete(
            "id",
        )
        assert trailer is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSamsara) -> None:
        response = await async_client.trailers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trailer = await response.parse()
        assert trailer is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSamsara) -> None:
        async with async_client.trailers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trailer = await response.parse()
            assert trailer is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.trailers.with_raw_response.delete(
                "",
            )
