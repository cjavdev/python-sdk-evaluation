# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet.documents import PdfCreateResponse, PdfRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPdfs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        pdf = client.fleet.documents.pdfs.create(
            document_id="6c8c0c01-206a-41a4-9d21-15b9978d04cb",
        )
        assert_matches_type(PdfCreateResponse, pdf, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.fleet.documents.pdfs.with_raw_response.create(
            document_id="6c8c0c01-206a-41a4-9d21-15b9978d04cb",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pdf = response.parse()
        assert_matches_type(PdfCreateResponse, pdf, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.fleet.documents.pdfs.with_streaming_response.create(
            document_id="6c8c0c01-206a-41a4-9d21-15b9978d04cb",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pdf = response.parse()
            assert_matches_type(PdfCreateResponse, pdf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        pdf = client.fleet.documents.pdfs.retrieve(
            "id",
        )
        assert_matches_type(PdfRetrieveResponse, pdf, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.fleet.documents.pdfs.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pdf = response.parse()
        assert_matches_type(PdfRetrieveResponse, pdf, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.fleet.documents.pdfs.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pdf = response.parse()
            assert_matches_type(PdfRetrieveResponse, pdf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fleet.documents.pdfs.with_raw_response.retrieve(
                "",
            )


class TestAsyncPdfs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        pdf = await async_client.fleet.documents.pdfs.create(
            document_id="6c8c0c01-206a-41a4-9d21-15b9978d04cb",
        )
        assert_matches_type(PdfCreateResponse, pdf, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.documents.pdfs.with_raw_response.create(
            document_id="6c8c0c01-206a-41a4-9d21-15b9978d04cb",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pdf = await response.parse()
        assert_matches_type(PdfCreateResponse, pdf, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.documents.pdfs.with_streaming_response.create(
            document_id="6c8c0c01-206a-41a4-9d21-15b9978d04cb",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pdf = await response.parse()
            assert_matches_type(PdfCreateResponse, pdf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        pdf = await async_client.fleet.documents.pdfs.retrieve(
            "id",
        )
        assert_matches_type(PdfRetrieveResponse, pdf, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.documents.pdfs.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pdf = await response.parse()
        assert_matches_type(PdfRetrieveResponse, pdf, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.documents.pdfs.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pdf = await response.parse()
            assert_matches_type(PdfRetrieveResponse, pdf, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fleet.documents.pdfs.with_raw_response.retrieve(
                "",
            )
