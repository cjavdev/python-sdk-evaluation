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
from ...types.fleet import carrier_proposed_assignment_list_params, carrier_proposed_assignment_create_params
from ..._base_client import make_request_options
from ...types.fleet.carrier_proposed_assignment_list_response import CarrierProposedAssignmentListResponse
from ...types.fleet.carrier_proposed_assignment_create_response import CarrierProposedAssignmentCreateResponse

__all__ = ["CarrierProposedAssignmentsResource", "AsyncCarrierProposedAssignmentsResource"]


class CarrierProposedAssignmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CarrierProposedAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return CarrierProposedAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CarrierProposedAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return CarrierProposedAssignmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        driver_id: str,
        vehicle_id: str,
        active_time: str | NotGiven = NOT_GIVEN,
        shipping_docs: str | NotGiven = NOT_GIVEN,
        trailer_ids: List[str] | NotGiven = NOT_GIVEN,
        trailer_names: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CarrierProposedAssignmentCreateResponse:
        """Creates a new assignment that a driver can later use.

        Each driver can only have
        one future assignment.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Carrier-Proposed Assignments** under the
        Assignments category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          driver_id: ID for the driver for the driver that this assignment is for. This can be either
              a unique Samsara ID or an external ID for the driver.

          vehicle_id: ID for the vehicle to propose. This can be either a unique Samsara ID or an
              external ID for the vehicle.

          active_time: Time after which this assignment will be active and visible to the driver on the
              mobile app. Not setting it makes it active now. UTC timestamp in RFC 3339
              format. Example: `2020-01-27T07:06:25Z`.

          shipping_docs: Shipping Documents that this assignment will propose to the driver.

          trailer_ids: IDs of trailers to propose. This can be either a unique Samsara IDs or an
              external IDs for the trailers. (forbidden if trailerNames is set)

          trailer_names: Names of trailers to propose. (forbidden if trailerIds is set)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fleet/carrier-proposed-assignments",
            body=maybe_transform(
                {
                    "driver_id": driver_id,
                    "vehicle_id": vehicle_id,
                    "active_time": active_time,
                    "shipping_docs": shipping_docs,
                    "trailer_ids": trailer_ids,
                    "trailer_names": trailer_names,
                },
                carrier_proposed_assignment_create_params.CarrierProposedAssignmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CarrierProposedAssignmentCreateResponse,
        )

    def list(
        self,
        *,
        active_time: str | NotGiven = NOT_GIVEN,
        after: str | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CarrierProposedAssignmentListResponse:
        """
        Show the assignments created by the POST fleet/carrier-proposed-assignments.
        This endpoint will only show the assignments that are active for drivers and
        currently visible to them in the driver app. Once a proposed assignment has been
        accepted, the endpoint will not return any data.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Carrier-Proposed Assignments** under the
        Assignments category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          active_time: If specified, shows assignments that will be active at this time. Defaults to
              now, which would show current active assignments. In RFC 3339 format.
              Millisecond precision and timezones are supported. (Examples:
              2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          driver_ids: A filter on the data based on this comma-separated list of driver IDs and
              externalIds. Example: `driverIds=1234,5678,payroll:4841`

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 512 objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fleet/carrier-proposed-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active_time": active_time,
                        "after": after,
                        "driver_ids": driver_ids,
                        "limit": limit,
                    },
                    carrier_proposed_assignment_list_params.CarrierProposedAssignmentListParams,
                ),
            ),
            cast_to=CarrierProposedAssignmentListResponse,
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
    ) -> str:
        """Permanently delete an assignment.

        You can only delete assignments that are not
        yet active. To override a currently active assignment, create a new empty one,
        instead.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Carrier-Proposed Assignments** under the
        Assignments category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/fleet/carrier-proposed-assignments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncCarrierProposedAssignmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCarrierProposedAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCarrierProposedAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCarrierProposedAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncCarrierProposedAssignmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        driver_id: str,
        vehicle_id: str,
        active_time: str | NotGiven = NOT_GIVEN,
        shipping_docs: str | NotGiven = NOT_GIVEN,
        trailer_ids: List[str] | NotGiven = NOT_GIVEN,
        trailer_names: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CarrierProposedAssignmentCreateResponse:
        """Creates a new assignment that a driver can later use.

        Each driver can only have
        one future assignment.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Carrier-Proposed Assignments** under the
        Assignments category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          driver_id: ID for the driver for the driver that this assignment is for. This can be either
              a unique Samsara ID or an external ID for the driver.

          vehicle_id: ID for the vehicle to propose. This can be either a unique Samsara ID or an
              external ID for the vehicle.

          active_time: Time after which this assignment will be active and visible to the driver on the
              mobile app. Not setting it makes it active now. UTC timestamp in RFC 3339
              format. Example: `2020-01-27T07:06:25Z`.

          shipping_docs: Shipping Documents that this assignment will propose to the driver.

          trailer_ids: IDs of trailers to propose. This can be either a unique Samsara IDs or an
              external IDs for the trailers. (forbidden if trailerNames is set)

          trailer_names: Names of trailers to propose. (forbidden if trailerIds is set)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fleet/carrier-proposed-assignments",
            body=await async_maybe_transform(
                {
                    "driver_id": driver_id,
                    "vehicle_id": vehicle_id,
                    "active_time": active_time,
                    "shipping_docs": shipping_docs,
                    "trailer_ids": trailer_ids,
                    "trailer_names": trailer_names,
                },
                carrier_proposed_assignment_create_params.CarrierProposedAssignmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CarrierProposedAssignmentCreateResponse,
        )

    async def list(
        self,
        *,
        active_time: str | NotGiven = NOT_GIVEN,
        after: str | NotGiven = NOT_GIVEN,
        driver_ids: List[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CarrierProposedAssignmentListResponse:
        """
        Show the assignments created by the POST fleet/carrier-proposed-assignments.
        This endpoint will only show the assignments that are active for drivers and
        currently visible to them in the driver app. Once a proposed assignment has been
        accepted, the endpoint will not return any data.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Carrier-Proposed Assignments** under the
        Assignments category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          active_time: If specified, shows assignments that will be active at this time. Defaults to
              now, which would show current active assignments. In RFC 3339 format.
              Millisecond precision and timezones are supported. (Examples:
              2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).

          after: If specified, this should be the endCursor value from the previous page of
              results. When present, this request will return the next page of results that
              occur immediately after the previous page of results.

          driver_ids: A filter on the data based on this comma-separated list of driver IDs and
              externalIds. Example: `driverIds=1234,5678,payroll:4841`

          limit: The limit for how many objects will be in the response. Default and max for this
              value is 512 objects.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fleet/carrier-proposed-assignments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "active_time": active_time,
                        "after": after,
                        "driver_ids": driver_ids,
                        "limit": limit,
                    },
                    carrier_proposed_assignment_list_params.CarrierProposedAssignmentListParams,
                ),
            ),
            cast_to=CarrierProposedAssignmentListResponse,
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
    ) -> str:
        """Permanently delete an assignment.

        You can only delete assignments that are not
        yet active. To override a currently active assignment, create a new empty one,
        instead.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Write Carrier-Proposed Assignments** under the
        Assignments category when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/fleet/carrier-proposed-assignments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class CarrierProposedAssignmentsResourceWithRawResponse:
    def __init__(self, carrier_proposed_assignments: CarrierProposedAssignmentsResource) -> None:
        self._carrier_proposed_assignments = carrier_proposed_assignments

        self.create = to_raw_response_wrapper(
            carrier_proposed_assignments.create,
        )
        self.list = to_raw_response_wrapper(
            carrier_proposed_assignments.list,
        )
        self.delete = to_raw_response_wrapper(
            carrier_proposed_assignments.delete,
        )


class AsyncCarrierProposedAssignmentsResourceWithRawResponse:
    def __init__(self, carrier_proposed_assignments: AsyncCarrierProposedAssignmentsResource) -> None:
        self._carrier_proposed_assignments = carrier_proposed_assignments

        self.create = async_to_raw_response_wrapper(
            carrier_proposed_assignments.create,
        )
        self.list = async_to_raw_response_wrapper(
            carrier_proposed_assignments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            carrier_proposed_assignments.delete,
        )


class CarrierProposedAssignmentsResourceWithStreamingResponse:
    def __init__(self, carrier_proposed_assignments: CarrierProposedAssignmentsResource) -> None:
        self._carrier_proposed_assignments = carrier_proposed_assignments

        self.create = to_streamed_response_wrapper(
            carrier_proposed_assignments.create,
        )
        self.list = to_streamed_response_wrapper(
            carrier_proposed_assignments.list,
        )
        self.delete = to_streamed_response_wrapper(
            carrier_proposed_assignments.delete,
        )


class AsyncCarrierProposedAssignmentsResourceWithStreamingResponse:
    def __init__(self, carrier_proposed_assignments: AsyncCarrierProposedAssignmentsResource) -> None:
        self._carrier_proposed_assignments = carrier_proposed_assignments

        self.create = async_to_streamed_response_wrapper(
            carrier_proposed_assignments.create,
        )
        self.list = async_to_streamed_response_wrapper(
            carrier_proposed_assignments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            carrier_proposed_assignments.delete,
        )
