# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.cameras.media import (
    RetrievalCreateResponse,
    RetrievalRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRetrieval:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        retrieval = client.cameras.media.retrieval.create(
            inputs=["dashcamRoadFacing", "dashcamDriverFacing", "analog"],
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="1234",
        )
        assert_matches_type(RetrievalCreateResponse, retrieval, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        retrieval = client.cameras.media.retrieval.create(
            inputs=["dashcamRoadFacing", "dashcamDriverFacing", "analog"],
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="1234",
            end_time="2019-06-13T19:08:55Z",
        )
        assert_matches_type(RetrievalCreateResponse, retrieval, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.cameras.media.retrieval.with_raw_response.create(
            inputs=["dashcamRoadFacing", "dashcamDriverFacing", "analog"],
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="1234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = response.parse()
        assert_matches_type(RetrievalCreateResponse, retrieval, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.cameras.media.retrieval.with_streaming_response.create(
            inputs=["dashcamRoadFacing", "dashcamDriverFacing", "analog"],
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="1234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = response.parse()
            assert_matches_type(RetrievalCreateResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        retrieval = client.cameras.media.retrieval.retrieve(
            retrieval_id="retrievalId",
        )
        assert_matches_type(RetrievalRetrieveResponse, retrieval, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.cameras.media.retrieval.with_raw_response.retrieve(
            retrieval_id="retrievalId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = response.parse()
        assert_matches_type(RetrievalRetrieveResponse, retrieval, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.cameras.media.retrieval.with_streaming_response.retrieve(
            retrieval_id="retrievalId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = response.parse()
            assert_matches_type(RetrievalRetrieveResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRetrieval:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        retrieval = await async_client.cameras.media.retrieval.create(
            inputs=["dashcamRoadFacing", "dashcamDriverFacing", "analog"],
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="1234",
        )
        assert_matches_type(RetrievalCreateResponse, retrieval, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        retrieval = await async_client.cameras.media.retrieval.create(
            inputs=["dashcamRoadFacing", "dashcamDriverFacing", "analog"],
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="1234",
            end_time="2019-06-13T19:08:55Z",
        )
        assert_matches_type(RetrievalCreateResponse, retrieval, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.cameras.media.retrieval.with_raw_response.create(
            inputs=["dashcamRoadFacing", "dashcamDriverFacing", "analog"],
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="1234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = await response.parse()
        assert_matches_type(RetrievalCreateResponse, retrieval, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.cameras.media.retrieval.with_streaming_response.create(
            inputs=["dashcamRoadFacing", "dashcamDriverFacing", "analog"],
            start_time="2019-06-13T19:08:25Z",
            vehicle_id="1234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = await response.parse()
            assert_matches_type(RetrievalCreateResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        retrieval = await async_client.cameras.media.retrieval.retrieve(
            retrieval_id="retrievalId",
        )
        assert_matches_type(RetrievalRetrieveResponse, retrieval, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.cameras.media.retrieval.with_raw_response.retrieve(
            retrieval_id="retrievalId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = await response.parse()
        assert_matches_type(RetrievalRetrieveResponse, retrieval, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.cameras.media.retrieval.with_streaming_response.retrieve(
            retrieval_id="retrievalId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = await response.parse()
            assert_matches_type(RetrievalRetrieveResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True
