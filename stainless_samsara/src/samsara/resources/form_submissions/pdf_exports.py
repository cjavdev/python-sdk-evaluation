# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ..._base_client import make_request_options
from ...types.form_submissions import pdf_export_create_params, pdf_export_retrieve_params
from ...types.form_submissions.form_submissions_get_form_submissions_pdf_exports_response_body import (
    FormSubmissionsGetFormSubmissionsPdfExportsResponseBody,
)
from ...types.form_submissions.form_submissions_post_form_submissions_pdf_exports_response_body import (
    FormSubmissionsPostFormSubmissionsPdfExportsResponseBody,
)

__all__ = ["PdfExportsResource", "AsyncPdfExportsResource"]


class PdfExportsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PdfExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return PdfExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PdfExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return PdfExportsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormSubmissionsPostFormSubmissionsPdfExportsResponseBody:
        """
        Creates a PDF export for a form submission.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Form Submissions** under the Closed Beta
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
          id: ID of the form submission to create a PDF export from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/form-submissions/pdf-exports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, pdf_export_create_params.PdfExportCreateParams),
            ),
            cast_to=FormSubmissionsPostFormSubmissionsPdfExportsResponseBody,
        )

    def retrieve(
        self,
        *,
        pdf_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormSubmissionsGetFormSubmissionsPdfExportsResponseBody:
        """
        Returns a PDF export for a form submission.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Form Submissions** under the Closed Beta
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
          pdf_id: ID of the form submission PDF export.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/form-submissions/pdf-exports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"pdf_id": pdf_id}, pdf_export_retrieve_params.PdfExportRetrieveParams),
            ),
            cast_to=FormSubmissionsGetFormSubmissionsPdfExportsResponseBody,
        )


class AsyncPdfExportsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPdfExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPdfExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPdfExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/samsara-python#with_streaming_response
        """
        return AsyncPdfExportsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormSubmissionsPostFormSubmissionsPdfExportsResponseBody:
        """
        Creates a PDF export for a form submission.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Write Form Submissions** under the Closed Beta
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
          id: ID of the form submission to create a PDF export from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/form-submissions/pdf-exports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, pdf_export_create_params.PdfExportCreateParams),
            ),
            cast_to=FormSubmissionsPostFormSubmissionsPdfExportsResponseBody,
        )

    async def retrieve(
        self,
        *,
        pdf_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormSubmissionsGetFormSubmissionsPdfExportsResponseBody:
        """
        Returns a PDF export for a form submission.

        **Beta:** This endpoint is in beta and is likely to change before being broadly
        available. Reach out to your Samsara Representative to have Forms APIs enabled
        for your organization.

        <b>Rate limit:</b> 100 requests/min (learn more about rate limits
        <a href="https://developers.samsara.com/docs/rate-limits" target="_blank">here</a>).

        To use this endpoint, select **Read Form Submissions** under the Closed Beta
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
          pdf_id: ID of the form submission PDF export.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/form-submissions/pdf-exports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"pdf_id": pdf_id}, pdf_export_retrieve_params.PdfExportRetrieveParams
                ),
            ),
            cast_to=FormSubmissionsGetFormSubmissionsPdfExportsResponseBody,
        )


class PdfExportsResourceWithRawResponse:
    def __init__(self, pdf_exports: PdfExportsResource) -> None:
        self._pdf_exports = pdf_exports

        self.create = to_raw_response_wrapper(
            pdf_exports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            pdf_exports.retrieve,
        )


class AsyncPdfExportsResourceWithRawResponse:
    def __init__(self, pdf_exports: AsyncPdfExportsResource) -> None:
        self._pdf_exports = pdf_exports

        self.create = async_to_raw_response_wrapper(
            pdf_exports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            pdf_exports.retrieve,
        )


class PdfExportsResourceWithStreamingResponse:
    def __init__(self, pdf_exports: PdfExportsResource) -> None:
        self._pdf_exports = pdf_exports

        self.create = to_streamed_response_wrapper(
            pdf_exports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            pdf_exports.retrieve,
        )


class AsyncPdfExportsResourceWithStreamingResponse:
    def __init__(self, pdf_exports: AsyncPdfExportsResource) -> None:
        self._pdf_exports = pdf_exports

        self.create = async_to_streamed_response_wrapper(
            pdf_exports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            pdf_exports.retrieve,
        )
