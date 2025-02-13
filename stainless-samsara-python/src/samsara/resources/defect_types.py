# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import defect_type_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.defect_type_list_response import DefectTypeListResponse

__all__ = ["DefectTypesResource", "AsyncDefectTypesResource"]


class DefectTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DefectTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DefectTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DefectTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DefectTypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DefectTypeListResponse:
        """
        Get DVIR defect types.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Defect Types** under the Maintenance
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        Args:
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          ids: A filter on the data based on this comma-separated list of defect type IDs.

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 512 objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/defect-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "ids": ids,
                        "limit": limit,
                    },
                    defect_type_list_params.DefectTypeListParams,
                ),
            ),
            cast_to=DefectTypeListResponse,
        )


class AsyncDefectTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDefectTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDefectTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDefectTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDefectTypesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DefectTypeListResponse:
        """
        Get DVIR defect types.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Defect Types** under the Maintenance
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        Args:
          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          ids: A filter on the data based on this comma-separated list of defect type IDs.

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 512 objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/defect-types",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "ids": ids,
                        "limit": limit,
                    },
                    defect_type_list_params.DefectTypeListParams,
                ),
            ),
            cast_to=DefectTypeListResponse,
        )


class DefectTypesResourceWithRawResponse:
    def __init__(self, defect_types: DefectTypesResource) -> None:
        self._defect_types = defect_types

        self.list = to_raw_response_wrapper(
            defect_types.list,
        )


class AsyncDefectTypesResourceWithRawResponse:
    def __init__(self, defect_types: AsyncDefectTypesResource) -> None:
        self._defect_types = defect_types

        self.list = async_to_raw_response_wrapper(
            defect_types.list,
        )


class DefectTypesResourceWithStreamingResponse:
    def __init__(self, defect_types: DefectTypesResource) -> None:
        self._defect_types = defect_types

        self.list = to_streamed_response_wrapper(
            defect_types.list,
        )


class AsyncDefectTypesResourceWithStreamingResponse:
    def __init__(self, defect_types: AsyncDefectTypesResource) -> None:
        self._defect_types = defect_types

        self.list = async_to_streamed_response_wrapper(
            defect_types.list,
        )
