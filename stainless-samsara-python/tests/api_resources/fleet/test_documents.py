# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from samsara import Samsara, AsyncSamsara
from tests.utils import assert_matches_type
from samsara._utils import parse_datetime
from samsara.types.fleet import (
    DocumentListResponse,
    DocumentCreateResponse,
    DocumentRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Samsara) -> None:
        document = client.fleet.documents.create(
            document_type_id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            driver_id="45646",
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Samsara) -> None:
        document = client.fleet.documents.create(
            document_type_id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            driver_id="45646",
            fields=[
                {
                    "label": "Load weight",
                    "type": "photo",
                    "value": {
                        "barcode_value": [
                            {
                                "barcode_type": "org.gs1.EAN-13",
                                "barcode_value": "0853883003114",
                            }
                        ],
                        "date_time_value": {"date_time": parse_datetime("1996-02-22T20:14:42Z")},
                        "multiple_choice_value": [
                            {
                                "selected": False,
                                "value": "Yes",
                            }
                        ],
                        "number_value": 123.456,
                        "photo_value": [
                            {
                                "id": "f5271458-21f9-4a9f-a290-780c6d8840ff",
                                "url": "https://samsara-driver-media-upload.s3.us-west-2.amazonaws.com/123456",
                            }
                        ],
                        "scanned_document_value": [
                            {
                                "id": "f5271458-21f9-4a9f-a290-780c6d8840ff",
                                "url": "https://samsara-driver-media-upload.s3.us-west-2.amazonaws.com/123456",
                            }
                        ],
                        "signature_value": {
                            "id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                            "name": "John Smith",
                            "signed_at_time": parse_datetime("2010-07-18T06:13:42Z"),
                            "url": "https://samsara-driver-media-upload.s3.us-west-2.amazonaws.com/123456",
                        },
                        "string_value": "Red Truck",
                    },
                }
            ],
            name="Dropoff Slip 123",
            notes="Missing a crate",
            route_stop_id="45646",
            state="submitted",
            vehicle_id="45646",
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Samsara) -> None:
        response = client.fleet.documents.with_raw_response.create(
            document_type_id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            driver_id="45646",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Samsara) -> None:
        with client.fleet.documents.with_streaming_response.create(
            document_type_id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            driver_id="45646",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Samsara) -> None:
        document = client.fleet.documents.retrieve(
            "id",
        )
        assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Samsara) -> None:
        response = client.fleet.documents.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Samsara) -> None:
        with client.fleet.documents.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fleet.documents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Samsara) -> None:
        document = client.fleet.documents.list(
            end_time="endTime",
            start_time="startTime",
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Samsara) -> None:
        document = client.fleet.documents.list(
            end_time="endTime",
            start_time="startTime",
            after="after",
            document_type_id="documentTypeId",
            query_by="queryBy",
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Samsara) -> None:
        response = client.fleet.documents.with_raw_response.list(
            end_time="endTime",
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Samsara) -> None:
        with client.fleet.documents.with_streaming_response.list(
            end_time="endTime",
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Samsara) -> None:
        document = client.fleet.documents.delete(
            "id",
        )
        assert document is None

    @parametrize
    def test_raw_response_delete(self, client: Samsara) -> None:
        response = client.fleet.documents.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert document is None

    @parametrize
    def test_streaming_response_delete(self, client: Samsara) -> None:
        with client.fleet.documents.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Samsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.fleet.documents.with_raw_response.delete(
                "",
            )


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSamsara) -> None:
        document = await async_client.fleet.documents.create(
            document_type_id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            driver_id="45646",
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSamsara) -> None:
        document = await async_client.fleet.documents.create(
            document_type_id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            driver_id="45646",
            fields=[
                {
                    "label": "Load weight",
                    "type": "photo",
                    "value": {
                        "barcode_value": [
                            {
                                "barcode_type": "org.gs1.EAN-13",
                                "barcode_value": "0853883003114",
                            }
                        ],
                        "date_time_value": {"date_time": parse_datetime("1996-02-22T20:14:42Z")},
                        "multiple_choice_value": [
                            {
                                "selected": False,
                                "value": "Yes",
                            }
                        ],
                        "number_value": 123.456,
                        "photo_value": [
                            {
                                "id": "f5271458-21f9-4a9f-a290-780c6d8840ff",
                                "url": "https://samsara-driver-media-upload.s3.us-west-2.amazonaws.com/123456",
                            }
                        ],
                        "scanned_document_value": [
                            {
                                "id": "f5271458-21f9-4a9f-a290-780c6d8840ff",
                                "url": "https://samsara-driver-media-upload.s3.us-west-2.amazonaws.com/123456",
                            }
                        ],
                        "signature_value": {
                            "id": "9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
                            "name": "John Smith",
                            "signed_at_time": parse_datetime("2010-07-18T06:13:42Z"),
                            "url": "https://samsara-driver-media-upload.s3.us-west-2.amazonaws.com/123456",
                        },
                        "string_value": "Red Truck",
                    },
                }
            ],
            name="Dropoff Slip 123",
            notes="Missing a crate",
            route_stop_id="45646",
            state="submitted",
            vehicle_id="45646",
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.documents.with_raw_response.create(
            document_type_id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            driver_id="45646",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.documents.with_streaming_response.create(
            document_type_id="9814a1fa-f0c6-408b-bf85-51dc3bc71ac7",
            driver_id="45646",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSamsara) -> None:
        document = await async_client.fleet.documents.retrieve(
            "id",
        )
        assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.documents.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.documents.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentRetrieveResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fleet.documents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSamsara) -> None:
        document = await async_client.fleet.documents.list(
            end_time="endTime",
            start_time="startTime",
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSamsara) -> None:
        document = await async_client.fleet.documents.list(
            end_time="endTime",
            start_time="startTime",
            after="after",
            document_type_id="documentTypeId",
            query_by="queryBy",
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.documents.with_raw_response.list(
            end_time="endTime",
            start_time="startTime",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.documents.with_streaming_response.list(
            end_time="endTime",
            start_time="startTime",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSamsara) -> None:
        document = await async_client.fleet.documents.delete(
            "id",
        )
        assert document is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSamsara) -> None:
        response = await async_client.fleet.documents.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert document is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSamsara) -> None:
        async with async_client.fleet.documents.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert document is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSamsara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.fleet.documents.with_raw_response.delete(
                "",
            )
