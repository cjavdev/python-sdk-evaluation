# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ....types.fleet.assets import reefer_list_params
from ....types.fleet.assets.reefer_list_response import ReeferListResponse

__all__ = ["ReefersResource", "AsyncReefersResource"]


class ReefersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReefersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return ReefersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReefersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return ReefersResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end_ms: int,
        start_ms: int,
        ending_before: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReeferListResponse:
        """
        <n class="warning">
        <nh>
        <i class="fa fa-exclamation-circle"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Fetches all reefers and reefer-specific stats.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Trailers** under the Trailers category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          end_ms: Timestamp in milliseconds representing the end of the period to fetch,
              inclusive. Used in combination with startMs.

          start_ms: Timestamp in milliseconds representing the start of the period to fetch,
              inclusive. Used in combination with endMs.

          ending_before: Pagination parameter indicating the cursor position to return results before.
              Used in conjunction with the 'limit' parameter. Mutually exclusive with
              'startingAfter' parameter.

          limit: Pagination parameter indicating the number of results to return in this request.
              Used in conjunction with either 'startingAfter' or 'endingBefore'.

          starting_after: Pagination parameter indicating the cursor position to continue returning
              results after. Used in conjunction with the 'limit' parameter. Mutually
              exclusive with 'endingBefore' parameter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/fleet/assets/reefers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_ms": end_ms,
                        "start_ms": start_ms,
                        "ending_before": ending_before,
                        "limit": limit,
                        "starting_after": starting_after,
                    },
                    reefer_list_params.ReeferListParams,
                ),
            ),
            cast_to=ReeferListResponse,
        )


class AsyncReefersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReefersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReefersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReefersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncReefersResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        end_ms: int,
        start_ms: int,
        ending_before: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReeferListResponse:
        """
        <n class="warning">
        <nh>
        <i class="fa fa-exclamation-circle"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Fetches all reefers and reefer-specific stats.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Trailers** under the Trailers category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          end_ms: Timestamp in milliseconds representing the end of the period to fetch,
              inclusive. Used in combination with startMs.

          start_ms: Timestamp in milliseconds representing the start of the period to fetch,
              inclusive. Used in combination with endMs.

          ending_before: Pagination parameter indicating the cursor position to return results before.
              Used in conjunction with the 'limit' parameter. Mutually exclusive with
              'startingAfter' parameter.

          limit: Pagination parameter indicating the number of results to return in this request.
              Used in conjunction with either 'startingAfter' or 'endingBefore'.

          starting_after: Pagination parameter indicating the cursor position to continue returning
              results after. Used in conjunction with the 'limit' parameter. Mutually
              exclusive with 'endingBefore' parameter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/fleet/assets/reefers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_ms": end_ms,
                        "start_ms": start_ms,
                        "ending_before": ending_before,
                        "limit": limit,
                        "starting_after": starting_after,
                    },
                    reefer_list_params.ReeferListParams,
                ),
            ),
            cast_to=ReeferListResponse,
        )


class ReefersResourceWithRawResponse:
    def __init__(self, reefers: ReefersResource) -> None:
        self._reefers = reefers

        self.list = to_raw_response_wrapper(
            reefers.list,
        )


class AsyncReefersResourceWithRawResponse:
    def __init__(self, reefers: AsyncReefersResource) -> None:
        self._reefers = reefers

        self.list = async_to_raw_response_wrapper(
            reefers.list,
        )


class ReefersResourceWithStreamingResponse:
    def __init__(self, reefers: ReefersResource) -> None:
        self._reefers = reefers

        self.list = to_streamed_response_wrapper(
            reefers.list,
        )


class AsyncReefersResourceWithStreamingResponse:
    def __init__(self, reefers: AsyncReefersResource) -> None:
        self._reefers = reefers

        self.list = async_to_streamed_response_wrapper(
            reefers.list,
        )
