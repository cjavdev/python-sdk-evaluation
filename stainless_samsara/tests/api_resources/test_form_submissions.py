# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types import (
    FormSubmissionStreamResponse,
    FormSubmissionsGetFormSubmissionsResponseBody,
    FormSubmissionsPostFormSubmissionResponseBody,
    FormSubmissionsPatchFormSubmissionResponseBody,
)
from samsara._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFormSubmissions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        form_submission = client.form_submissions.create(
            form_template={
                "id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                "revision_id": "1214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            },
            status="toDo",
        )
        assert_matches_type(FormSubmissionsPostFormSubmissionResponseBody, form_submission, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        form_submission = client.form_submissions.create(
            form_template={
                "id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                "revision_id": "1214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            },
            status="toDo",
            assigned_to={
                "id": "938172",
                "type": "driver",
            },
            due_at_time=parse_datetime("2019-06-13T19:08:25Z"),
            fields=[
                {
                    "id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                    "type": "number",
                    "asset_value": {"asset": {"id": "281474982859091"}},
                    "check_boxes_value": {
                        "value_ids": [
                            "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                            "1214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                            "2214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                            "3214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                        ]
                    },
                    "date_time_value": {"value": parse_datetime("2019-06-13T19:08:25Z")},
                    "multiple_choice_value": {"value_id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7"},
                    "number_value": {"value": 123.456},
                    "person_value": {"person": {"polymorphic_user_id": "user-12345"}},
                    "table_value": {
                        "rows": [
                            {
                                "id": "ee62df83-16e8-46ae-94d6-4933848f5e66",
                                "cells": [
                                    {
                                        "id": "9fac4466-9d85-4768-9f1f-ff8f757f70c4",
                                        "type": "number",
                                        "check_boxes_value": {
                                            "value_ids": [
                                                "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                                                "1214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                                                "2214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                                                "3214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                                            ]
                                        },
                                        "date_time_value": {"value": parse_datetime("2019-06-13T19:08:25Z")},
                                        "multiple_choice_value": {"value_id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7"},
                                        "number_value": {"value": 123.456},
                                        "person_value": {"person": {"polymorphic_user_id": "user-12345"}},
                                        "text_value": {"value": "Exposed wires"},
                                    }
                                ],
                            }
                        ]
                    },
                    "text_value": {"value": "Exposed wires"},
                }
            ],
            title="Job - J999",
        )
        assert_matches_type(FormSubmissionsPostFormSubmissionResponseBody, form_submission, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.form_submissions.with_raw_response.create(
            form_template={
                "id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                "revision_id": "1214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            },
            status="toDo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form_submission = response.parse()
        assert_matches_type(FormSubmissionsPostFormSubmissionResponseBody, form_submission, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.form_submissions.with_streaming_response.create(
            form_template={
                "id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                "revision_id": "1214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            },
            status="toDo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form_submission = response.parse()
            assert_matches_type(FormSubmissionsPostFormSubmissionResponseBody, form_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        form_submission = client.form_submissions.update(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
        )
        assert_matches_type(FormSubmissionsPatchFormSubmissionResponseBody, form_submission, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        form_submission = client.form_submissions.update(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            assigned_to={
                "id": "938172",
                "type": "driver",
            },
            due_at_time=parse_datetime("2019-06-13T19:08:25Z"),
            status="toDo",
            title="Job - J999",
        )
        assert_matches_type(FormSubmissionsPatchFormSubmissionResponseBody, form_submission, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.form_submissions.with_raw_response.update(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form_submission = response.parse()
        assert_matches_type(FormSubmissionsPatchFormSubmissionResponseBody, form_submission, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.form_submissions.with_streaming_response.update(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form_submission = response.parse()
            assert_matches_type(FormSubmissionsPatchFormSubmissionResponseBody, form_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        form_submission = client.form_submissions.list(
            ids=["string"],
        )
        assert_matches_type(FormSubmissionsGetFormSubmissionsResponseBody, form_submission, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        form_submission = client.form_submissions.list(
            ids=["string"],
            include=["string"],
        )
        assert_matches_type(FormSubmissionsGetFormSubmissionsResponseBody, form_submission, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.form_submissions.with_raw_response.list(
            ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form_submission = response.parse()
        assert_matches_type(FormSubmissionsGetFormSubmissionsResponseBody, form_submission, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.form_submissions.with_streaming_response.list(
            ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form_submission = response.parse()
            assert_matches_type(FormSubmissionsGetFormSubmissionsResponseBody, form_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stream(self, client: Samsara) -> None:
        form_submission = client.form_submissions.stream(
            start_time="startTime",
        )
        assert_matches_type(FormSubmissionStreamResponse, form_submission, path=["response"])

    @parametrize
    def test_method_stream_with_all_params(self, client: Samsara) -> None:
        form_submission = client.form_submissions.stream(
            start_time="startTime",
            after="after",
            driver_ids=["string"],
            end_time="endTime",
            form_template_ids=["string"],
            include=["string"],
            user_ids=["string"],
        )
        assert_matches_type(FormSubmissionStreamResponse, form_submission, path=["response"])

    @parametrize
    def test_raw_response_stream(self, client: Samsara) -> None:
        response = client.form_submissions.with_raw_response.stream(
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form_submission = response.parse()
        assert_matches_type(FormSubmissionStreamResponse, form_submission, path=["response"])

    @parametrize
    def test_streaming_response_stream(self, client: Samsara) -> None:
        with client.form_submissions.with_streaming_response.stream(
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form_submission = response.parse()
            assert_matches_type(FormSubmissionStreamResponse, form_submission, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFormSubmissions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        form_submission = await async_client.form_submissions.create(
            form_template={
                "id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                "revision_id": "1214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            },
            status="toDo",
        )
        assert_matches_type(FormSubmissionsPostFormSubmissionResponseBody, form_submission, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        form_submission = await async_client.form_submissions.create(
            form_template={
                "id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                "revision_id": "1214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            },
            status="toDo",
            assigned_to={
                "id": "938172",
                "type": "driver",
            },
            due_at_time=parse_datetime("2019-06-13T19:08:25Z"),
            fields=[
                {
                    "id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                    "type": "number",
                    "asset_value": {"asset": {"id": "281474982859091"}},
                    "check_boxes_value": {
                        "value_ids": [
                            "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                            "1214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                            "2214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                            "3214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                        ]
                    },
                    "date_time_value": {"value": parse_datetime("2019-06-13T19:08:25Z")},
                    "multiple_choice_value": {"value_id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7"},
                    "number_value": {"value": 123.456},
                    "person_value": {"person": {"polymorphic_user_id": "user-12345"}},
                    "table_value": {
                        "rows": [
                            {
                                "id": "ee62df83-16e8-46ae-94d6-4933848f5e66",
                                "cells": [
                                    {
                                        "id": "9fac4466-9d85-4768-9f1f-ff8f757f70c4",
                                        "type": "number",
                                        "check_boxes_value": {
                                            "value_ids": [
                                                "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                                                "1214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                                                "2214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                                                "3214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                                            ]
                                        },
                                        "date_time_value": {"value": parse_datetime("2019-06-13T19:08:25Z")},
                                        "multiple_choice_value": {"value_id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7"},
                                        "number_value": {"value": 123.456},
                                        "person_value": {"person": {"polymorphic_user_id": "user-12345"}},
                                        "text_value": {"value": "Exposed wires"},
                                    }
                                ],
                            }
                        ]
                    },
                    "text_value": {"value": "Exposed wires"},
                }
            ],
            title="Job - J999",
        )
        assert_matches_type(FormSubmissionsPostFormSubmissionResponseBody, form_submission, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.form_submissions.with_raw_response.create(
            form_template={
                "id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                "revision_id": "1214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            },
            status="toDo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form_submission = await response.parse()
        assert_matches_type(FormSubmissionsPostFormSubmissionResponseBody, form_submission, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.form_submissions.with_streaming_response.create(
            form_template={
                "id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                "revision_id": "1214a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            },
            status="toDo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form_submission = await response.parse()
            assert_matches_type(FormSubmissionsPostFormSubmissionResponseBody, form_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        form_submission = await async_client.form_submissions.update(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
        )
        assert_matches_type(FormSubmissionsPatchFormSubmissionResponseBody, form_submission, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        form_submission = await async_client.form_submissions.update(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            assigned_to={
                "id": "938172",
                "type": "driver",
            },
            due_at_time=parse_datetime("2019-06-13T19:08:25Z"),
            status="toDo",
            title="Job - J999",
        )
        assert_matches_type(FormSubmissionsPatchFormSubmissionResponseBody, form_submission, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.form_submissions.with_raw_response.update(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form_submission = await response.parse()
        assert_matches_type(FormSubmissionsPatchFormSubmissionResponseBody, form_submission, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.form_submissions.with_streaming_response.update(
            id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form_submission = await response.parse()
            assert_matches_type(FormSubmissionsPatchFormSubmissionResponseBody, form_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        form_submission = await async_client.form_submissions.list(
            ids=["string"],
        )
        assert_matches_type(FormSubmissionsGetFormSubmissionsResponseBody, form_submission, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        form_submission = await async_client.form_submissions.list(
            ids=["string"],
            include=["string"],
        )
        assert_matches_type(FormSubmissionsGetFormSubmissionsResponseBody, form_submission, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.form_submissions.with_raw_response.list(
            ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form_submission = await response.parse()
        assert_matches_type(FormSubmissionsGetFormSubmissionsResponseBody, form_submission, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.form_submissions.with_streaming_response.list(
            ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form_submission = await response.parse()
            assert_matches_type(FormSubmissionsGetFormSubmissionsResponseBody, form_submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stream(self, async_client: AsyncSamsara) -> None:
        form_submission = await async_client.form_submissions.stream(
            start_time="startTime",
        )
        assert_matches_type(FormSubmissionStreamResponse, form_submission, path=["response"])

    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncSamsara) -> None:
        form_submission = await async_client.form_submissions.stream(
            start_time="startTime",
            after="after",
            driver_ids=["string"],
            end_time="endTime",
            form_template_ids=["string"],
            include=["string"],
            user_ids=["string"],
        )
        assert_matches_type(FormSubmissionStreamResponse, form_submission, path=["response"])

    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncSamsara) -> None:
        response = await async_client.form_submissions.with_raw_response.stream(
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form_submission = await response.parse()
        assert_matches_type(FormSubmissionStreamResponse, form_submission, path=["response"])

    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncSamsara) -> None:
        async with async_client.form_submissions.with_streaming_response.stream(
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form_submission = await response.parse()
            assert_matches_type(FormSubmissionStreamResponse, form_submission, path=["response"])

        assert cast(Any, response.is_closed) is True
