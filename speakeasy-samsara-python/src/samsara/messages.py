"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from samsara import models, utils
from samsara._hooks import HookContext
from samsara.types import OptionalNullable, UNSET
from samsara.utils import get_security_from_env
from typing import List, Mapping, Optional


class Messages(BaseSDK):
    def v1get_messages(
        self,
        *,
        end_ms: Optional[int] = None,
        duration_ms: Optional[int] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.V1getMessagesResponse:
        r"""Get all messages.

        <n class=\"warning\">
        <nh>
        <i class=\"fa fa-exclamation-circle\"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Get all messages.

        <b>Rate limit:</b> 75 requests/sec (learn more about rate limits <a href=\"https://developers.samsara.com/docs/rate-limits\" target=\"_blank\">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href=\"https://forms.gle/zkD4NCH7HjKb7mm69\" target=\"_blank\">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href=\"https://www.samsara.com/help\" target=\"_blank\">submit a case</a> to our support team.

        To use this endpoint, select **Read Messages** under the Driver Workflow category when creating or editing an API token. <a href=\"https://developers.samsara.com/docs/authentication#scopes-for-api-tokens\" target=\"_blank\">Learn More.</a>

        :param end_ms: Time in unix milliseconds that represents the end of time range of messages to return. Used in combination with durationMs. Defaults to now.
        :param duration_ms: Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours.
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

        request = models.V1getMessagesRequest(
            end_ms=end_ms,
            duration_ms=duration_ms,
        )

        req = self._build_request(
            method="GET",
            path="/v1/fleet/messages",
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
                operation_id="V1getMessages",
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
            return utils.unmarshal_json(http_res.text, models.InlineResponse2005)
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

    async def v1get_messages_async(
        self,
        *,
        end_ms: Optional[int] = None,
        duration_ms: Optional[int] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.V1getMessagesResponse:
        r"""Get all messages.

        <n class=\"warning\">
        <nh>
        <i class=\"fa fa-exclamation-circle\"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Get all messages.

        <b>Rate limit:</b> 75 requests/sec (learn more about rate limits <a href=\"https://developers.samsara.com/docs/rate-limits\" target=\"_blank\">here</a>).

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href=\"https://forms.gle/zkD4NCH7HjKb7mm69\" target=\"_blank\">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href=\"https://www.samsara.com/help\" target=\"_blank\">submit a case</a> to our support team.

        To use this endpoint, select **Read Messages** under the Driver Workflow category when creating or editing an API token. <a href=\"https://developers.samsara.com/docs/authentication#scopes-for-api-tokens\" target=\"_blank\">Learn More.</a>

        :param end_ms: Time in unix milliseconds that represents the end of time range of messages to return. Used in combination with durationMs. Defaults to now.
        :param duration_ms: Time in milliseconds that represents the duration before endMs to query. Defaults to 24 hours.
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

        request = models.V1getMessagesRequest(
            end_ms=end_ms,
            duration_ms=duration_ms,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/fleet/messages",
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
                operation_id="V1getMessages",
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
            return utils.unmarshal_json(http_res.text, models.InlineResponse2005)
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

    def v1create_messages(
        self,
        *,
        driver_ids: List[float],
        text: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.V1createMessagesResponse:
        r"""Send a message to a list of driver ids.

        <n class=\"warning\">
        <nh>
        <i class=\"fa fa-exclamation-circle\"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Send a message to a list of driver ids.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href=\"https://forms.gle/zkD4NCH7HjKb7mm69\" target=\"_blank\">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href=\"https://www.samsara.com/help\" target=\"_blank\">submit a case</a> to our support team.

        To use this endpoint, select **Write Messages** under the Driver Workflow category when creating or editing an API token. <a href=\"https://developers.samsara.com/docs/authentication#scopes-for-api-tokens\" target=\"_blank\">Learn More.</a>

        :param driver_ids: IDs of the drivers for whom the messages are sent to.
        :param text: The text sent in the message. Max 2500 characters allowed.
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

        request = models.InlineObject2(
            driver_ids=driver_ids,
            text=text,
        )

        req = self._build_request(
            method="POST",
            path="/v1/fleet/messages",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.InlineObject2
            ),
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
                operation_id="V1createMessages",
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
            return utils.unmarshal_json(http_res.text, models.InlineResponse2006)
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

    async def v1create_messages_async(
        self,
        *,
        driver_ids: List[float],
        text: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.V1createMessagesResponse:
        r"""Send a message to a list of driver ids.

        <n class=\"warning\">
        <nh>
        <i class=\"fa fa-exclamation-circle\"></i>
        This endpoint is still on our legacy API.
        </nh>
        </n>

        Send a message to a list of driver ids.

        **Submit Feedback**: Likes, dislikes, and API feature requests should be filed as feedback in our <a href=\"https://forms.gle/zkD4NCH7HjKb7mm69\" target=\"_blank\">API feedback form</a>. If you encountered an issue or noticed inaccuracies in the API documentation, please <a href=\"https://www.samsara.com/help\" target=\"_blank\">submit a case</a> to our support team.

        To use this endpoint, select **Write Messages** under the Driver Workflow category when creating or editing an API token. <a href=\"https://developers.samsara.com/docs/authentication#scopes-for-api-tokens\" target=\"_blank\">Learn More.</a>

        :param driver_ids: IDs of the drivers for whom the messages are sent to.
        :param text: The text sent in the message. Max 2500 characters allowed.
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

        request = models.InlineObject2(
            driver_ids=driver_ids,
            text=text,
        )

        req = self._build_request_async(
            method="POST",
            path="/v1/fleet/messages",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.InlineObject2
            ),
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
                operation_id="V1createMessages",
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
            return utils.unmarshal_json(http_res.text, models.InlineResponse2006)
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
