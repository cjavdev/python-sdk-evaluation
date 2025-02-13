# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import hos_authentication_log_list_params
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
from ..types.v1_hos_authentication_logs_response import V1HosAuthenticationLogsResponse

__all__ = ["HosAuthenticationLogsResource", "AsyncHosAuthenticationLogsResource"]


class HosAuthenticationLogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HosAuthenticationLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return HosAuthenticationLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HosAuthenticationLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return HosAuthenticationLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        driver_id: int,
        end_ms: int,
        start_ms: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1HosAuthenticationLogsResponse:
        """
        <n class="warning">
        <nh>
        <i class="fa fa-exclamation-circle"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Get the HOS (hours of service) signin and signout logs for the specified driver.
        The response includes 4 fields that are now deprecated.

        **Note:** If data is still being uploaded from the Samsara Driver App, it may
        not be completely reflected in the response from this endpoint. The best
        practice is to wait a couple of days before querying this endpoint to make sure
        that all data from the Samsara Driver App has been uploaded.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read ELD Hours of Service (US)** under the
        Compliance category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          driver_id: Driver ID to query.

          end_ms: End of the time range, specified in milliseconds UNIX time.

          start_ms: Beginning of the time range, specified in milliseconds UNIX time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/fleet/hos_authentication_logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "driver_id": driver_id,
                        "end_ms": end_ms,
                        "start_ms": start_ms,
                    },
                    hos_authentication_log_list_params.HosAuthenticationLogListParams,
                ),
            ),
            cast_to=V1HosAuthenticationLogsResponse,
        )


class AsyncHosAuthenticationLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHosAuthenticationLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHosAuthenticationLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHosAuthenticationLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncHosAuthenticationLogsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        driver_id: int,
        end_ms: int,
        start_ms: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1HosAuthenticationLogsResponse:
        """
        <n class="warning">
        <nh>
        <i class="fa fa-exclamation-circle"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Get the HOS (hours of service) signin and signout logs for the specified driver.
        The response includes 4 fields that are now deprecated.

        **Note:** If data is still being uploaded from the Samsara Driver App, it may
        not be completely reflected in the response from this endpoint. The best
        practice is to wait a couple of days before querying this endpoint to make sure
        that all data from the Samsara Driver App has been uploaded.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read ELD Hours of Service (US)** under the
        Compliance category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          driver_id: Driver ID to query.

          end_ms: End of the time range, specified in milliseconds UNIX time.

          start_ms: Beginning of the time range, specified in milliseconds UNIX time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/fleet/hos_authentication_logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "driver_id": driver_id,
                        "end_ms": end_ms,
                        "start_ms": start_ms,
                    },
                    hos_authentication_log_list_params.HosAuthenticationLogListParams,
                ),
            ),
            cast_to=V1HosAuthenticationLogsResponse,
        )


class HosAuthenticationLogsResourceWithRawResponse:
    def __init__(self, hos_authentication_logs: HosAuthenticationLogsResource) -> None:
        self._hos_authentication_logs = hos_authentication_logs

        self.list = to_raw_response_wrapper(
            hos_authentication_logs.list,
        )


class AsyncHosAuthenticationLogsResourceWithRawResponse:
    def __init__(self, hos_authentication_logs: AsyncHosAuthenticationLogsResource) -> None:
        self._hos_authentication_logs = hos_authentication_logs

        self.list = async_to_raw_response_wrapper(
            hos_authentication_logs.list,
        )


class HosAuthenticationLogsResourceWithStreamingResponse:
    def __init__(self, hos_authentication_logs: HosAuthenticationLogsResource) -> None:
        self._hos_authentication_logs = hos_authentication_logs

        self.list = to_streamed_response_wrapper(
            hos_authentication_logs.list,
        )


class AsyncHosAuthenticationLogsResourceWithStreamingResponse:
    def __init__(self, hos_authentication_logs: AsyncHosAuthenticationLogsResource) -> None:
        self._hos_authentication_logs = hos_authentication_logs

        self.list = async_to_streamed_response_wrapper(
            hos_authentication_logs.list,
        )
