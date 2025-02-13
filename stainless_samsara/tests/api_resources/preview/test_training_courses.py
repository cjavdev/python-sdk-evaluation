# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.preview import TrainingCoursesGetTrainingCoursesResponseBody

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrainingCourses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        training_course = client.preview.training_courses.list()
        assert_matches_type(TrainingCoursesGetTrainingCoursesResponseBody, training_course, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        training_course = client.preview.training_courses.list(
            after="after",
            category_ids=["string"],
            course_ids=["string"],
            status=["string"],
        )
        assert_matches_type(TrainingCoursesGetTrainingCoursesResponseBody, training_course, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.preview.training_courses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_course = response.parse()
        assert_matches_type(TrainingCoursesGetTrainingCoursesResponseBody, training_course, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.preview.training_courses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_course = response.parse()
            assert_matches_type(TrainingCoursesGetTrainingCoursesResponseBody, training_course, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTrainingCourses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        training_course = await async_client.preview.training_courses.list()
        assert_matches_type(TrainingCoursesGetTrainingCoursesResponseBody, training_course, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        training_course = await async_client.preview.training_courses.list(
            after="after",
            category_ids=["string"],
            course_ids=["string"],
            status=["string"],
        )
        assert_matches_type(TrainingCoursesGetTrainingCoursesResponseBody, training_course, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.preview.training_courses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        training_course = await response.parse()
        assert_matches_type(TrainingCoursesGetTrainingCoursesResponseBody, training_course, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.preview.training_courses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            training_course = await response.parse()
            assert_matches_type(TrainingCoursesGetTrainingCoursesResponseBody, training_course, path=["response"])

        assert cast(Any, response.is_closed) is True
