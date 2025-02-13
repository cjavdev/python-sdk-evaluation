# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable

import httpx

from ...types import trailer_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from .assignments import (
    AssignmentsResource,
    AsyncAssignmentsResource,
    AssignmentsResourceWithRawResponse,
    AsyncAssignmentsResourceWithRawResponse,
    AssignmentsResourceWithStreamingResponse,
    AsyncAssignmentsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.fleet.trailers_get_trailer_response_body import TrailersGetTrailerResponseBody
from ...types.fleet.trailers_update_trailer_response_body import TrailersUpdateTrailerResponseBody

__all__ = ["TrailersResource", "AsyncTrailersResource"]


class TrailersResource(SyncAPIResource):
    @cached_property
    def assignments(self) -> AssignmentsResource:
        return AssignmentsResource(self._client)

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

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrailersGetTrailerResponseBody:
        """
        Retrieve a trailer with given ID.

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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/fleet/trailers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrailersGetTrailerResponseBody,
        )

    def update(
        self,
        id: str,
        *,
        attributes: Iterable[trailer_update_params.Attribute] | NotGiven = NOT_GIVEN,
        enabled_for_mobile: bool | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        license_plate: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        odometer_meters: int | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        trailer_serial_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrailersUpdateTrailerResponseBody:
        """Update a trailer.

        **Note** this implementation of patch uses
        [the JSON merge patch](https://tools.ietf.org/html/rfc7396) proposed standard.
        This means that any fields included in the patch request will _overwrite_ fields
        which exist on the target resource. For arrays, this means any array included in
        the request will _replace_ the array that exists at the specified path, it will
        not _add_ to the existing array

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
          attributes: A list of attributes to assign to the trailer.

          enabled_for_mobile: Indicates if the trailer is visible on the Samsara mobile apps.

          external_ids: A map of external ids

          license_plate: The license plate of the Trailer. **By default**: empty. Can be set or updated
              through the Samsara Dashboard or the API at any time.

          name: The human-readable name of the Trailer. This is set by a fleet administrator and
              will appear in both Samsara’s cloud dashboard as well as the Samsara Driver
              mobile app. By default, this name is the serial number of the Samsara Asset
              Gateway. It can be set or updated through the Samsara Dashboard or through the
              API at any time.

          notes: These are generic notes about the Trailer. Empty by default. Can be set or
              updated through the Samsara Dashboard or the API at any time.

          odometer_meters: When you provide a manual odometer override, Samsara will begin updating a
              trailer's odometer using GPS distance traveled since this override was set. Only
              applies to trailers installed with Samsara gateways.

          tag_ids: An array of IDs of tags to associate with this trailer. If your access to the
              API is scoped by one or more tags, this field is required to pass in.

          trailer_serial_number: The serial number of the trailer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/fleet/trailers/{id}",
            body=maybe_transform(
                {
                    "attributes": attributes,
                    "enabled_for_mobile": enabled_for_mobile,
                    "external_ids": external_ids,
                    "license_plate": license_plate,
                    "name": name,
                    "notes": notes,
                    "odometer_meters": odometer_meters,
                    "tag_ids": tag_ids,
                    "trailer_serial_number": trailer_serial_number,
                },
                trailer_update_params.TrailerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrailersUpdateTrailerResponseBody,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a trailer with the given ID.

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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/fleet/trailers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTrailersResource(AsyncAPIResource):
    @cached_property
    def assignments(self) -> AsyncAssignmentsResource:
        return AsyncAssignmentsResource(self._client)

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

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrailersGetTrailerResponseBody:
        """
        Retrieve a trailer with given ID.

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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/fleet/trailers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrailersGetTrailerResponseBody,
        )

    async def update(
        self,
        id: str,
        *,
        attributes: Iterable[trailer_update_params.Attribute] | NotGiven = NOT_GIVEN,
        enabled_for_mobile: bool | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        license_plate: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        odometer_meters: int | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        trailer_serial_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrailersUpdateTrailerResponseBody:
        """Update a trailer.

        **Note** this implementation of patch uses
        [the JSON merge patch](https://tools.ietf.org/html/rfc7396) proposed standard.
        This means that any fields included in the patch request will _overwrite_ fields
        which exist on the target resource. For arrays, this means any array included in
        the request will _replace_ the array that exists at the specified path, it will
        not _add_ to the existing array

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
          attributes: A list of attributes to assign to the trailer.

          enabled_for_mobile: Indicates if the trailer is visible on the Samsara mobile apps.

          external_ids: A map of external ids

          license_plate: The license plate of the Trailer. **By default**: empty. Can be set or updated
              through the Samsara Dashboard or the API at any time.

          name: The human-readable name of the Trailer. This is set by a fleet administrator and
              will appear in both Samsara’s cloud dashboard as well as the Samsara Driver
              mobile app. By default, this name is the serial number of the Samsara Asset
              Gateway. It can be set or updated through the Samsara Dashboard or through the
              API at any time.

          notes: These are generic notes about the Trailer. Empty by default. Can be set or
              updated through the Samsara Dashboard or the API at any time.

          odometer_meters: When you provide a manual odometer override, Samsara will begin updating a
              trailer's odometer using GPS distance traveled since this override was set. Only
              applies to trailers installed with Samsara gateways.

          tag_ids: An array of IDs of tags to associate with this trailer. If your access to the
              API is scoped by one or more tags, this field is required to pass in.

          trailer_serial_number: The serial number of the trailer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/fleet/trailers/{id}",
            body=await async_maybe_transform(
                {
                    "attributes": attributes,
                    "enabled_for_mobile": enabled_for_mobile,
                    "external_ids": external_ids,
                    "license_plate": license_plate,
                    "name": name,
                    "notes": notes,
                    "odometer_meters": odometer_meters,
                    "tag_ids": tag_ids,
                    "trailer_serial_number": trailer_serial_number,
                },
                trailer_update_params.TrailerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrailersUpdateTrailerResponseBody,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a trailer with the given ID.

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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/fleet/trailers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TrailersResourceWithRawResponse:
    def __init__(self, trailers: TrailersResource) -> None:
        self._trailers = trailers

        self.retrieve = to_raw_response_wrapper(
            trailers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            trailers.update,
        )
        self.delete = to_raw_response_wrapper(
            trailers.delete,
        )

    @cached_property
    def assignments(self) -> AssignmentsResourceWithRawResponse:
        return AssignmentsResourceWithRawResponse(self._trailers.assignments)


class AsyncTrailersResourceWithRawResponse:
    def __init__(self, trailers: AsyncTrailersResource) -> None:
        self._trailers = trailers

        self.retrieve = async_to_raw_response_wrapper(
            trailers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            trailers.update,
        )
        self.delete = async_to_raw_response_wrapper(
            trailers.delete,
        )

    @cached_property
    def assignments(self) -> AsyncAssignmentsResourceWithRawResponse:
        return AsyncAssignmentsResourceWithRawResponse(self._trailers.assignments)


class TrailersResourceWithStreamingResponse:
    def __init__(self, trailers: TrailersResource) -> None:
        self._trailers = trailers

        self.retrieve = to_streamed_response_wrapper(
            trailers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            trailers.update,
        )
        self.delete = to_streamed_response_wrapper(
            trailers.delete,
        )

    @cached_property
    def assignments(self) -> AssignmentsResourceWithStreamingResponse:
        return AssignmentsResourceWithStreamingResponse(self._trailers.assignments)


class AsyncTrailersResourceWithStreamingResponse:
    def __init__(self, trailers: AsyncTrailersResource) -> None:
        self._trailers = trailers

        self.retrieve = async_to_streamed_response_wrapper(
            trailers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            trailers.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            trailers.delete,
        )

    @cached_property
    def assignments(self) -> AsyncAssignmentsResourceWithStreamingResponse:
        return AsyncAssignmentsResourceWithStreamingResponse(self._trailers.assignments)
