# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import (
    live_share_list_params,
    live_share_create_params,
    live_share_delete_params,
    live_share_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.live_share_list_response import LiveShareListResponse
from ..types.live_share_create_response import LiveShareCreateResponse
from ..types.live_share_update_response import LiveShareUpdateResponse

__all__ = ["LiveSharesResource", "AsyncLiveSharesResource"]


class LiveSharesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LiveSharesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return LiveSharesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LiveSharesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return LiveSharesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        type: Literal["assetsLocation", "assetsNearLocation", "assetsOnRoute"],
        assets_location_link_config: live_share_create_params.AssetsLocationLinkConfig | NotGiven = NOT_GIVEN,
        assets_near_location_link_config: live_share_create_params.AssetsNearLocationLinkConfig | NotGiven = NOT_GIVEN,
        assets_on_route_link_config: live_share_create_params.AssetsOnRouteLinkConfig | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        expires_at_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LiveShareCreateResponse:
        """
        Create Live Sharing Link.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Live Sharing Links** under the Driver
        Workflow category when creating or editing an API token.
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
          name: Name of the Live Sharing Link.

          type: Type of the Live Sharing Link. This field specifies which one of
              '<type>LinkConfig' objects will be used to configure the sharing link. Valid
              values: `assetsLocation`, `assetsNearLocation`, `assetsOnRoute`

          assets_location_link_config: Configuration details specific to the 'By Asset' Live Sharing Link.

          assets_near_location_link_config: Configuration details specific to the 'By Location' Live Sharing Link.

          assets_on_route_link_config: Configuration details specific to the 'By Recurring Route' Live Sharing Link.

          description: Description for the Live Sharing Link (not applicable for 'assetsOnRoute' type).

          expires_at_time: Date that this link expires in RFC 3339 format. Can't be set in the past. If not
              provided then link will never expire.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/live-shares",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "assets_location_link_config": assets_location_link_config,
                    "assets_near_location_link_config": assets_near_location_link_config,
                    "assets_on_route_link_config": assets_on_route_link_config,
                    "description": description,
                    "expires_at_time": expires_at_time,
                },
                live_share_create_params.LiveShareCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveShareCreateResponse,
        )

    def update(
        self,
        *,
        id: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        expires_at_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LiveShareUpdateResponse:
        """
        Update Live Sharing Link.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Live Sharing Links** under the Driver
        Workflow category when creating or editing an API token.
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
          id: Unique identifier for the Live Sharing Link.

          name: Name of the Live Sharing Link.

          description: Description for the Live Sharing Link (not applicable for 'assetsOnRoute' type).

          expires_at_time: Date that this link expires in RFC 3339 format. Can't be set in the past. If not
              provided then link will never expire.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/live-shares",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "expires_at_time": expires_at_time,
                },
                live_share_update_params.LiveShareUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, live_share_update_params.LiveShareUpdateParams),
            ),
            cast_to=LiveShareUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        type: Literal["all", "assetsLocation", "assetsNearLocation", "assetsOnRoute"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LiveShareListResponse:
        """
        Returns all non-expired Live Sharing Links.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Live Sharing Links** under the Driver
        Workflow category when creating or editing an API token.
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

          ids: A filter on the data based on this comma-separated list of Live Share Link IDs

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 100 objects.

          type: A filter on the data based on the Live Sharing Link type. Valid values: `all`,
              `assetsLocation`, `assetsNearLocation`, `assetsOnRoute`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/live-shares",
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
                        "type": type,
                    },
                    live_share_list_params.LiveShareListParams,
                ),
            ),
            cast_to=LiveShareListResponse,
        )

    def delete(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete Live Sharing Link.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Live Sharing Links** under the Driver
        Workflow category when creating or editing an API token.
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
          id: Unique identifier for the Live Sharing Link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/live-shares",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, live_share_delete_params.LiveShareDeleteParams),
            ),
            cast_to=NoneType,
        )


class AsyncLiveSharesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLiveSharesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLiveSharesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLiveSharesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncLiveSharesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        type: Literal["assetsLocation", "assetsNearLocation", "assetsOnRoute"],
        assets_location_link_config: live_share_create_params.AssetsLocationLinkConfig | NotGiven = NOT_GIVEN,
        assets_near_location_link_config: live_share_create_params.AssetsNearLocationLinkConfig | NotGiven = NOT_GIVEN,
        assets_on_route_link_config: live_share_create_params.AssetsOnRouteLinkConfig | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        expires_at_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LiveShareCreateResponse:
        """
        Create Live Sharing Link.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Live Sharing Links** under the Driver
        Workflow category when creating or editing an API token.
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
          name: Name of the Live Sharing Link.

          type: Type of the Live Sharing Link. This field specifies which one of
              '<type>LinkConfig' objects will be used to configure the sharing link. Valid
              values: `assetsLocation`, `assetsNearLocation`, `assetsOnRoute`

          assets_location_link_config: Configuration details specific to the 'By Asset' Live Sharing Link.

          assets_near_location_link_config: Configuration details specific to the 'By Location' Live Sharing Link.

          assets_on_route_link_config: Configuration details specific to the 'By Recurring Route' Live Sharing Link.

          description: Description for the Live Sharing Link (not applicable for 'assetsOnRoute' type).

          expires_at_time: Date that this link expires in RFC 3339 format. Can't be set in the past. If not
              provided then link will never expire.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/live-shares",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "assets_location_link_config": assets_location_link_config,
                    "assets_near_location_link_config": assets_near_location_link_config,
                    "assets_on_route_link_config": assets_on_route_link_config,
                    "description": description,
                    "expires_at_time": expires_at_time,
                },
                live_share_create_params.LiveShareCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LiveShareCreateResponse,
        )

    async def update(
        self,
        *,
        id: str,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        expires_at_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LiveShareUpdateResponse:
        """
        Update Live Sharing Link.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Live Sharing Links** under the Driver
        Workflow category when creating or editing an API token.
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
          id: Unique identifier for the Live Sharing Link.

          name: Name of the Live Sharing Link.

          description: Description for the Live Sharing Link (not applicable for 'assetsOnRoute' type).

          expires_at_time: Date that this link expires in RFC 3339 format. Can't be set in the past. If not
              provided then link will never expire.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/live-shares",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                    "expires_at_time": expires_at_time,
                },
                live_share_update_params.LiveShareUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, live_share_update_params.LiveShareUpdateParams),
            ),
            cast_to=LiveShareUpdateResponse,
        )

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        type: Literal["all", "assetsLocation", "assetsNearLocation", "assetsOnRoute"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LiveShareListResponse:
        """
        Returns all non-expired Live Sharing Links.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Live Sharing Links** under the Driver
        Workflow category when creating or editing an API token.
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

          ids: A filter on the data based on this comma-separated list of Live Share Link IDs

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 100 objects.

          type: A filter on the data based on the Live Sharing Link type. Valid values: `all`,
              `assetsLocation`, `assetsNearLocation`, `assetsOnRoute`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/live-shares",
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
                        "type": type,
                    },
                    live_share_list_params.LiveShareListParams,
                ),
            ),
            cast_to=LiveShareListResponse,
        )

    async def delete(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete Live Sharing Link.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Live Sharing Links** under the Driver
        Workflow category when creating or editing an API token.
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
          id: Unique identifier for the Live Sharing Link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/live-shares",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, live_share_delete_params.LiveShareDeleteParams),
            ),
            cast_to=NoneType,
        )


