# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.hos import clock_list_params
from ..._base_client import make_request_options
from ...types.hos.clock_list_response import ClockListResponse

__all__ = ["ClocksResource", "AsyncClocksResource"]


class ClocksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return ClocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return ClocksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClockListResponse:
        """Get the current HOS status for all drivers.

        Note that this includes inactive as
        well as active drivers. The legacy version of this endpoint can be found at
        [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getFleetHosLogsSummary).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read ELD Compliance Settings (US)** under the
        Compliance category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          driver_ids:
              A filter on the data based on this comma-separated list of driver IDs. Example:
              `driverIds=1234,5678`

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
            "/fleet/hos/clocks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "driver_ids": driver_ids,
                        "limit": limit,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    clock_list_params.ClockListParams,
                ),
            ),
            cast_to=ClockListResponse,
        )


class AsyncClocksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncClocksResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClockListResponse:
        """Get the current HOS status for all drivers.

        Note that this includes inactive as
        well as active drivers. The legacy version of this endpoint can be found at
        [samsara.com/api-legacy](https://www.samsara.com/api-legacy#operation/getFleetHosLogsSummary).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read ELD Compliance Settings (US)** under the
        Compliance category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          driver_ids:
              A filter on the data based on this comma-separated list of driver IDs. Example:
              `driverIds=1234,5678`

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
            "/fleet/hos/clocks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "driver_ids": driver_ids,
                        "limit": limit,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    clock_list_params.ClockListParams,
                ),
            ),
            cast_to=ClockListResponse,
        )


class ClocksResourceWithRawResponse:
    def __init__(self, clocks: ClocksResource) -> None:
        self._clocks = clocks

        self.list = to_raw_response_wrapper(
            clocks.list,
        )


class AsyncClocksResourceWithRawResponse:
    def __init__(self, clocks: AsyncClocksResource) -> None:
        self._clocks = clocks

        self.list = async_to_raw_response_wrapper(
            clocks.list,
        )


class ClocksResourceWithStreamingResponse:
    def __init__(self, clocks: ClocksResource) -> None:
        self._clocks = clocks

        self.list = to_streamed_response_wrapper(
            clocks.list,
        )


class AsyncClocksResourceWithStreamingResponse:
    def __init__(self, clocks: AsyncClocksResource) -> None:
        self._clocks = clocks

        self.list = async_to_streamed_response_wrapper(
            clocks.list,
        )
