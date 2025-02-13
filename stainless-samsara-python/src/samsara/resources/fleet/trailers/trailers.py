# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable

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
from ....types.fleet import trailer_list_params, trailer_create_params
from ...._base_client import make_request_options
from ....types.fleet.trailers_list_trailers_response_body import TrailersListTrailersResponseBody
from ....types.fleet.trailers_create_trailer_response_body import TrailersCreateTrailerResponseBody

__all__ = ["TrailersResource", "AsyncTrailersResource"]


class TrailersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrailersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return TrailersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrailersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return TrailersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        attributes: Iterable[trailer_create_params.Attribute] | NotGiven = NOT_GIVEN,
        enabled_for_mobile: bool | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        license_plate: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        trailer_serial_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrailersCreateTrailerResponseBody:
        """
        Creates a new trailer asset.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Trailers** under the Trailers category when
        creating or editing an API token.
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
          name: The human-readable name of the Trailer. This is set by a fleet administrator and
              will appear in both Samsara’s cloud dashboard as well as the Samsara Driver
              mobile app. By default, this name is the serial number of the Samsara Asset
              Gateway. It can be set or updated through the Samsara Dashboard or through the
              API at any time.

          attributes: A list of attributes to assign to the trailer.

          enabled_for_mobile: Indicates if the trailer is visible on the Samsara mobile apps.

          external_ids: A map of external ids

          license_plate: The license plate of the Trailer. **By default**: empty. Can be set or updated
              through the Samsara Dashboard or the API at any time.

          notes: These are generic notes about the Trailer. Empty by default. Can be set or
              updated through the Samsara Dashboard or the API at any time.

          tag_ids: An array of IDs of tags to associate with this trailer. If your access to the
              API is scoped by one or more tags, this field is required to pass in.

          trailer_serial_number: The serial number of the trailer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fleet/trailers",
            body=maybe_transform(
                {
                    "name": name,
                    "attributes": attributes,
                    "enabled_for_mobile": enabled_for_mobile,
                    "external_ids": external_ids,
                    "license_plate": license_plate,
                    "notes": notes,
                    "tag_ids": tag_ids,
                    "trailer_serial_number": trailer_serial_number,
                },
                trailer_create_params.TrailerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrailersCreateTrailerResponseBody,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrailersListTrailersResponseBody:
        """
        List all trailers.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Trailers** under the Trailers category when
        creating or editing an API token.
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
            "/fleet/trailers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    trailer_list_params.TrailerListParams,
                ),
            ),
            cast_to=TrailersListTrailersResponseBody,
        )


class AsyncTrailersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrailersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrailersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrailersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncTrailersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        attributes: Iterable[trailer_create_params.Attribute] | NotGiven = NOT_GIVEN,
        enabled_for_mobile: bool | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        license_plate: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        trailer_serial_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrailersCreateTrailerResponseBody:
        """
        Creates a new trailer asset.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Trailers** under the Trailers category when
        creating or editing an API token.
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
          name: The human-readable name of the Trailer. This is set by a fleet administrator and
              will appear in both Samsara’s cloud dashboard as well as the Samsara Driver
              mobile app. By default, this name is the serial number of the Samsara Asset
              Gateway. It can be set or updated through the Samsara Dashboard or through the
              API at any time.

          attributes: A list of attributes to assign to the trailer.

          enabled_for_mobile: Indicates if the trailer is visible on the Samsara mobile apps.

          external_ids: A map of external ids

          license_plate: The license plate of the Trailer. **By default**: empty. Can be set or updated
              through the Samsara Dashboard or the API at any time.

          notes: These are generic notes about the Trailer. Empty by default. Can be set or
              updated through the Samsara Dashboard or the API at any time.

          tag_ids: An array of IDs of tags to associate with this trailer. If your access to the
              API is scoped by one or more tags, this field is required to pass in.

          trailer_serial_number: The serial number of the trailer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fleet/trailers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "attributes": attributes,
                    "enabled_for_mobile": enabled_for_mobile,
                    "external_ids": external_ids,
                    "license_plate": license_plate,
                    "notes": notes,
                    "tag_ids": tag_ids,
                    "trailer_serial_number": trailer_serial_number,
                },
                trailer_create_params.TrailerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrailersCreateTrailerResponseBody,
        )

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrailersListTrailersResponseBody:
        """
        List all trailers.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Trailers** under the Trailers category when
        creating or editing an API token.
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
            "/fleet/trailers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                        "parent_tag_ids": parent_tag_ids,
                        "tag_ids": tag_ids,
                    },
                    trailer_list_params.TrailerListParams,
                ),
            ),
            cast_to=TrailersListTrailersResponseBody,
        )


class TrailersResourceWithRawResponse:
    def __init__(self, trailers: TrailersResource) -> None:
        self._trailers = trailers

        self.create = to_raw_response_wrapper(
            trailers.create,
        )
        self.list = to_raw_response_wrapper(
            trailers.list,
        )


class AsyncTrailersResourceWithRawResponse:
    def __init__(self, trailers: AsyncTrailersResource) -> None:
        self._trailers = trailers

        self.create = async_to_raw_response_wrapper(
            trailers.create,
        )
        self.list = async_to_raw_response_wrapper(
            trailers.list,
        )


class TrailersResourceWithStreamingResponse:
    def __init__(self, trailers: TrailersResource) -> None:
        self._trailers = trailers

        self.create = to_streamed_response_wrapper(
            trailers.create,
        )
        self.list = to_streamed_response_wrapper(
            trailers.list,
        )


class AsyncTrailersResourceWithStreamingResponse:
    def __init__(self, trailers: AsyncTrailersResource) -> None:
        self._trailers = trailers

        self.create = async_to_streamed_response_wrapper(
            trailers.create,
        )
        self.list = async_to_streamed_response_wrapper(
            trailers.list,
        )
