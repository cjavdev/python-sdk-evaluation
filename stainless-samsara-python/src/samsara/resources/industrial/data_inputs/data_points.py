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
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.industrial.data_inputs import (
    data_point_feed_params,
    data_point_history_params,
    data_point_retrieve_params,
)
from ....types.industrial.data_inputs.data_input_list_response import DataInputListResponse
from ....types.industrial.data_inputs.data_input_snapshot_response import DataInputSnapshotResponse

__all__ = ["DataPointsResource", "AsyncDataPointsResource"]


class DataPointsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataPointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DataPointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataPointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DataPointsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        asset_ids: List[str] | NotGiven = NOT_GIVEN,
        data_input_ids: List[str] | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataInputSnapshotResponse:
        """Returns last known data points for all data inputs.

        This can be filtered by
        optional tags, specific data input IDs or asset IDs.

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

          data_input_ids: A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678`

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
            "/industrial/data-inputs/data-points",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "asset_ids": asset_ids,
                        "data_input_ids": data_input_ids,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    data_point_retrieve_params.DataPointRetrieveParams,
                ),
            ),
            cast_to=DataInputSnapshotResponse,
        )

    def feed(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        asset_ids: List[str] | NotGiven = NOT_GIVEN,
        data_input_ids: List[str] | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataInputListResponse:
        """
        Follow a continuous feed of all data input data points.

        Your first call to this endpoint will provide you with the most recent data
        points for each data input and a `pagination` object that contains an
        `endCursor`.

        You can provide the `endCursor` to the `after` parameter of this endpoint to get
        data point updates since that `endCursor`.

        If `hasNextPage` is `false`, no updates are readily available yet. We suggest
        waiting a minimum of 5 seconds before requesting updates.

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

          data_input_ids: A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678`

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
            "/industrial/data-inputs/data-points/feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "asset_ids": asset_ids,
                        "data_input_ids": data_input_ids,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    data_point_feed_params.DataPointFeedParams,
                ),
            ),
            cast_to=DataInputListResponse,
        )

    def history(
        self,
        *,
        end_time: str,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        asset_ids: List[str] | NotGiven = NOT_GIVEN,
        data_input_ids: List[str] | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataInputListResponse:
        """
        Returns all known data points during the given time range for all data inputs.
        This can be filtered by optional tags, specific data input IDs or asset IDs.

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
          end_time: An end time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          start_time: A start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          asset_ids:
              A comma-separated list of industrial asset UUIDs. Example:
              `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`

          data_input_ids: A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678`

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
            "/industrial/data-inputs/data-points/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "start_time": start_time,
                        "after": after,
                        "asset_ids": asset_ids,
                        "data_input_ids": data_input_ids,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    data_point_history_params.DataPointHistoryParams,
                ),
            ),
            cast_to=DataInputListResponse,
        )


class AsyncDataPointsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataPointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataPointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataPointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDataPointsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        asset_ids: List[str] | NotGiven = NOT_GIVEN,
        data_input_ids: List[str] | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataInputSnapshotResponse:
        """Returns last known data points for all data inputs.

        This can be filtered by
        optional tags, specific data input IDs or asset IDs.

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

          data_input_ids: A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678`

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
            "/industrial/data-inputs/data-points",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "asset_ids": asset_ids,
                        "data_input_ids": data_input_ids,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    data_point_retrieve_params.DataPointRetrieveParams,
                ),
            ),
            cast_to=DataInputSnapshotResponse,
        )

    async def feed(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        asset_ids: List[str] | NotGiven = NOT_GIVEN,
        data_input_ids: List[str] | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataInputListResponse:
        """
        Follow a continuous feed of all data input data points.

        Your first call to this endpoint will provide you with the most recent data
        points for each data input and a `pagination` object that contains an
        `endCursor`.

        You can provide the `endCursor` to the `after` parameter of this endpoint to get
        data point updates since that `endCursor`.

        If `hasNextPage` is `false`, no updates are readily available yet. We suggest
        waiting a minimum of 5 seconds before requesting updates.

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

          data_input_ids: A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678`

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
            "/industrial/data-inputs/data-points/feed",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "asset_ids": asset_ids,
                        "data_input_ids": data_input_ids,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    data_point_feed_params.DataPointFeedParams,
                ),
            ),
            cast_to=DataInputListResponse,
        )

    async def history(
        self,
        *,
        end_time: str,
        start_time: str,
        after: str | NotGiven = NOT_GIVEN,
        asset_ids: List[str] | NotGiven = NOT_GIVEN,
        data_input_ids: List[str] | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DataInputListResponse:
        """
        Returns all known data points during the given time range for all data inputs.
        This can be filtered by optional tags, specific data input IDs or asset IDs.

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
          end_time: An end time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          start_time: A start time in RFC 3339 format. Millisecond precision and timezones are
              supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
              2015-09-15T14:00:12-04:00).

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          asset_ids:
              A comma-separated list of industrial asset UUIDs. Example:
              `assetIds=076efac2-83b5-47aa-ba36-18428436dcac,6707b3f0-23b9-4fe3-b7be-11be34aea544`

          data_input_ids: A comma-separated list of data input IDs. Example: `dataInputIds=1234,5678`

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
            "/industrial/data-inputs/data-points/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_time": end_time,
                        "start_time": start_time,
                        "after": after,
                        "asset_ids": asset_ids,
                        "data_input_ids": data_input_ids,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    data_point_history_params.DataPointHistoryParams,
                ),
            ),
            cast_to=DataInputListResponse,
        )


class DataPointsResourceWithRawResponse:
    def __init__(self, data_points: DataPointsResource) -> None:
        self._data_points = data_points

        self.retrieve = to_raw_response_wrapper(
            data_points.retrieve,
        )
        self.feed = to_raw_response_wrapper(
            data_points.feed,
        )
        self.history = to_raw_response_wrapper(
            data_points.history,
        )


class AsyncDataPointsResourceWithRawResponse:
    def __init__(self, data_points: AsyncDataPointsResource) -> None:
        self._data_points = data_points

        self.retrieve = async_to_raw_response_wrapper(
            data_points.retrieve,
        )
        self.feed = async_to_raw_response_wrapper(
            data_points.feed,
        )
        self.history = async_to_raw_response_wrapper(
            data_points.history,
        )


class DataPointsResourceWithStreamingResponse:
    def __init__(self, data_points: DataPointsResource) -> None:
        self._data_points = data_points

        self.retrieve = to_streamed_response_wrapper(
            data_points.retrieve,
        )
        self.feed = to_streamed_response_wrapper(
            data_points.feed,
        )
        self.history = to_streamed_response_wrapper(
            data_points.history,
        )


class AsyncDataPointsResourceWithStreamingResponse:
    def __init__(self, data_points: AsyncDataPointsResource) -> None:
        self._data_points = data_points

        self.retrieve = async_to_streamed_response_wrapper(
            data_points.retrieve,
        )
        self.feed = async_to_streamed_response_wrapper(
            data_points.feed,
        )
        self.history = async_to_streamed_response_wrapper(
            data_points.history,
        )
