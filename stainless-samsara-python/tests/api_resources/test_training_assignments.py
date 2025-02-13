# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import (
    TrainingAssignmentsPostTrainingAssignmentsResponseBody,
    TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrainingAssignments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        training_assignment = client.training_assignments.create(
            course_id="courseId",
            due_at_time="dueAtTime",
            learner_ids=["string"],
        )
        assert_matches_type(
            TrainingAssignmentsPostTrainingAssignmentsResponseBody, training_assignment, path=["response"]
        )

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.training_assignments.with_raw_response.create(
            course_id="courseId",
            due_at_time="dueAtTime",
            learner_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_assignment = response.parse()
        assert_matches_type(
            TrainingAssignmentsPostTrainingAssignmentsResponseBody, training_assignment, path=["response"]
        )

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.training_assignments.with_streaming_response.create(
            course_id="courseId",
            due_at_time="dueAtTime",
            learner_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_assignment = response.parse()
            assert_matches_type(
                TrainingAssignmentsPostTrainingAssignmentsResponseBody, training_assignment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stream(self, client: Samsara) -> None:
        training_assignment = client.training_assignments.stream(
            start_time="startTime",
        )
        assert_matches_type(
            TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody, training_assignment, path=["response"]
        )

    @parametrize
    def test_method_stream_with_all_params(self, client: Samsara) -> None:
        training_assignment = client.training_assignments.stream(
            start_time="startTime",
            after="after",
            course_ids=["string"],
            end_time="endTime",
            learner_ids=["string"],
            status=["string"],
        )
        assert_matches_type(
            TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody, training_assignment, path=["response"]
        )

    @parametrize
    def test_raw_response_stream(self, client: Samsara) -> None:
        response = client.training_assignments.with_raw_response.stream(
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_assignment = response.parse()
        assert_matches_type(
            TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody, training_assignment, path=["response"]
        )

    @parametrize
    def test_streaming_response_stream(self, client: Samsara) -> None:
        with client.training_assignments.with_streaming_response.stream(
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_assignment = response.parse()
            assert_matches_type(
                TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody, training_assignment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncTrainingAssignments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        training_assignment = await async_client.training_assignments.create(
            course_id="courseId",
            due_at_time="dueAtTime",
            learner_ids=["string"],
        )
        assert_matches_type(
            TrainingAssignmentsPostTrainingAssignmentsResponseBody, training_assignment, path=["response"]
        )

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.training_assignments.with_raw_response.create(
            course_id="courseId",
            due_at_time="dueAtTime",
            learner_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_assignment = await response.parse()
        assert_matches_type(
            TrainingAssignmentsPostTrainingAssignmentsResponseBody, training_assignment, path=["response"]
        )

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.training_assignments.with_streaming_response.create(
            course_id="courseId",
            due_at_time="dueAtTime",
            learner_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_assignment = await response.parse()
            assert_matches_type(
                TrainingAssignmentsPostTrainingAssignmentsResponseBody, training_assignment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stream(self, async_client: AsyncSamsara) -> None:
        training_assignment = await async_client.training_assignments.stream(
            start_time="startTime",
        )
        assert_matches_type(
            TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody, training_assignment, path=["response"]
        )

    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncSamsara) -> None:
        training_assignment = await async_client.training_assignments.stream(
            start_time="startTime",
            after="after",
            course_ids=["string"],
            end_time="endTime",
            learner_ids=["string"],
            status=["string"],
        )
        assert_matches_type(
            TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody, training_assignment, path=["response"]
        )

    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncSamsara) -> None:
        response = await async_client.training_assignments.with_raw_response.stream(
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_assignment = await response.parse()
        assert_matches_type(
            TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody, training_assignment, path=["response"]
        )

    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncSamsara) -> None:
        async with async_client.training_assignments.with_streaming_response.stream(
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_assignment = await response.parse()
            assert_matches_type(
                TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody, training_assignment, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
