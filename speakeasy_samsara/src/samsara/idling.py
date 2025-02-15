"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from samsara import models, utils
from samsara._hooks import HookContext
from samsara.types import OptionalNullable, UNSET
from samsara.utils import get_security_from_env
from typing import Any, Mapping, Optional


class Idling(BaseSDK):
    def get_vehicle_idling_reports(
        self,
        *,
        start_time: str,
        end_time: str,
        after: Optional[str] = None,
        limit: Optional[int] = 512,
        vehicle_ids: Optional[str] = None,
        tag_ids: Optional[str] = None,
        parent_tag_ids: Optional[str] = None,
        is_pto_active: Optional[bool] = None,
        min_idling_duration_minutes: Optional[int] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GetVehicleIdlingReportsResponse:
        r"""Get vehicle idling reports.

        Get all vehicle idling reports for the requested time duration.

        <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href=\"https://developers.samsara.com/docs/rate-limits\" target=\"_blank\">here</a>).

        To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy category when creating or editing an API token. <a href=\"https://developers.samsara.com/docs/authentication#scopes-for-api-tokens\" target=\"_blank\">Learn More.</a>


        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href=\"https://forms.gle/zkD4NCH7HjKb7mm69\" target=\"_blank\">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href=\"https://www.samsara.com/help\" target=\"_blank\">submit a case</a> to our support team.

        :param start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
        :param end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
        :param after: If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
        :param limit: The limit for how many objects will be in the response. Default and max for this value is 512 objects.
        :param vehicle_ids: A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
        :param tag_ids: A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
        :param parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
        :param is_pto_active: A filter on the data based on power take-off being active or inactive.
        :param min_idling_duration_minutes: A filter on the data based on a minimum idling duration.
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

        request = models.GetVehicleIdlingReportsRequest(
            after=after,
            limit=limit,
            start_time=start_time,
            end_time=end_time,
            vehicle_ids=vehicle_ids,
            tag_ids=tag_ids,
            parent_tag_ids=parent_tag_ids,
            is_pto_active=is_pto_active,
            min_idling_duration_minutes=min_idling_duration_minutes,
        )

        req = self._build_request(
            method="GET",
            path="/fleet/reports/vehicle/idling",
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
                operation_id="getVehicleIdlingReports",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=[
                "401",
                "404",
                "405",
                "429",
                "4XX",
                "500",
                "501",
                "502",
                "503",
                "504",
                "5XX",
            ],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, models.IdlingReportsGetVehicleIdlingReportsResponseBody
            )
        if utils.match_response(http_res, "401", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsUnauthorizedErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsUnauthorizedErrorResponseBody(
                data=response_data
            )
        if utils.match_response(http_res, "404", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsNotFoundErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsNotFoundErrorResponseBody(
                data=response_data
            )
        if utils.match_response(http_res, "405", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsMethodNotAllowedErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsMethodNotAllowedErrorResponseBody(
                data=response_data
            )
        if utils.match_response(http_res, "429", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsTooManyRequestsErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsTooManyRequestsErrorResponseBody(
                data=response_data
            )
        if utils.match_response(http_res, "500", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsInternalServerErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsInternalServerErrorResponseBody(
                data=response_data
            )
        if utils.match_response(http_res, "501", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsNotImplementedErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsNotImplementedErrorResponseBody(
                data=response_data
            )
        if utils.match_response(http_res, "502", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsBadGatewayErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsBadGatewayErrorResponseBody(
                data=response_data
            )
        if utils.match_response(http_res, "503", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsServiceUnavailableErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsServiceUnavailableErrorResponseBody(
                data=response_data
            )
        if utils.match_response(http_res, "504", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsGatewayTimeoutErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsGatewayTimeoutErrorResponseBody(
                data=response_data
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
            return utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsBadRequestErrorResponseBody,
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_vehicle_idling_reports_async(
        self,
        *,
        start_time: str,
        end_time: str,
        after: Optional[str] = None,
        limit: Optional[int] = 512,
        vehicle_ids: Optional[str] = None,
        tag_ids: Optional[str] = None,
        parent_tag_ids: Optional[str] = None,
        is_pto_active: Optional[bool] = None,
        min_idling_duration_minutes: Optional[int] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.GetVehicleIdlingReportsResponse:
        r"""Get vehicle idling reports.

        Get all vehicle idling reports for the requested time duration.

        <b>Rate limit:</b> 25 requests/sec (learn more about rate limits <a href=\"https://developers.samsara.com/docs/rate-limits\" target=\"_blank\">here</a>).

        To use this endpoint, select **Read Fuel & Energy** under the Fuel & Energy category when creating or editing an API token. <a href=\"https://developers.samsara.com/docs/authentication#scopes-for-api-tokens\" target=\"_blank\">Learn More.</a>


        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href=\"https://forms.gle/zkD4NCH7HjKb7mm69\" target=\"_blank\">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href=\"https://www.samsara.com/help\" target=\"_blank\">submit a case</a> to our support team.

        :param start_time: A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
        :param end_time: An end time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. Note that the most recent 72 hours of data may still be processing and is subject to change and latency, so it is not recommended to request data for the most recent 72 hours. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
        :param after: If specified, this should be the endCursor value from the previous page of results. When present, this request will return the next page of results that occur immediately after the previous page of results.
        :param limit: The limit for how many objects will be in the response. Default and max for this value is 512 objects.
        :param vehicle_ids: A filter on the data based on this comma-separated list of vehicle IDs and externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
        :param tag_ids: A filter on the data based on this comma-separated list of tag IDs. Example: `tagIds=1234,5678`
        :param parent_tag_ids: A filter on the data based on this comma-separated list of parent tag IDs, for use by orgs with tag hierarchies. Specifying a parent tag will implicitly include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
        :param is_pto_active: A filter on the data based on power take-off being active or inactive.
        :param min_idling_duration_minutes: A filter on the data based on a minimum idling duration.
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

        request = models.GetVehicleIdlingReportsRequest(
            after=after,
            limit=limit,
            start_time=start_time,
            end_time=end_time,
            vehicle_ids=vehicle_ids,
            tag_ids=tag_ids,
            parent_tag_ids=parent_tag_ids,
            is_pto_active=is_pto_active,
            min_idling_duration_minutes=min_idling_duration_minutes,
        )

        req = self._build_request_async(
            method="GET",
            path="/fleet/reports/vehicle/idling",
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
                operation_id="getVehicleIdlingReports",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=[
                "401",
                "404",
                "405",
                "429",
                "4XX",
                "500",
                "501",
                "502",
                "503",
                "504",
                "5XX",
            ],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, models.IdlingReportsGetVehicleIdlingReportsResponseBody
            )
        if utils.match_response(http_res, "401", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsUnauthorizedErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsUnauthorizedErrorResponseBody(
                data=response_data
            )
        if utils.match_response(http_res, "404", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsNotFoundErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsNotFoundErrorResponseBody(
                data=response_data
            )
        if utils.match_response(http_res, "405", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsMethodNotAllowedErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsMethodNotAllowedErrorResponseBody(
                data=response_data
            )
        if utils.match_response(http_res, "429", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsTooManyRequestsErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsTooManyRequestsErrorResponseBody(
                data=response_data
            )
        if utils.match_response(http_res, "500", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsInternalServerErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsInternalServerErrorResponseBody(
                data=response_data
            )
        if utils.match_response(http_res, "501", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsNotImplementedErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsNotImplementedErrorResponseBody(
                data=response_data
            )
        if utils.match_response(http_res, "502", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsBadGatewayErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsBadGatewayErrorResponseBody(
                data=response_data
            )
        if utils.match_response(http_res, "503", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsServiceUnavailableErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsServiceUnavailableErrorResponseBody(
                data=response_data
            )
        if utils.match_response(http_res, "504", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsGatewayTimeoutErrorResponseBodyData,
            )
            raise models.IdlingReportsGetVehicleIdlingReportsGatewayTimeoutErrorResponseBody(
                data=response_data
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
            return utils.unmarshal_json(
                http_res.text,
                models.IdlingReportsGetVehicleIdlingReportsBadRequestErrorResponseBody,
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
