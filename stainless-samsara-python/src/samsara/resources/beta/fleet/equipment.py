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
from ...._base_client import make_request_options
from ....types.beta.fleet import equipment_update_params
from ....types.beta.fleet.equipment_update_response import EquipmentUpdateResponse

__all__ = ["EquipmentResource", "AsyncEquipmentResource"]


class EquipmentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EquipmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return EquipmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EquipmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return EquipmentResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        path_id: str,
        body_id: str | NotGiven = NOT_GIVEN,
        attributes: Iterable[equipment_update_params.Attribute] | NotGiven = NOT_GIVEN,
        engine_hours: int | NotGiven = NOT_GIVEN,
        equipment_serial_number: str | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        odometer_meters: int | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EquipmentUpdateResponse:
        """Update an equipment.

        **Note** this implementation of patch uses
        [the JSON merge patch](https://tools.ietf.org/html/rfc7396) proposed standard.
        This means that any fields included in the patch request will _overwrite_ fields
        which exist on the target resource. For arrays, this means any array included in
        the request will _replace_ the array that exists at the specified path, it will
        not _add_ to the existing array

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Equipment** under the Equipment category
        when creating or editing an API token.
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
          body_id: The unique Samsara ID of the Equipment. This is automatically generated when the
              Equipment object is created. It cannot be changed.

          attributes: List of attributes associated with the entity

          engine_hours: When you provide a manual engine hours override, Samsara will begin updating a
              equipment's engine hours used since this override was set.

          equipment_serial_number: The serial number of the equipment.

          external_ids: A map of external ids

          name: The human-readable name of the Equipment. This is set by a fleet administrator
              and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver
              mobile app. By default, this name is the serial number of the Samsara Asset
              Gateway. It can be set or updated through the Samsara Dashboard or through the
              API at any time.

          notes: These are generic notes about the Equipment. Empty by default. Can be set or
              updated through the Samsara Dashboard or the API at any time.

          odometer_meters: When you provide a manual odometer override, Samsara will begin updating a
              equipment's odometer using GPS distance traveled since this override was set.

          tag_ids: An array of IDs of tags to associate with this equipment. If your access to the
              API is scoped by one or more tags, this field is required to pass in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._patch(
            f"/beta/fleet/equipment/{path_id}",
            body=maybe_transform(
                {
                    "body_id": body_id,
                    "attributes": attributes,
                    "engine_hours": engine_hours,
                    "equipment_serial_number": equipment_serial_number,
                    "external_ids": external_ids,
                    "name": name,
                    "notes": notes,
                    "odometer_meters": odometer_meters,
                    "tag_ids": tag_ids,
                },
                equipment_update_params.EquipmentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EquipmentUpdateResponse,
        )


class AsyncEquipmentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEquipmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEquipmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEquipmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncEquipmentResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        path_id: str,
        body_id: str | NotGiven = NOT_GIVEN,
        attributes: Iterable[equipment_update_params.Attribute] | NotGiven = NOT_GIVEN,
        engine_hours: int | NotGiven = NOT_GIVEN,
        equipment_serial_number: str | NotGiven = NOT_GIVEN,
        external_ids: Dict[str, str] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        notes: str | NotGiven = NOT_GIVEN,
        odometer_meters: int | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EquipmentUpdateResponse:
        """Update an equipment.

        **Note** this implementation of patch uses
        [the JSON merge patch](https://tools.ietf.org/html/rfc7396) proposed standard.
        This means that any fields included in the patch request will _overwrite_ fields
        which exist on the target resource. For arrays, this means any array included in
        the request will _replace_ the array that exists at the specified path, it will
        not _add_ to the existing array

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Equipment** under the Equipment category
        when creating or editing an API token.
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
          body_id: The unique Samsara ID of the Equipment. This is automatically generated when the
              Equipment object is created. It cannot be changed.

          attributes: List of attributes associated with the entity

          engine_hours: When you provide a manual engine hours override, Samsara will begin updating a
              equipment's engine hours used since this override was set.

          equipment_serial_number: The serial number of the equipment.

          external_ids: A map of external ids

          name: The human-readable name of the Equipment. This is set by a fleet administrator
              and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver
              mobile app. By default, this name is the serial number of the Samsara Asset
              Gateway. It can be set or updated through the Samsara Dashboard or through the
              API at any time.

          notes: These are generic notes about the Equipment. Empty by default. Can be set or
              updated through the Samsara Dashboard or the API at any time.

          odometer_meters: When you provide a manual odometer override, Samsara will begin updating a
              equipment's odometer using GPS distance traveled since this override was set.

          tag_ids: An array of IDs of tags to associate with this equipment. If your access to the
              API is scoped by one or more tags, this field is required to pass in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._patch(
            f"/beta/fleet/equipment/{path_id}",
            body=await async_maybe_transform(
                {
                    "body_id": body_id,
                    "attributes": attributes,
                    "engine_hours": engine_hours,
                    "equipment_serial_number": equipment_serial_number,
                    "external_ids": external_ids,
                    "name": name,
                    "notes": notes,
                    "odometer_meters": odometer_meters,
                    "tag_ids": tag_ids,
                },
                equipment_update_params.EquipmentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EquipmentUpdateResponse,
        )


class EquipmentResourceWithRawResponse:
    def __init__(self, equipment: EquipmentResource) -> None:
        self._equipment = equipment

        self.update = to_raw_response_wrapper(
            equipment.update,
        )


class AsyncEquipmentResourceWithRawResponse:
    def __init__(self, equipment: AsyncEquipmentResource) -> None:
        self._equipment = equipment

        self.update = async_to_raw_response_wrapper(
            equipment.update,
        )


class EquipmentResourceWithStreamingResponse:
    def __init__(self, equipment: EquipmentResource) -> None:
        self._equipment = equipment

        self.update = to_streamed_response_wrapper(
            equipment.update,
        )


class AsyncEquipmentResourceWithStreamingResponse:
    def __init__(self, equipment: AsyncEquipmentResource) -> None:
        self._equipment = equipment

        self.update = async_to_streamed_response_wrapper(
            equipment.update,
        )
