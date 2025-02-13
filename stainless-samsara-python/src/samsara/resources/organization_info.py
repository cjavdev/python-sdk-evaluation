# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.organization_info_response import OrganizationInfoResponse

__all__ = ["OrganizationInfoResource", "AsyncOrganizationInfoResource"]


class OrganizationInfoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrganizationInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return OrganizationInfoResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationInfoResponse:
        """
        Get information about your organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Org Information** under the Setup &
        Administration category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>
        """
        return self._get(
            "/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationInfoResponse,
        )


class AsyncOrganizationInfoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrganizationInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncOrganizationInfoResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationInfoResponse:
        """
        Get information about your organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Org Information** under the Setup &
        Administration category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>
        """
        return await self._get(
            "/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationInfoResponse,
        )


class OrganizationInfoResourceWithRawResponse:
    def __init__(self, organization_info: OrganizationInfoResource) -> None:
        self._organization_info = organization_info

        self.retrieve = to_raw_response_wrapper(
            organization_info.retrieve,
        )


class AsyncOrganizationInfoResourceWithRawResponse:
    def __init__(self, organization_info: AsyncOrganizationInfoResource) -> None:
        self._organization_info = organization_info

        self.retrieve = async_to_raw_response_wrapper(
            organization_info.retrieve,
        )


class OrganizationInfoResourceWithStreamingResponse:
    def __init__(self, organization_info: OrganizationInfoResource) -> None:
        self._organization_info = organization_info

        self.retrieve = to_streamed_response_wrapper(
            organization_info.retrieve,
        )


class AsyncOrganizationInfoResourceWithStreamingResponse:
    def __init__(self, organization_info: AsyncOrganizationInfoResource) -> None:
        self._organization_info = organization_info

        self.retrieve = async_to_streamed_response_wrapper(
            organization_info.retrieve,
        )
