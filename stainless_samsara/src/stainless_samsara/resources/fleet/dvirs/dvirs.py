# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
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
from ....types.fleet import dvir_create_params, dvir_resolve_params
from ...._base_client import make_request_options
from ....types.fleet.dvir_create_response import DvirCreateResponse
from ....types.fleet.dvir_resolve_response import DvirResolveResponse

__all__ = ["DvirsResource", "AsyncDvirsResource"]


class DvirsResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> DvirsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return DvirsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DvirsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return DvirsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        author_id: str,
        safety_status: Literal["safe", "unsafe"],
        type: Literal["mechanic"],
        license_plate: str | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        mechanic_notes: str | NotGiven = NOT_GIVEN,
        odometer_meters: int | NotGiven = NOT_GIVEN,
        resolved_defect_ids: List[str] | NotGiven = NOT_GIVEN,
        trailer_id: str | NotGiven = NOT_GIVEN,
        vehicle_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DvirCreateResponse:
        """
        Creates a new mechanic DVIR in the organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write DVIRs** under the Maintenance category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          author_id: Samsara user ID of the mechanic creating the DVIR.

          safety_status: Whether or not this vehicle or trailer is safe to drive.

          type: Only type 'mechanic' is currently accepted.

          license_plate: The license plate of this vehicle.

          location: Optional string if your jurisdiction requires a location of the DVIR.

          mechanic_notes: The mechanics notes on the DVIR.

          odometer_meters: The odometer reading in meters.

          resolved_defect_ids: Array of ids for defects being resolved with this DVIR.

          trailer_id: Id of trailer being inspected. Either vehicleId or trailerId must be provided.

          vehicle_id: Id of vehicle being inspected. Either vehicleId or trailerId must be provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fleet/dvirs",
            body=maybe_transform(
                {
                    "author_id": author_id,
                    "safety_status": safety_status,
                    "type": type,
                    "license_plate": license_plate,
                    "location": location,
                    "mechanic_notes": mechanic_notes,
                    "odometer_meters": odometer_meters,
                    "resolved_defect_ids": resolved_defect_ids,
                    "trailer_id": trailer_id,
                    "vehicle_id": vehicle_id,
                },
                dvir_create_params.DvirCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DvirCreateResponse,
        )

    def resolve(
        self,
        id: str,
        *,
        author_id: str,
        is_resolved: bool,
        mechanic_notes: str | NotGiven = NOT_GIVEN,
        signed_at_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DvirResolveResponse:
        """
        Resolves a given DVIR by marking its `isResolved` field to `true`.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write DVIRs** under the Maintenance category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          author_id: The user who is resolving the dvir.

          is_resolved: Resolves the DVIR. Must be `true`.

          mechanic_notes: The mechanics notes on the DVIR.

          signed_at_time: Time when user signed this DVIR. Defaults to now. UTC timestamp in RFC 3339
              format. Example: `2020-01-27T07:06:25Z`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/fleet/dvirs/{id}",
            body=maybe_transform(
                {
                    "author_id": author_id,
                    "is_resolved": is_resolved,
                    "mechanic_notes": mechanic_notes,
                    "signed_at_time": signed_at_time,
                },
                dvir_resolve_params.DvirResolveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DvirResolveResponse,
        )


class AsyncDvirsResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDvirsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDvirsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDvirsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncDvirsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        author_id: str,
        safety_status: Literal["safe", "unsafe"],
        type: Literal["mechanic"],
        license_plate: str | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        mechanic_notes: str | NotGiven = NOT_GIVEN,
        odometer_meters: int | NotGiven = NOT_GIVEN,
        resolved_defect_ids: List[str] | NotGiven = NOT_GIVEN,
        trailer_id: str | NotGiven = NOT_GIVEN,
        vehicle_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DvirCreateResponse:
        """
        Creates a new mechanic DVIR in the organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write DVIRs** under the Maintenance category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          author_id: Samsara user ID of the mechanic creating the DVIR.

          safety_status: Whether or not this vehicle or trailer is safe to drive.

          type: Only type 'mechanic' is currently accepted.

          license_plate: The license plate of this vehicle.

          location: Optional string if your jurisdiction requires a location of the DVIR.

          mechanic_notes: The mechanics notes on the DVIR.

          odometer_meters: The odometer reading in meters.

          resolved_defect_ids: Array of ids for defects being resolved with this DVIR.

          trailer_id: Id of trailer being inspected. Either vehicleId or trailerId must be provided.

          vehicle_id: Id of vehicle being inspected. Either vehicleId or trailerId must be provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fleet/dvirs",
            body=await async_maybe_transform(
                {
                    "author_id": author_id,
                    "safety_status": safety_status,
                    "type": type,
                    "license_plate": license_plate,
                    "location": location,
                    "mechanic_notes": mechanic_notes,
                    "odometer_meters": odometer_meters,
                    "resolved_defect_ids": resolved_defect_ids,
                    "trailer_id": trailer_id,
                    "vehicle_id": vehicle_id,
                },
                dvir_create_params.DvirCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DvirCreateResponse,
        )

    async def resolve(
        self,
        id: str,
        *,
        author_id: str,
        is_resolved: bool,
        mechanic_notes: str | NotGiven = NOT_GIVEN,
        signed_at_time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DvirResolveResponse:
        """
        Resolves a given DVIR by marking its `isResolved` field to `true`.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write DVIRs** under the Maintenance category when
        creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          author_id: The user who is resolving the dvir.

          is_resolved: Resolves the DVIR. Must be `true`.

          mechanic_notes: The mechanics notes on the DVIR.

          signed_at_time: Time when user signed this DVIR. Defaults to now. UTC timestamp in RFC 3339
              format. Example: `2020-01-27T07:06:25Z`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/fleet/dvirs/{id}",
            body=await async_maybe_transform(
                {
                    "author_id": author_id,
                    "is_resolved": is_resolved,
                    "mechanic_notes": mechanic_notes,
                    "signed_at_time": signed_at_time,
                },
                dvir_resolve_params.DvirResolveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DvirResolveResponse,
        )


class DvirsResourceWithRawResponse:
    def __init__(self, dvirs: DvirsResource) -> None:
        self._dvirs = dvirs

        self.create = to_raw_response_wrapper(
            dvirs.create,
        )
        self.resolve = to_raw_response_wrapper(
            dvirs.resolve,
        )

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._dvirs.history)


class AsyncDvirsResourceWithRawResponse:
    def __init__(self, dvirs: AsyncDvirsResource) -> None:
        self._dvirs = dvirs

        self.create = async_to_raw_response_wrapper(
            dvirs.create,
        )
        self.resolve = async_to_raw_response_wrapper(
            dvirs.resolve,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._dvirs.history)


class DvirsResourceWithStreamingResponse:
    def __init__(self, dvirs: DvirsResource) -> None:
        self._dvirs = dvirs

        self.create = to_streamed_response_wrapper(
            dvirs.create,
        )
        self.resolve = to_streamed_response_wrapper(
            dvirs.resolve,
        )

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._dvirs.history)


class AsyncDvirsResourceWithStreamingResponse:
    def __init__(self, dvirs: AsyncDvirsResource) -> None:
        self._dvirs = dvirs

        self.create = async_to_streamed_response_wrapper(
            dvirs.create,
        )
        self.resolve = async_to_streamed_response_wrapper(
            dvirs.resolve,
        )

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._dvirs.history)