class LiveSharesResourceWithRawResponse:
    def __init__(self, live_shares: LiveSharesResource) -> None:
        self._live_shares = live_shares

        self.create = to_raw_response_wrapper(
            live_shares.create,
        )
        self.update = to_raw_response_wrapper(
            live_shares.update,
        )
        self.list = to_raw_response_wrapper(
            live_shares.list,
        )
        self.delete = to_raw_response_wrapper(
            live_shares.delete,
        )


class AsyncLiveSharesResourceWithRawResponse:
    def __init__(self, live_shares: AsyncLiveSharesResource) -> None:
        self._live_shares = live_shares

        self.create = async_to_raw_response_wrapper(
            live_shares.create,
        )
        self.update = async_to_raw_response_wrapper(
            live_shares.update,
        )
        self.list = async_to_raw_response_wrapper(
            live_shares.list,
        )
        self.delete = async_to_raw_response_wrapper(
            live_shares.delete,
        )


class LiveSharesResourceWithStreamingResponse:
    def __init__(self, live_shares: LiveSharesResource) -> None:
        self._live_shares = live_shares

        self.create = to_streamed_response_wrapper(
            live_shares.create,
        )
        self.update = to_streamed_response_wrapper(
            live_shares.update,
        )
        self.list = to_streamed_response_wrapper(
            live_shares.list,
        )
        self.delete = to_streamed_response_wrapper(
            live_shares.delete,
        )


class AsyncLiveSharesResourceWithStreamingResponse:
    def __init__(self, live_shares: AsyncLiveSharesResource) -> None:
        self._live_shares = live_shares

        self.create = async_to_streamed_response_wrapper(
            live_shares.create,
        )
        self.update = async_to_streamed_response_wrapper(
            live_shares.update,
        )
        self.list = async_to_streamed_response_wrapper(
            live_shares.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            live_shares.delete,
        )
