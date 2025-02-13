# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.fleet.trailers import InlineResponse200_7, V1TrailerAssignmentsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssignments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        assignment = client.trailers.assignments.retrieve(
            trailer_id=0,
        )
        assert_matches_type(V1TrailerAssignmentsResponse, assignment, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Samsara) -> None:
        assignment = client.trailers.assignments.retrieve(
            trailer_id=0,
            end_ms=0,
            start_ms=0,
        )
        assert_matches_type(V1TrailerAssignmentsResponse, assignment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.trailers.assignments.with_raw_response.retrieve(
            trailer_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignment = response.parse()
        assert_matches_type(V1TrailerAssignmentsResponse, assignment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.trailers.assignments.with_streaming_response.retrieve(
            trailer_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignment = response.parse()
            assert_matches_type(V1TrailerAssignmentsResponse, assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        assignment = client.trailers.assignments.list()
        assert_matches_type(InlineResponse200_7, assignment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        assignment = client.trailers.assignments.list(
            ending_before="endingBefore",
            end_ms=0,
            limit=0,
            starting_after="startingAfter",
            start_ms=0,
        )
        assert_matches_type(InlineResponse200_7, assignment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.trailers.assignments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignment = response.parse()
        assert_matches_type(InlineResponse200_7, assignment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.trailers.assignments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignment = response.parse()
            assert_matches_type(InlineResponse200_7, assignment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAssignments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        assignment = await async_client.trailers.assignments.retrieve(
            trailer_id=0,
        )
        assert_matches_type(V1TrailerAssignmentsResponse, assignment, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSamsara) -> None:
        assignment = await async_client.trailers.assignments.retrieve(
            trailer_id=0,
            end_ms=0,
            start_ms=0,
        )
        assert_matches_type(V1TrailerAssignmentsResponse, assignment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.trailers.assignments.with_raw_response.retrieve(
            trailer_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignment = await response.parse()
        assert_matches_type(V1TrailerAssignmentsResponse, assignment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.trailers.assignments.with_streaming_response.retrieve(
            trailer_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignment = await response.parse()
            assert_matches_type(V1TrailerAssignmentsResponse, assignment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        assignment = await async_client.trailers.assignments.list()
        assert_matches_type(InlineResponse200_7, assignment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        assignment = await async_client.trailers.assignments.list(
            ending_before="endingBefore",
            end_ms=0,
            limit=0,
            starting_after="startingAfter",
            start_ms=0,
        )
        assert_matches_type(InlineResponse200_7, assignment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.trailers.assignments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        assignment = await response.parse()
        assert_matches_type(InlineResponse200_7, assignment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.trailers.assignments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            assignment = await response.parse()
            assert_matches_type(InlineResponse200_7, assignment, path=["response"])

        assert cast(Any, response.is_closed) is True
