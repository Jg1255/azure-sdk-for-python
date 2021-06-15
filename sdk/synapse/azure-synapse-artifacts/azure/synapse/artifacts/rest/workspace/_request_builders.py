# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.pipeline.transport._base import _format_url_section
from azure.synapse.artifacts.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, IO, Optional

_SERIALIZER = Serializer()


def build_get_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Get Workspace.

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
                "adlaResourceId": "str (optional)",
                "connectivityEndpoints": {
                    "str": "str (optional)"
                },
                "defaultDataLakeStorage": {
                    "accountUrl": "str (optional)",
                    "filesystem": "str (optional)"
                },
                "encryption": {
                    "cmk": {
                        "key": {
                            "keyVaultUrl": "str (optional)",
                            "name": "str (optional)"
                        },
                        "status": "str (optional)"
                    },
                    "doubleEncryptionEnabled": "bool (optional)"
                },
                "extraProperties": {
                    "str": "object (optional)"
                },
                "id": "str (optional)",
                "identity": {
                    "principalId": "str (optional)",
                    "tenantId": "str (optional)",
                    "type": "str (optional)"
                },
                "location": "str",
                "managedResourceGroupName": "str (optional)",
                "managedVirtualNetwork": "str (optional)",
                "managedVirtualNetworkSettings": {
                    "allowedAadTenantIdsForLinking": [
                        "str (optional)"
                    ],
                    "linkedAccessCheckOnTargetResource": "bool (optional)",
                    "preventDataExfiltration": "bool (optional)"
                },
                "name": "str (optional)",
                "privateEndpointConnections": [
                    {
                        "id": "str (optional)",
                        "name": "str (optional)",
                        "privateEndpoint": {
                            "id": "str (optional)"
                        },
                        "privateLinkServiceConnectionState": {
                            "actionsRequired": "str (optional)",
                            "description": "str (optional)",
                            "status": "str (optional)"
                        },
                        "provisioningState": "str (optional)",
                        "type": "str (optional)"
                    }
                ],
                "provisioningState": "str (optional)",
                "purviewConfiguration": {
                    "purviewResourceId": "str (optional)"
                },
                "sqlAdministratorLogin": "str (optional)",
                "sqlAdministratorLoginPassword": "str (optional)",
                "tags": {
                    "str": "str (optional)"
                },
                "type": "str (optional)",
                "virtualNetworkProfile": {
                    "computeSubnetId": "str (optional)"
                },
                "workspaceRepositoryConfiguration": {
                    "accountName": "str (optional)",
                    "collaborationBranch": "str (optional)",
                    "hostName": "str (optional)",
                    "lastCommitId": "str (optional)",
                    "projectName": "str (optional)",
                    "repositoryName": "str (optional)",
                    "rootFolder": "str (optional)",
                    "tenantId": "str (optional)",
                    "type": "str (optional)"
                },
                "workspaceUID": "str (optional)"
            }
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/workspace")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)
