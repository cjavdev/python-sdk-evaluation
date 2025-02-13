# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from .data_points import (
    DataPointsResource,
    AsyncDataPointsResource,
    DataPointsResourceWithRawResponse,
    AsyncDataPointsResourceWithRawResponse,
    DataPointsResourceWithStreamingResponse,
    AsyncDataPointsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.industrial import data_input_list_params
from ....types.industrial.data_inputs_tiny_response import DataInputsTinyResponse

__all__ = ["DataInputsResource", "AsyncDataInputsResource"]


class DataInputsResource(SyncAPIResource):
    @cached_property
    def data_points(self) -> DataPointsResource:
        return DataPointsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DataInputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DataInputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataInputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DataInputsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        asset_ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataInputsTinyResponse:
        """
        Returns all data inputs, optionally filtered by tags or asset ids.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Equipment Statistics** under the Equipment
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          asset_ids:
              A comma-separated list of industrial asset UUIDs. Example:
              `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 512 objects.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/industrial/data-inputs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "asset_ids": asset_ids,
                        "limit": limit,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    data_input_list_params.DataInputListParams,
                ),
            ),
            cast_to=DataInputsTinyResponse,
        )


class AsyncDataInputsResource(AsyncAPIResource):
    @cached_property
    def data_points(self) -> AsyncDataPointsResource:
        return AsyncDataPointsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDataInputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataInputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataInputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDataInputsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        asset_ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataInputsTinyResponse:
        """
        Returns all data inputs, optionally filtered by tags or asset ids.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Equipment Statistics** under the Equipment
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          asset_ids:
              A comma-separated list of industrial asset UUIDs. Example:
              `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 512 objects.

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/industrial/data-inputs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "asset_ids": asset_ids,
                        "limit": limit,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    data_input_list_params.DataInputListParams,
                ),
            ),
            cast_to=DataInputsTinyResponse,
        )


class DataInputsResourceWithRawResponse:
    def __init__(self, data_inputs: DataInputsResource) -> None:
        self._data_inputs = data_inputs

        self.list = to_raw_response_wrapper(
            data_inputs.list,
        )

    @cached_property
    def data_points(self) -> DataPointsResourceWithRawResponse:
        return DataPointsResourceWithRawResponse(self._data_inputs.data_points)


class AsyncDataInputsResourceWithRawResponse:
    def __init__(self, data_inputs: AsyncDataInputsResource) -> None:
        self._data_inputs = data_inputs

        self.list = async_to_raw_response_wrapper(
            data_inputs.list,
        )

    @cached_property
    def data_points(self) -> AsyncDataPointsResourceWithRawResponse:
        return AsyncDataPointsResourceWithRawResponse(self._data_inputs.data_points)


class DataInputsResourceWithStreamingResponse:
    def __init__(self, data_inputs: DataInputsResource) -> None:
        self._data_inputs = data_inputs

        self.list = to_streamed_response_wrapper(
            data_inputs.list,
        )

    @cached_property
    def data_points(self) -> DataPointsResourceWithStreamingResponse:
        return DataPointsResourceWithStreamingResponse(self._data_inputs.data_points)


class AsyncDataInputsResourceWithStreamingResponse:
    def __init__(self, data_inputs: AsyncDataInputsResource) -> None:
        self._data_inputs = data_inputs

        self.list = async_to_streamed_response_wrapper(
            data_inputs.list,
        )

    @cached_property
    def data_points(self) -> AsyncDataPointsResourceWithStreamingResponse:
        return AsyncDataPointsResourceWithStreamingResponse(self._data_inputs.data_points)
