# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ....types.fleet.reports import ifta_jurisdiction_list_params
from ....types.fleet.reports.ifta_jurisdiction_list_response import IftaJurisdictionListResponse

__all__ = ["IftaJurisdictionResource", "AsyncIftaJurisdictionResource"]


class IftaJurisdictionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IftaJurisdictionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return IftaJurisdictionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IftaJurisdictionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return IftaJurisdictionResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        year: int,
        fuel_type: Literal[
            "Unspecified",
            "A55",
            "Biodiesel",
            "CompressedNaturalGas",
            "Diesel",
            "E85",
            "Electricity",
            "Ethanol",
            "Gasohol",
            "Gasoline",
            "Hydrogen",
            "LiquifiedNaturalGas",
            "M85",
            "Methanol",
            "Propane",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        jurisdictions: str | NotGiven = NOT_GIVEN,
        month: Literal[
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        quarter: Literal["Q1", "Q2", "Q3", "Q4"] | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        vehicle_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IftaJurisdictionListResponse:
        """Get all jurisdiction IFTA reports for the requested time duration.

        Data is
        returned in your organization's defined timezone.

        **Note:** The most recent 72 hours of data may still be processing and is
        subject to change and latency, so it is not recommended to request data for the
        most recent 72 hours.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read IFTA (US)** under the Compliance category
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
          year: The year of the requested IFTA report summary. Must be provided with a month or
              quarter param. Example: `year=2021`

          fuel_type: A filter on the data based on this comma-separated list of IFTA fuel types.
              Example: `fuelType=Diesel` Valid values: `Unspecified`, `A55`, `Biodiesel`,
              `CompressedNaturalGas`, `Diesel`, `E85`, `Electricity`, `Ethanol`, `Gasohol`,
              `Gasoline`, `Hydrogen`, `LiquifiedNaturalGas`, `M85`, `Methanol`, `Propane`,
              `Other`

          jurisdictions: A filter on the data based on this comma-separated list of jurisdictions.
              Example: `jurisdictions=GA`

          month: The month of the requested IFTA report summary. Can not be provided with the
              quarter param. Example: `month=January` Valid values: `January`, `February`,
              `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`,
              `November`, `December`

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          quarter: The quarter of the requested IFTA report summary. Can not be provided with the
              month param. Q1: January, February, March. Q2: April, May, June. Q3: July,
              August, September. Q4: October, November, December. Example: `quarter=Q1` Valid
              values: `Q1`, `Q2`, `Q3`, `Q4`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          vehicle_ids: A filter on the data based on this comma-separated list of vehicle IDs and
              externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/fleet/reports/ifta/jurisdiction",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "year": year,
                        "fuel_type": fuel_type,
                        "jurisdictions": jurisdictions,
                        "month": month,
                        "parent_tag_ids": parent_tag_ids,
                        "quarter": quarter,
                        "tag_ids": tag_ids,
                        "vehicle_ids": vehicle_ids,
                    },
                    ifta_jurisdiction_list_params.IftaJurisdictionListParams,
                ),
            ),
            cast_to=IftaJurisdictionListResponse,
        )


class AsyncIftaJurisdictionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIftaJurisdictionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIftaJurisdictionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIftaJurisdictionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncIftaJurisdictionResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        year: int,
        fuel_type: Literal[
            "Unspecified",
            "A55",
            "Biodiesel",
            "CompressedNaturalGas",
            "Diesel",
            "E85",
            "Electricity",
            "Ethanol",
            "Gasohol",
            "Gasoline",
            "Hydrogen",
            "LiquifiedNaturalGas",
            "M85",
            "Methanol",
            "Propane",
            "Other",
        ]
        | NotGiven = NOT_GIVEN,
        jurisdictions: str | NotGiven = NOT_GIVEN,
        month: Literal[
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        | NotGiven = NOT_GIVEN,
        parent_tag_ids: str | NotGiven = NOT_GIVEN,
        quarter: Literal["Q1", "Q2", "Q3", "Q4"] | NotGiven = NOT_GIVEN,
        tag_ids: str | NotGiven = NOT_GIVEN,
        vehicle_ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IftaJurisdictionListResponse:
        """Get all jurisdiction IFTA reports for the requested time duration.

        Data is
        returned in your organization's defined timezone.

        **Note:** The most recent 72 hours of data may still be processing and is
        subject to change and latency, so it is not recommended to request data for the
        most recent 72 hours.

        <b>Rate limit:</b> 5 requests/sec (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read IFTA (US)** under the Compliance category
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
          year: The year of the requested IFTA report summary. Must be provided with a month or
              quarter param. Example: `year=2021`

          fuel_type: A filter on the data based on this comma-separated list of IFTA fuel types.
              Example: `fuelType=Diesel` Valid values: `Unspecified`, `A55`, `Biodiesel`,
              `CompressedNaturalGas`, `Diesel`, `E85`, `Electricity`, `Ethanol`, `Gasohol`,
              `Gasoline`, `Hydrogen`, `LiquifiedNaturalGas`, `M85`, `Methanol`, `Propane`,
              `Other`

          jurisdictions: A filter on the data based on this comma-separated list of jurisdictions.
              Example: `jurisdictions=GA`

          month: The month of the requested IFTA report summary. Can not be provided with the
              quarter param. Example: `month=January` Valid values: `January`, `February`,
              `March`, `April`, `May`, `June`, `July`, `August`, `September`, `October`,
              `November`, `December`

          parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for
              use by orgs with tag hierarchies. Specifying a parent tag will implicitly
              include all descendent tags of the parent tag. Example: `parentTagIds=345,678`

          quarter: The quarter of the requested IFTA report summary. Can not be provided with the
              month param. Q1: January, February, March. Q2: April, May, June. Q3: July,
              August, September. Q4: October, November, December. Example: `quarter=Q1` Valid
              values: `Q1`, `Q2`, `Q3`, `Q4`

          tag_ids:
              A filter on the data based on this comma-separated list of tag IDs. Example:
              `tagIds=1234,5678`

          vehicle_ids: A filter on the data based on this comma-separated list of vehicle IDs and
              externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/fleet/reports/ifta/jurisdiction",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "year": year,
                        "fuel_type": fuel_type,
                        "jurisdictions": jurisdictions,
                        "month": month,
                        "parent_tag_ids": parent_tag_ids,
                        "quarter": quarter,
                        "tag_ids": tag_ids,
                        "vehicle_ids": vehicle_ids,
                    },
                    ifta_jurisdiction_list_params.IftaJurisdictionListParams,
                ),
            ),
            cast_to=IftaJurisdictionListResponse,
        )


class IftaJurisdictionResourceWithRawResponse:
    def __init__(self, ifta_jurisdiction: IftaJurisdictionResource) -> None:
        self._ifta_jurisdiction = ifta_jurisdiction

        self.list = to_raw_response_wrapper(
            ifta_jurisdiction.list,
        )


class AsyncIftaJurisdictionResourceWithRawResponse:
    def __init__(self, ifta_jurisdiction: AsyncIftaJurisdictionResource) -> None:
        self._ifta_jurisdiction = ifta_jurisdiction

        self.list = async_to_raw_response_wrapper(
            ifta_jurisdiction.list,
        )


class IftaJurisdictionResourceWithStreamingResponse:
    def __init__(self, ifta_jurisdiction: IftaJurisdictionResource) -> None:
        self._ifta_jurisdiction = ifta_jurisdiction

        self.list = to_streamed_response_wrapper(
            ifta_jurisdiction.list,
        )


class AsyncIftaJurisdictionResourceWithStreamingResponse:
    def __init__(self, ifta_jurisdiction: AsyncIftaJurisdictionResource) -> None:
        self._ifta_jurisdiction = ifta_jurisdiction

        self.list = async_to_streamed_response_wrapper(
            ifta_jurisdiction.list,
        )
