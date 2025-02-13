# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import fuel_purchase_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.fuel_purchase_post_fuel_purchase_response_body import FuelPurchasePostFuelPurchaseResponseBody

__all__ = ["FuelPurchasesResource", "AsyncFuelPurchasesResource"]


class FuelPurchasesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FuelPurchasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return FuelPurchasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FuelPurchasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return FuelPurchasesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        fuel_quantity_liters: str,
        transaction_location: str,
        transaction_price: fuel_purchase_create_params.TransactionPrice,
        transaction_reference: str,
        transaction_time: str,
        ifta_fuel_type: Literal[
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
        vehicle_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FuelPurchasePostFuelPurchaseResponseBody:
        """
        Create a fuel purchase transaction.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Fuel Purchase** under the Fuel & Energy
        category when creating or editing an API token.
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
          fuel_quantity_liters: The amount of fuel purchased in liters.

          transaction_location: The full street address for the location of the fuel transaction, as it might be
              recognized by Google Maps. Ideal entries should be in accordance with the format
              used by the national postal service of the country concerned (example: 1 De Haro
              St, San Francisco, CA 94107, United States). Alternatively, exact
              latitude/longitude can be provided (example: 40.748441, -73.985664).

          transaction_price: The price of the fuel transaction in the currency of the country where the
              transaction occurred.

          transaction_reference: The fuel transaction reference. This is the transaction identifier. For
              instance, this can be the Serial Number on the invoice.

          transaction_time: The time of the fuel transaction in RFC 3339 format. Timezone must be specified.
              For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.

          ifta_fuel_type: The type of fuel purchased supported by IFTA. Valid values: `Unspecified`,
              `A55`, `Biodiesel`, `CompressedNaturalGas`, `Diesel`, `E85`, `Electricity`,
              `Ethanol`, `Gasohol`, `Gasoline`, `Hydrogen`, `LiquifiedNaturalGas`, `M85`,
              `Methanol`, `Propane`, `Other`

          vehicle_id: Samsara ID of the vehicle that purchased the fuel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fuel-purchase",
            body=maybe_transform(
                {
                    "fuel_quantity_liters": fuel_quantity_liters,
                    "transaction_location": transaction_location,
                    "transaction_price": transaction_price,
                    "transaction_reference": transaction_reference,
                    "transaction_time": transaction_time,
                    "ifta_fuel_type": ifta_fuel_type,
                    "vehicle_id": vehicle_id,
                },
                fuel_purchase_create_params.FuelPurchaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FuelPurchasePostFuelPurchaseResponseBody,
        )


class AsyncFuelPurchasesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFuelPurchasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFuelPurchasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFuelPurchasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncFuelPurchasesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        fuel_quantity_liters: str,
        transaction_location: str,
        transaction_price: fuel_purchase_create_params.TransactionPrice,
        transaction_reference: str,
        transaction_time: str,
        ifta_fuel_type: Literal[
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
        vehicle_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FuelPurchasePostFuelPurchaseResponseBody:
        """
        Create a fuel purchase transaction.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Fuel Purchase** under the Fuel & Energy
        category when creating or editing an API token.
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
          fuel_quantity_liters: The amount of fuel purchased in liters.

          transaction_location: The full street address for the location of the fuel transaction, as it might be
              recognized by Google Maps. Ideal entries should be in accordance with the format
              used by the national postal service of the country concerned (example: 1 De Haro
              St, San Francisco, CA 94107, United States). Alternatively, exact
              latitude/longitude can be provided (example: 40.748441, -73.985664).

          transaction_price: The price of the fuel transaction in the currency of the country where the
              transaction occurred.

          transaction_reference: The fuel transaction reference. This is the transaction identifier. For
              instance, this can be the Serial Number on the invoice.

          transaction_time: The time of the fuel transaction in RFC 3339 format. Timezone must be specified.
              For example, 2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.

          ifta_fuel_type: The type of fuel purchased supported by IFTA. Valid values: `Unspecified`,
              `A55`, `Biodiesel`, `CompressedNaturalGas`, `Diesel`, `E85`, `Electricity`,
              `Ethanol`, `Gasohol`, `Gasoline`, `Hydrogen`, `LiquifiedNaturalGas`, `M85`,
              `Methanol`, `Propane`, `Other`

          vehicle_id: Samsara ID of the vehicle that purchased the fuel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fuel-purchase",
            body=await async_maybe_transform(
                {
                    "fuel_quantity_liters": fuel_quantity_liters,
                    "transaction_location": transaction_location,
                    "transaction_price": transaction_price,
                    "transaction_reference": transaction_reference,
                    "transaction_time": transaction_time,
                    "ifta_fuel_type": ifta_fuel_type,
                    "vehicle_id": vehicle_id,
                },
                fuel_purchase_create_params.FuelPurchaseCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FuelPurchasePostFuelPurchaseResponseBody,
        )


class FuelPurchasesResourceWithRawResponse:
    def __init__(self, fuel_purchases: FuelPurchasesResource) -> None:
        self._fuel_purchases = fuel_purchases

        self.create = to_raw_response_wrapper(
            fuel_purchases.create,
        )


class AsyncFuelPurchasesResourceWithRawResponse:
    def __init__(self, fuel_purchases: AsyncFuelPurchasesResource) -> None:
        self._fuel_purchases = fuel_purchases

        self.create = async_to_raw_response_wrapper(
            fuel_purchases.create,
        )


class FuelPurchasesResourceWithStreamingResponse:
    def __init__(self, fuel_purchases: FuelPurchasesResource) -> None:
        self._fuel_purchases = fuel_purchases

        self.create = to_streamed_response_wrapper(
            fuel_purchases.create,
        )


class AsyncFuelPurchasesResourceWithStreamingResponse:
    def __init__(self, fuel_purchases: AsyncFuelPurchasesResource) -> None:
        self._fuel_purchases = fuel_purchases

        self.create = async_to_streamed_response_wrapper(
            fuel_purchases.create,
        )
