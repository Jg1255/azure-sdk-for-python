# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, IO, Optional

from azure.core.pipeline.transport._base import _format_url_section
from azure.synapse.artifacts.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_list_request(**kwargs: Any) -> HttpRequest:
    """List Big Data Pools.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "nextLink": "str (optional)",
                "value": [
                    {
                        "autoPause": {
                            "delayInMinutes": "int (optional)",
                            "enabled": "bool (optional)"
                        },
                        "autoScale": {
                            "enabled": "bool (optional)",
                            "maxNodeCount": "int (optional)",
                            "minNodeCount": "int (optional)"
                        },
                        "cacheSize": "int (optional)",
                        "creationDate": "datetime (optional)",
                        "customLibraries": [
                            {
                                "containerName": "str (optional)",
                                "creatorId": "str (optional)",
                                "name": "str (optional)",
                                "path": "str (optional)",
                                "provisioningStatus": "str (optional)",
                                "type": "str (optional)",
                                "uploadedTimestamp": "datetime (optional)"
                            }
                        ],
                        "defaultSparkLogFolder": "str (optional)",
                        "dynamicExecutorAllocation": {
                            "enabled": "bool (optional)"
                        },
                        "id": "str (optional)",
                        "isComputeIsolationEnabled": "bool (optional)",
                        "lastSucceededTimestamp": "datetime (optional)",
                        "libraryRequirements": {
                            "content": "str (optional)",
                            "filename": "str (optional)",
                            "time": "datetime (optional)"
                        },
                        "location": "str",
                        "name": "str (optional)",
                        "nodeCount": "int (optional)",
                        "nodeSize": "str (optional)",
                        "nodeSizeFamily": "str (optional)",
                        "provisioningState": "str (optional)",
                        "sessionLevelPackagesEnabled": "bool (optional)",
                        "sparkConfigProperties": {
                            "content": "str (optional)",
                            "filename": "str (optional)",
                            "time": "datetime (optional)"
                        },
                        "sparkEventsFolder": "str (optional)",
                        "sparkVersion": "str (optional)",
                        "tags": {
                            "str": "str (optional)"
                        },
                        "type": "str (optional)"
                    }
                ]
            }
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/bigDataPools")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_get_request(big_data_pool_name: str, **kwargs: Any) -> HttpRequest:
    """Get Big Data Pool.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param big_data_pool_name: The Big Data Pool name.
    :type big_data_pool_name: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "autoPause": {
                    "delayInMinutes": "int (optional)",
                    "enabled": "bool (optional)"
                },
                "autoScale": {
                    "enabled": "bool (optional)",
                    "maxNodeCount": "int (optional)",
                    "minNodeCount": "int (optional)"
                },
                "cacheSize": "int (optional)",
                "creationDate": "datetime (optional)",
                "customLibraries": [
                    {
                        "containerName": "str (optional)",
                        "creatorId": "str (optional)",
                        "name": "str (optional)",
                        "path": "str (optional)",
                        "provisioningStatus": "str (optional)",
                        "type": "str (optional)",
                        "uploadedTimestamp": "datetime (optional)"
                    }
                ],
                "defaultSparkLogFolder": "str (optional)",
                "dynamicExecutorAllocation": {
                    "enabled": "bool (optional)"
                },
                "id": "str (optional)",
                "isComputeIsolationEnabled": "bool (optional)",
                "lastSucceededTimestamp": "datetime (optional)",
                "libraryRequirements": {
                    "content": "str (optional)",
                    "filename": "str (optional)",
                    "time": "datetime (optional)"
                },
                "location": "str",
                "name": "str (optional)",
                "nodeCount": "int (optional)",
                "nodeSize": "str (optional)",
                "nodeSizeFamily": "str (optional)",
                "provisioningState": "str (optional)",
                "sessionLevelPackagesEnabled": "bool (optional)",
                "sparkConfigProperties": {
                    "content": "str (optional)",
                    "filename": "str (optional)",
                    "time": "datetime (optional)"
                },
                "sparkEventsFolder": "str (optional)",
                "sparkVersion": "str (optional)",
                "tags": {
                    "str": "str (optional)"
                },
                "type": "str (optional)"
            }
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/bigDataPools/{bigDataPoolName}")
    path_format_arguments = {
        "bigDataPoolName": _SERIALIZER.url("big_data_pool_name", big_data_pool_name, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)
