# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.preview.custom_reports.runs import data_retrieve_params
from .....types.preview.custom_reports.runs.custom_reports_get_custom_report_run_data_response_body import (
    CustomReportsGetCustomReportRunDataResponseBody,
)

__all__ = ["DataResource", "AsyncDataResource"]


class DataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DataResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomReportsGetCustomReportRunDataResponseBody:
        """
        This endpoint will return the custom report data for a given custom report run
        ID. For more information regarding custom report columns, please see our
        [KB article section on Custom Report Fields](https://kb.samsara.com/hc/en-us/articles/360052711232-Manage-Custom-Reports).

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Custom Reports** under the Closed Beta
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Endpoints in this section are in Preview. These APIs are not functional and are
        instead for soliciting feedback from our API users on the intended design of
        this API. Additionally, it is not guaranteed that we will be releasing an
        endpoint included in this section to production. This means that developers
        should **NOT** rely on these APIs to build business critical applications

        - Samsara may change the structure of a preview API's interface without
          versioning or any notice to API users.

        - When an endpoint becomes generally available, it will be announced in the API
          [changelog](https://developers.samsara.com/changelog).

          **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
          as feedback in our
          <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
          form</a>. If you encountered an issue or noticed inaccuracies in the API
          documentation, please
          <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to
          our support team.

        Args:
          id: The ID of the specified run for the requested custom report.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/preview/custom-reports/runs/data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after": after,
                    },
                    data_retrieve_params.DataRetrieveParams,
                ),
            ),
            cast_to=CustomReportsGetCustomReportRunDataResponseBody,
        )


class AsyncDataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDataResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomReportsGetCustomReportRunDataResponseBody:
        """
        This endpoint will return the custom report data for a given custom report run
        ID. For more information regarding custom report columns, please see our
        [KB article section on Custom Report Fields](https://kb.samsara.com/hc/en-us/articles/360052711232-Manage-Custom-Reports).

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Custom Reports** under the Closed Beta
        category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Endpoints in this section are in Preview. These APIs are not functional and are
        instead for soliciting feedback from our API users on the intended design of
        this API. Additionally, it is not guaranteed that we will be releasing an
        endpoint included in this section to production. This means that developers
        should **NOT** rely on these APIs to build business critical applications

        - Samsara may change the structure of a preview API's interface without
          versioning or any notice to API users.

        - When an endpoint becomes generally available, it will be announced in the API
          [changelog](https://developers.samsara.com/changelog).

          **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
          as feedback in our
          <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
          form</a>. If you encountered an issue or noticed inaccuracies in the API
          documentation, please
          <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to
          our support team.

        Args:
          id: The ID of the specified run for the requested custom report.

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/preview/custom-reports/runs/data",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "id": id,
                        "after": after,
                    },
                    data_retrieve_params.DataRetrieveParams,
                ),
            ),
            cast_to=CustomReportsGetCustomReportRunDataResponseBody,
        )


class DataResourceWithRawResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

        self.retrieve = to_raw_response_wrapper(
            data.retrieve,
        )


class AsyncDataResourceWithRawResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

        self.retrieve = async_to_raw_response_wrapper(
            data.retrieve,
        )


class DataResourceWithStreamingResponse:
    def __init__(self, data: DataResource) -> None:
        self._data = data

        self.retrieve = to_streamed_response_wrapper(
            data.retrieve,
        )


class AsyncDataResourceWithStreamingResponse:
    def __init__(self, data: AsyncDataResource) -> None:
        self._data = data

        self.retrieve = async_to_streamed_response_wrapper(
            data.retrieve,
        )
