# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, List, Optional

from azure.core.pipeline.transport._base import _format_url_section
from azure.synapse.accesscontrol.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_list_role_definitions_request(
    *,
    is_built_in: Optional[bool] = None,
    scope: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """List role definitions.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :keyword is_built_in: Is a Synapse Built-In Role or not.
    :paramtype is_built_in: bool
    :keyword scope: Scope of the Synapse Built-in Role.
    :paramtype scope: str
    :return: Returns an :class:`~azure.synapse.accesscontrol.core.rest.HttpRequest` that you will
     pass to the client's `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart
     for how to incorporate this response into your code flow.
    :rtype: ~azure.synapse.accesscontrol.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == [
                {
                    "availabilityStatus": "str (optional)",
                    "description": "str (optional)",
                    "id": "str (optional)",
                    "isBuiltIn": "bool (optional)",
                    "name": "str (optional)",
                    "permissions": [
                        {
                            "actions": [
                                "str (optional)"
                            ],
                            "dataActions": [
                                "str (optional)"
                            ],
                            "notActions": [
                                "str (optional)"
                            ],
                            "notDataActions": [
                                "str (optional)"
                            ]
                        }
                    ],
                    "scopes": [
                        "str (optional)"
                    ]
                }
            ]
    """


    api_version = "2020-08-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop("template_url", '/roleDefinitions')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if is_built_in is not None:
        query_parameters['isBuiltIn'] = _SERIALIZER.query("is_built_in", is_built_in, 'bool')
    if scope is not None:
        query_parameters['scope'] = _SERIALIZER.query("scope", scope, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_role_definition_by_id_request(
    role_definition_id: str,
    **kwargs: Any
) -> HttpRequest:
    """Get role definition by role definition Id.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param role_definition_id: Synapse Built-In Role Definition Id.
    :type role_definition_id: str
    :return: Returns an :class:`~azure.synapse.accesscontrol.core.rest.HttpRequest` that you will
     pass to the client's `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart
     for how to incorporate this response into your code flow.
    :rtype: ~azure.synapse.accesscontrol.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "availabilityStatus": "str (optional)",
                "description": "str (optional)",
                "id": "str (optional)",
                "isBuiltIn": "bool (optional)",
                "name": "str (optional)",
                "permissions": [
                    {
                        "actions": [
                            "str (optional)"
                        ],
                        "dataActions": [
                            "str (optional)"
                        ],
                        "notActions": [
                            "str (optional)"
                        ],
                        "notDataActions": [
                            "str (optional)"
                        ]
                    }
                ],
                "scopes": [
                    "str (optional)"
                ]
            }
    """


    api_version = "2020-08-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop("template_url", '/roleDefinitions/{roleDefinitionId}')
    path_format_arguments = {
        'roleDefinitionId': _SERIALIZER.url("role_definition_id", role_definition_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_scopes_request(
    **kwargs: Any
) -> HttpRequest:
    """List rbac scopes.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.synapse.accesscontrol.core.rest.HttpRequest` that you will
     pass to the client's `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart
     for how to incorporate this response into your code flow.
    :rtype: ~azure.synapse.accesscontrol.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == [
                "str (optional)"
            ]
    """


    api_version = "2020-08-01-preview"
    accept = "application/json, text/json"

    # Construct URL
    url = kwargs.pop("template_url", '/rbacScopes')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

