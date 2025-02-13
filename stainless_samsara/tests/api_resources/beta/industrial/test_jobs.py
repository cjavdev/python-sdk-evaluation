# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara.types.beta.industrial import (
    Job,
    JobCreateResponse,
    JobDeleteResponse,
    JobUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        job = client.beta.industrial.jobs.create(
            job={
                "id": "8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
                "end_date": "2019-06-13T19:08:25Z",
                "name": "My Job Name",
                "start_date": "2019-06-13T19:08:25Z",
            },
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        job = client.beta.industrial.jobs.create(
            job={
                "id": "8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
                "end_date": "2019-06-13T19:08:25Z",
                "name": "My Job Name",
                "start_date": "2019-06-13T19:08:25Z",
                "address": {
                    "address": "1990 Alameda st, San Francisco, Ca 94103",
                    "latitude": 37.456345,
                    "longitude": 34.5633749,
                    "name": "Worksite #1",
                },
                "customer_name": "Samsara",
                "fleet_device_ids": [1234567, 654321],
                "industrial_asset_ids": [
                    "8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
                    "ba84a7e2-9c8d-481f-a248-7cce6b22be9d",
                ],
                "notes": "These are my notes",
                "ontime_window_after_arrival_ms": 300000,
                "ontime_window_before_arrival_ms": 300000,
            },
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.beta.industrial.jobs.with_raw_response.create(
            job={
                "id": "8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
                "end_date": "2019-06-13T19:08:25Z",
                "name": "My Job Name",
                "start_date": "2019-06-13T19:08:25Z",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.beta.industrial.jobs.with_streaming_response.create(
            job={
                "id": "8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
                "end_date": "2019-06-13T19:08:25Z",
                "name": "My Job Name",
                "start_date": "2019-06-13T19:08:25Z",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Samsara) -> None:
        job = client.beta.industrial.jobs.update(
            id="id",
            job={},
        )
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Samsara) -> None:
        job = client.beta.industrial.jobs.update(
            id="id",
            job={
                "id": "8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
                "address": {
                    "address": "1990 Alameda st, San Francisco, Ca 94103",
                    "latitude": 37.456345,
                    "longitude": 34.5633749,
                    "name": "Worksite #1",
                },
                "customer_name": "Samsara",
                "end_date": "2019-06-13T19:08:25Z",
                "fleet_device_ids": [1234567, 654321],
                "industrial_asset_ids": [
                    "8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
                    "ba84a7e2-9c8d-481f-a248-7cce6b22be9d",
                ],
                "name": "My Job Name",
                "notes": "These are my notes",
                "ontime_window_after_arrival_ms": 300000,
                "ontime_window_before_arrival_ms": 300000,
                "start_date": "2019-06-13T19:08:25Z",
            },
            keep_history=True,
        )
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Samsara) -> None:
        response = client.beta.industrial.jobs.with_raw_response.update(
            id="id",
            job={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Samsara) -> None:
        with client.beta.industrial.jobs.with_streaming_response.update(
            id="id",
            job={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobUpdateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        job = client.beta.industrial.jobs.list()
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        job = client.beta.industrial.jobs.list(
            id="id",
            after="after",
            customer_name="customerName",
            end_date="endDate",
            fleet_device_ids=[0],
            industrial_asset_ids=["string"],
            start_date="startDate",
            status="active",
        )
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.beta.industrial.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.beta.industrial.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Job, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Samsara) -> None:
        job = client.beta.industrial.jobs.delete(
            id="id",
        )
        assert_matches_type(JobDeleteResponse, job, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Samsara) -> None:
        response = client.beta.industrial.jobs.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobDeleteResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Samsara) -> None:
        with client.beta.industrial.jobs.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobDeleteResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        job = await async_client.beta.industrial.jobs.create(
            job={
                "id": "8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
                "end_date": "2019-06-13T19:08:25Z",
                "name": "My Job Name",
                "start_date": "2019-06-13T19:08:25Z",
            },
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        job = await async_client.beta.industrial.jobs.create(
            job={
                "id": "8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
                "end_date": "2019-06-13T19:08:25Z",
                "name": "My Job Name",
                "start_date": "2019-06-13T19:08:25Z",
                "address": {
                    "address": "1990 Alameda st, San Francisco, Ca 94103",
                    "latitude": 37.456345,
                    "longitude": 34.5633749,
                    "name": "Worksite #1",
                },
                "customer_name": "Samsara",
                "fleet_device_ids": [1234567, 654321],
                "industrial_asset_ids": [
                    "8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
                    "ba84a7e2-9c8d-481f-a248-7cce6b22be9d",
                ],
                "notes": "These are my notes",
                "ontime_window_after_arrival_ms": 300000,
                "ontime_window_before_arrival_ms": 300000,
            },
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.beta.industrial.jobs.with_raw_response.create(
            job={
                "id": "8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
                "end_date": "2019-06-13T19:08:25Z",
                "name": "My Job Name",
                "start_date": "2019-06-13T19:08:25Z",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.beta.industrial.jobs.with_streaming_response.create(
            job={
                "id": "8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
                "end_date": "2019-06-13T19:08:25Z",
                "name": "My Job Name",
                "start_date": "2019-06-13T19:08:25Z",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncSamsara) -> None:
        job = await async_client.beta.industrial.jobs.update(
            id="id",
            job={},
        )
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSamsara) -> None:
        job = await async_client.beta.industrial.jobs.update(
            id="id",
            job={
                "id": "8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
                "address": {
                    "address": "1990 Alameda st, San Francisco, Ca 94103",
                    "latitude": 37.456345,
                    "longitude": 34.5633749,
                    "name": "Worksite #1",
                },
                "customer_name": "Samsara",
                "end_date": "2019-06-13T19:08:25Z",
                "fleet_device_ids": [1234567, 654321],
                "industrial_asset_ids": [
                    "8d218e6c-7a16-4f9f-90f7-cc1d93b9e596",
                    "ba84a7e2-9c8d-481f-a248-7cce6b22be9d",
                ],
                "name": "My Job Name",
                "notes": "These are my notes",
                "ontime_window_after_arrival_ms": 300000,
                "ontime_window_before_arrival_ms": 300000,
                "start_date": "2019-06-13T19:08:25Z",
            },
            keep_history=True,
        )
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSamsara) -> None:
        response = await async_client.beta.industrial.jobs.with_raw_response.update(
            id="id",
            job={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobUpdateResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSamsara) -> None:
        async with async_client.beta.industrial.jobs.with_streaming_response.update(
            id="id",
            job={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobUpdateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        job = await async_client.beta.industrial.jobs.list()
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        job = await async_client.beta.industrial.jobs.list(
            id="id",
            after="after",
            customer_name="customerName",
            end_date="endDate",
            fleet_device_ids=[0],
            industrial_asset_ids=["string"],
            start_date="startDate",
            status="active",
        )
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.beta.industrial.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.beta.industrial.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Job, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSamsara) -> None:
        job = await async_client.beta.industrial.jobs.delete(
            id="id",
        )
        assert_matches_type(JobDeleteResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSamsara) -> None:
        response = await async_client.beta.industrial.jobs.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobDeleteResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSamsara) -> None:
        async with async_client.beta.industrial.jobs.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobDeleteResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True
