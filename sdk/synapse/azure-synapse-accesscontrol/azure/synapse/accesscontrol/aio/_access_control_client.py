# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.synapse.accesscontrol.core.rest import AsyncHttpResponse, HttpRequest
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict

    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import AccessControlClientConfiguration


class AccessControlClient(object):
    """AccessControlClient.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param endpoint: The workspace development endpoint, for example https://myworkspace.dev.azuresynapse.net.
    :type endpoint: str
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        endpoint: str,
        **kwargs: Any
    ) -> None:
        base_url = '{endpoint}'
        self._config = AccessControlClientConfiguration(credential, endpoint, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False

    async def send_request(self, request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `azure.synapse.accesscontrol.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:

        >>> from azure.synapse.accesscontrol.rest import build_check_principal_access_request
        >>> request = build_check_principal_access_request(json, content)
        <HttpRequest [POST], url: '/checkAccessSynapseRbac'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        For advanced cases, you can also create your own :class:`~azure.synapse.accesscontrol.core.rest.HttpRequest`
        and pass it in.

        :param request: The network request you want to make. Required.
        :type request: ~azure.synapse.accesscontrol.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.synapse.accesscontrol.core.rest.AsyncHttpResponse
        """
        request_copy = deepcopy(request)
        path_format_arguments = {
            'endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AccessControlClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
