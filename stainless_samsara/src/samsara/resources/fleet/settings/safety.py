# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.fleet.settings.safety_settings_get_safety_settings_response_body import (
    SafetySettingsGetSafetySettingsResponseBody,
)

__all__ = ["SafetyResource", "AsyncSafetyResource"]


class SafetyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SafetyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return SafetyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SafetyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return SafetyResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SafetySettingsGetSafetySettingsResponseBody:
        """
        Get safety settings

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Safety Events & Scores** under the Safety &
        Cameras category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.
        """
        return self._get(
            "/fleet/settings/safety",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SafetySettingsGetSafetySettingsResponseBody,
        )


class AsyncSafetyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSafetyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSafetyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSafetyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncSafetyResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SafetySettingsGetSafetySettingsResponseBody:
        """
        Get safety settings

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Safety Events & Scores** under the Safety &
        Cameras category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.
        """
        return await self._get(
            "/fleet/settings/safety",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SafetySettingsGetSafetySettingsResponseBody,
        )


class SafetyResourceWithRawResponse:
    def __init__(self, safety: SafetyResource) -> None:
        self._safety = safety

        self.retrieve = to_raw_response_wrapper(
            safety.retrieve,
        )


class AsyncSafetyResourceWithRawResponse:
    def __init__(self, safety: AsyncSafetyResource) -> None:
        self._safety = safety

        self.retrieve = async_to_raw_response_wrapper(
            safety.retrieve,
        )


class SafetyResourceWithStreamingResponse:
    def __init__(self, safety: SafetyResource) -> None:
        self._safety = safety

        self.retrieve = to_streamed_response_wrapper(
            safety.retrieve,
        )


class AsyncSafetyResourceWithStreamingResponse:
    def __init__(self, safety: AsyncSafetyResource) -> None:
        self._safety = safety

        self.retrieve = async_to_streamed_response_wrapper(
            safety.retrieve,
        )
