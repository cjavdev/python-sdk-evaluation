# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .locations import (
    LocationsResource,
    AsyncLocationsResource,
    LocationsResourceWithRawResponse,
    AsyncLocationsResourceWithRawResponse,
    LocationsResourceWithStreamingResponse,
    AsyncLocationsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.fleet import equipment_list_params
from ...._base_client import make_request_options
from ....types.fleet.equipment_list_response import EquipmentListResponse

__all__ = ["EquipmentResource", "AsyncEquipmentResource"]


class EquipmentResource(SyncAPIResource):
    @cached_property
    def locations(self) -> LocationsResource:
        return LocationsResource(self._client)

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

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EquipmentListResponse:
        """Returns a list of all equipment in an organization.

        Equipment objects represent
        powered assets connected to a
        [Samsara AG26](https://www.samsara.com/products/models/ag26) via an APWR, CAT,
        or J1939 cable. They are automatically created with a unique Samsara Equipment
        ID whenever an AG26 is activated in your organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Equipment** under the Equipment category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

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
            "/fleet/equipment",
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
                    equipment_list_params.EquipmentListParams,
                ),
            ),
            cast_to=EquipmentListResponse,
        )


class AsyncEquipmentResource(AsyncAPIResource):
    @cached_property
    def locations(self) -> AsyncLocationsResource:
        return AsyncLocationsResource(self._client)

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

    async def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        parent_tag_ids: List[str] | NotGiven = NOT_GIVEN,
        tag_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EquipmentListResponse:
        """Returns a list of all equipment in an organization.

        Equipment objects represent
        powered assets connected to a
        [Samsara AG26](https://www.samsara.com/products/models/ag26) via an APWR, CAT,
        or J1939 cable. They are automatically created with a unique Samsara Equipment
        ID whenever an AG26 is activated in your organization.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed
        as feedback in our
        <a href="https://forms.gle/zkD4NCH7HjKb7mm69" target="_blank">API feedback
        form</a>. If you encountered an issue or noticed inaccuracies in the API
        documentation, please
        <a href="https://www.samsara.com/help" target="_blank">submit a case</a> to our
        support team.

        To use this endpoint, select **Read Equipment** under the Equipment category
        when creating or editing an API token.
        <a href="https://developers.samsara.com/docs/authentication#scopes-for-api-tokens" target="_blank">Learn
        More.</a>

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
            "/fleet/equipment",
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
                    equipment_list_params.EquipmentListParams,
                ),
            ),
            cast_to=EquipmentListResponse,
        )


class EquipmentResourceWithRawResponse:
    def __init__(self, equipment: EquipmentResource) -> None:
        self._equipment = equipment

        self.list = to_raw_response_wrapper(
            equipment.list,
        )

    @cached_property
    def locations(self) -> LocationsResourceWithRawResponse:
        return LocationsResourceWithRawResponse(self._equipment.locations)


class AsyncEquipmentResourceWithRawResponse:
    def __init__(self, equipment: AsyncEquipmentResource) -> None:
        self._equipment = equipment

        self.list = async_to_raw_response_wrapper(
            equipment.list,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithRawResponse:
        return AsyncLocationsResourceWithRawResponse(self._equipment.locations)


class EquipmentResourceWithStreamingResponse:
    def __init__(self, equipment: EquipmentResource) -> None:
        self._equipment = equipment

        self.list = to_streamed_response_wrapper(
            equipment.list,
        )

    @cached_property
    def locations(self) -> LocationsResourceWithStreamingResponse:
        return LocationsResourceWithStreamingResponse(self._equipment.locations)


class AsyncEquipmentResourceWithStreamingResponse:
    def __init__(self, equipment: AsyncEquipmentResource) -> None:
        self._equipment = equipment

        self.list = async_to_streamed_response_wrapper(
            equipment.list,
        )

    @cached_property
    def locations(self) -> AsyncLocationsResourceWithStreamingResponse:
        return AsyncLocationsResourceWithStreamingResponse(self._equipment.locations)
