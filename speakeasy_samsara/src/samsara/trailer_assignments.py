"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from samsara import models, utils
from samsara._hooks import HookContext
from samsara.types import OptionalNullable, UNSET
from samsara.utils import get_security_from_env
from typing import Mapping, Optional


class TrailerAssignments(BaseSDK):
    def v1get_all_trailer_assignments(
        self,
        *,
        start_ms: Optional[int] = None,
        end_ms: Optional[int] = None,
        limit: Optional[float] = None,
        starting_after: Optional[str] = None,
        ending_before: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.V1getAllTrailerAssignmentsResponse:
        r"""List trailer assignments for all trailers

        <n class=\"warning\">
        <nh>
        <i class=\"fa fa-exclamation-circle\"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Fetch trailer assignment data for all trailers in your organization.

        <b>Rate limit:</b> 100 requests/sec (learn more about rate limits <a href=\"https://developers.samsara.com/docs/rate-limits\" target=\"_blank\">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href=\"https://forms.gle/zkD4NCH7HjKb7mm69\" target=\"_blank\">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href=\"https://www.samsara.com/help\" target=\"_blank\">submit a case</a> to our support team.

        To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href=\"https://developers.samsara.com/docs/authentication#scopes-for-api-tokens\" target=\"_blank\">Learn More.</a>

        :param start_ms: Timestamp in Unix epoch miliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments.
        :param end_ms: Timestamp in Unix epoch miliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time
        :param limit: Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'.
        :param starting_after: Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter.
        :param ending_before: Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.V1getAllTrailerAssignmentsRequest(
            start_ms=start_ms,
            end_ms=end_ms,
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
        )

        req = self._build_request(
            method="GET",
            path="/v1/fleet/trailers/assignments",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="V1getAllTrailerAssignments",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.InlineResponse2007)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "default", "application/json"):
            return utils.unmarshal_json(http_res.text, str)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def v1get_all_trailer_assignments_async(
        self,
        *,
        start_ms: Optional[int] = None,
        end_ms: Optional[int] = None,
        limit: Optional[float] = None,
        starting_after: Optional[str] = None,
        ending_before: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.V1getAllTrailerAssignmentsResponse:
        r"""List trailer assignments for all trailers

        <n class=\"warning\">
        <nh>
        <i class=\"fa fa-exclamation-circle\"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Fetch trailer assignment data for all trailers in your organization.

        <b>Rate limit:</b> 100 requests/sec (learn more about rate limits <a href=\"https://developers.samsara.com/docs/rate-limits\" target=\"_blank\">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href=\"https://forms.gle/zkD4NCH7HjKb7mm69\" target=\"_blank\">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href=\"https://www.samsara.com/help\" target=\"_blank\">submit a case</a> to our support team.

        To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href=\"https://developers.samsara.com/docs/authentication#scopes-for-api-tokens\" target=\"_blank\">Learn More.</a>

        :param start_ms: Timestamp in Unix epoch miliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments.
        :param end_ms: Timestamp in Unix epoch miliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time
        :param limit: Pagination parameter indicating the number of results to return in this request. Used in conjunction with either 'startingAfter' or 'endingBefore'.
        :param starting_after: Pagination parameter indicating the cursor position to continue returning results after. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'endingBefore' parameter.
        :param ending_before: Pagination parameter indicating the cursor position to return results before. Used in conjunction with the 'limit' parameter. Mutually exclusive with 'startingAfter' parameter.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.V1getAllTrailerAssignmentsRequest(
            start_ms=start_ms,
            end_ms=end_ms,
            limit=limit,
            starting_after=starting_after,
            ending_before=ending_before,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/fleet/trailers/assignments",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="V1getAllTrailerAssignments",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.InlineResponse2007)
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "default", "application/json"):
            return utils.unmarshal_json(http_res.text, str)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def v1get_fleet_trailer_assignments(
        self,
        *,
        trailer_id: int,
        start_ms: Optional[int] = None,
        end_ms: Optional[int] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.V1getFleetTrailerAssignmentsResponse:
        r"""List trailer assignments for a given trailer

        <n class=\"warning\">
        <nh>
        <i class=\"fa fa-exclamation-circle\"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Fetch trailer assignment data for a single trailer.

        <b>Rate limit:</b> 100 requests/sec (learn more about rate limits <a href=\"https://developers.samsara.com/docs/rate-limits\" target=\"_blank\">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href=\"https://forms.gle/zkD4NCH7HjKb7mm69\" target=\"_blank\">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href=\"https://www.samsara.com/help\" target=\"_blank\">submit a case</a> to our support team.

        To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href=\"https://developers.samsara.com/docs/authentication#scopes-for-api-tokens\" target=\"_blank\">Learn More.</a>

        :param trailer_id: ID of trailer. Must contain only digits 0-9.
        :param start_ms: Timestamp in Unix epoch milliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments.
        :param end_ms: Timestamp in Unix epoch milliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.V1getFleetTrailerAssignmentsRequest(
            trailer_id=trailer_id,
            start_ms=start_ms,
            end_ms=end_ms,
        )

        req = self._build_request(
            method="GET",
            path="/v1/fleet/trailers/{trailerId}/assignments",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="V1getFleetTrailerAssignments",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, models.V1TrailerAssignmentsResponse
            )
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "default", "application/json"):
            return utils.unmarshal_json(http_res.text, str)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def v1get_fleet_trailer_assignments_async(
        self,
        *,
        trailer_id: int,
        start_ms: Optional[int] = None,
        end_ms: Optional[int] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.V1getFleetTrailerAssignmentsResponse:
        r"""List trailer assignments for a given trailer

        <n class=\"warning\">
        <nh>
        <i class=\"fa fa-exclamation-circle\"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Fetch trailer assignment data for a single trailer.

        <b>Rate limit:</b> 100 requests/sec (learn more about rate limits <a href=\"https://developers.samsara.com/docs/rate-limits\" target=\"_blank\">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href=\"https://forms.gle/zkD4NCH7HjKb7mm69\" target=\"_blank\">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href=\"https://www.samsara.com/help\" target=\"_blank\">submit a case</a> to our support team.

        To use this endpoint, select **Read Assignments** under the Assignments category when creating or editing an API token. <a href=\"https://developers.samsara.com/docs/authentication#scopes-for-api-tokens\" target=\"_blank\">Learn More.</a>

        :param trailer_id: ID of trailer. Must contain only digits 0-9.
        :param start_ms: Timestamp in Unix epoch milliseconds representing the start of the period to fetch. Omitting both startMs and endMs only returns current assignments.
        :param end_ms: Timestamp in Unix epoch milliseconds representing the end of the period to fetch. Omitting endMs sets endMs as the current time
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.V1getFleetTrailerAssignmentsRequest(
            trailer_id=trailer_id,
            start_ms=start_ms,
            end_ms=end_ms,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/fleet/trailers/{trailerId}/assignments",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="V1getFleetTrailerAssignments",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, models.V1TrailerAssignmentsResponse
            )
        if utils.match_response(http_res, "4XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "default", "application/json"):
            return utils.unmarshal_json(http_res.text, str)

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
