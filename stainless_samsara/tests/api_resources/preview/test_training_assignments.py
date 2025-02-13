# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.preview import (
    TrainingAssignmentsPatchTrainingAssignmentsResponseBody,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrainingAssignments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        training_assignment = client.preview.training_assignments.update(
            due_at_time="dueAtTime",
            ids=["string"],
        )
        assert_matches_type(
            TrainingAssignmentsPatchTrainingAssignmentsResponseBody, training_assignment, path=["response"]
        )

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.preview.training_assignments.with_raw_response.update(
            due_at_time="dueAtTime",
            ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_assignment = response.parse()
        assert_matches_type(
            TrainingAssignmentsPatchTrainingAssignmentsResponseBody, training_assignment, path=["response"]
        )

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.preview.training_assignments.with_streaming_response.update(
            due_at_time="dueAtTime",
            ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_assignment = response.parse()
            assert_matches_type(
                TrainingAssignmentsPatchTrainingAssignmentsResponseBody, training_assignment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Samsara) -> None:
        training_assignment = client.preview.training_assignments.delete(
            ids=["string"],
        )
        assert training_assignment is None

    @parametrize
    def test_raw_response_delete(self, client: Samsara) -> None:
        response = client.preview.training_assignments.with_raw_response.delete(
            ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_assignment = response.parse()
        assert training_assignment is None

    @parametrize
    def test_streaming_response_delete(self, client: Samsara) -> None:
        with client.preview.training_assignments.with_streaming_response.delete(
            ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_assignment = response.parse()
            assert training_assignment is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTrainingAssignments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        training_assignment = await async_client.preview.training_assignments.update(
            due_at_time="dueAtTime",
            ids=["string"],
        )
        assert_matches_type(
            TrainingAssignmentsPatchTrainingAssignmentsResponseBody, training_assignment, path=["response"]
        )

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.preview.training_assignments.with_raw_response.update(
            due_at_time="dueAtTime",
            ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_assignment = await response.parse()
        assert_matches_type(
            TrainingAssignmentsPatchTrainingAssignmentsResponseBody, training_assignment, path=["response"]
        )

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.preview.training_assignments.with_streaming_response.update(
            due_at_time="dueAtTime",
            ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_assignment = await response.parse()
            assert_matches_type(
                TrainingAssignmentsPatchTrainingAssignmentsResponseBody, training_assignment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSamsara) -> None:
        training_assignment = await async_client.preview.training_assignments.delete(
            ids=["string"],
        )
        assert training_assignment is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSamsara) -> None:
        response = await async_client.preview.training_assignments.with_raw_response.delete(
            ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_assignment = await response.parse()
        assert training_assignment is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSamsara) -> None:
        async with async_client.preview.training_assignments.with_streaming_response.delete(
            ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_assignment = await response.parse()
            assert training_assignment is None

        assert cast(Any, response.is_closed) is True
