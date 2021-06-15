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


def build_get_datasets_by_workspace_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Lists datasets.

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
                        "etag": "str (optional)",
                        "id": "str (optional)",
                        "name": "str (optional)",
                        "properties": "properties",
                        "type": "str (optional)"
                    }
                ]
            }
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/datasets")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_create_or_update_dataset_request_initial(
    dataset_name,  # type: str
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Creates or updates a dataset.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param dataset_name: The dataset name.
    :type dataset_name: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Dataset resource definition.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Dataset resource definition.
    :paramtype content: Any
    :keyword if_match: ETag of the dataset entity.  Should only be specified for update, for which
     it should match existing entity or can be * for unconditional update.
    :paramtype if_match: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            properties = {
                "": {
                    "str": "object (optional)"
                },
                "annotations": [
                    "object (optional)"
                ],
                "description": "str (optional)",
                "folder": {
                    "name": "str (optional)"
                },
                "linkedServiceName": {
                    "parameters": {
                        "str": "object (optional)"
                    },
                    "referenceName": "str",
                    "type": "str"
                },
                "parameters": {
                    "str": {
                        "defaultValue": "object (optional)",
                        "type": "str"
                    }
                },
                "schema": "object (optional)",
                "structure": "object (optional)",
                "tableName": "object (optional)",
                "type": "AmazonMWSObject"
            }
            # OR
            properties = {
                "": {
                    "str": "object (optional)"
                },
                "annotations": [
                    "object (optional)"
                ],
                "description": "str (optional)",
                "folder": {
                    "name": "str (optional)"
                },
                "linkedServiceName": {
                    "parameters": {
                        "str": "object (optional)"
                    },
                    "referenceName": "str",
                    "type": "str"
                },
                "parameters": {
                    "str": {
                        "defaultValue": "object (optional)",
                        "type": "str"
                    }
                },
                "schema": "object (optional)",
                "structure": "object (optional)",
                "table": "object (optional)",
                "tableName": "object (optional)",
                "type": "AmazonRedshiftTable"
            }
            # OR
            properties = {
                "": {
                    "str": "object (optional)"
                },
                "annotations": [
                    "object (optional)"
                ],
                "bucketName": "object",
                "compression": "compression",
                "description": "str (optional)",
                "folder": {
                    "name": "str (optional)"
                },
                "format": "format",
                "key": "object (optional)",
                "linkedServiceName": {
                    "parameters": {
                        "str": "object (optional)"
                    },
                    "referenceName": "str",
                    "type": "str"
                },
                "modifiedDatetimeEnd": "object (optional)",
                "modifiedDatetimeStart": "object (optional)",
                "parameters": {
                    "str": {
                        "defaultValue": "object (optional)",
                        "type": "str"
                    }
                },
                "prefix": "object (optional)",
                "schema": "object (optional)",
                "structure": "object (optional)",
                "type": "AmazonS3Object",
                "version": "object (optional)"
            }
            # OR
            properties = {
                "": {
                    "str": "object (optional)"
                },
                "annotations": [
                    "object (optional)"
                ],
                "avroCompressionCodec": "object (optional)",
                "avroCompressionLevel": "int (optional)",
                "description": "str (optional)",
                "folder": {
                    "name": "str (optional)"
                },
                "linkedServiceName": {
                    "parameters": {
                        "str": "object (optional)"
                    },
                    "referenceName": "str",
                    "type": "str"
                },
                "location": "location",
                "parameters": {
                    "str": {
                        "defaultValue": "object (optional)",
                        "type": "str"
                    }
                },
                "schema": "object (optional)",
                "structure": "object (optional)",
                "type": "Avro"
            }
            # OR
            properties = {
                "": {
                    "str": "object (optional)"
                },
                "annotations": [
                    "object (optional)"
                ],
                "compression": "compression",
                "description": "str (optional)",
                "fileName": "object (optional)",
                "folder": {
                    "name": "str (optional)"
                },
                "folderPath": "object (optional)",
                "format": "format",
                "linkedServiceName": {
                    "parameters": {
                        "str": "object (optional)"
                    },
                    "referenceName": "str",
                    "type": "str"
                },
                "modifiedDatetimeEnd": "object (optional)",
                "modifiedDatetimeStart": "object (optional)",
                "parameters": {
                    "str": {
                        "defaultValue": "object (optional)",
                        "type": "str"
                    }
                },
                "schema": "object (optional)",
                "structure": "object (optional)",
                "tableRootLocation": "object (optional)",
                "type": "AzureBlob"
            }

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "etag": "str (optional)",
                "id": "str (optional)",
                "name": "str (optional)",
                "properties": "properties",
                "type": "str (optional)"
            }

            # response body for status code(s): 200
            response.json() == {
                "etag": "str (optional)",
                "id": "str (optional)",
                "name": "str (optional)",
                "properties": "properties",
                "type": "str (optional)"
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]
    json = kwargs.pop("json", None)  # type: Any
    if_match = kwargs.pop("if_match", None)  # type: Optional[str]
    if_match = kwargs.pop("if_match", None)  # type: Optional[str]

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/datasets/{datasetName}")
    path_format_arguments = {
        "datasetName": _SERIALIZER.url(
            "dataset_name",
            dataset_name,
            "str",
            max_length=260,
            min_length=1,
            pattern=r"^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$",
        ),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if if_match is not None:
        header_parameters["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_get_dataset_request(
    dataset_name,  # type: str
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Gets a dataset.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param dataset_name: The dataset name.
    :type dataset_name: str
    :keyword if_none_match: ETag of the dataset entity. Should only be specified for get. If the
     ETag matches the existing entity tag, or if * was provided, then no content will be returned.
    :paramtype if_none_match: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200
            response.json() == {
                "etag": "str (optional)",
                "id": "str (optional)",
                "name": "str (optional)",
                "properties": "properties",
                "type": "str (optional)"
            }
    """

    if_none_match = kwargs.pop("if_none_match", None)  # type: Optional[str]
    if_none_match = kwargs.pop("if_none_match", None)  # type: Optional[str]

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/datasets/{datasetName}")
    path_format_arguments = {
        "datasetName": _SERIALIZER.url(
            "dataset_name",
            dataset_name,
            "str",
            max_length=260,
            min_length=1,
            pattern=r"^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$",
        ),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if if_none_match is not None:
        header_parameters["If-None-Match"] = _SERIALIZER.header("if_none_match", if_none_match, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_delete_dataset_request_initial(
    dataset_name,  # type: str
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Deletes a dataset.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param dataset_name: The dataset name.
    :type dataset_name: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/datasets/{datasetName}")
    path_format_arguments = {
        "datasetName": _SERIALIZER.url(
            "dataset_name",
            dataset_name,
            "str",
            max_length=260,
            min_length=1,
            pattern=r"^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$",
        ),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_rename_dataset_request_initial(
    dataset_name,  # type: str
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    """Renames a dataset.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your
    code flow.

    :param dataset_name: The dataset name.
    :type dataset_name: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. proposed new name.
    :paramtype json: Any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). proposed new name.
    :paramtype content: Any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "newName": "str (optional)"
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]
    json = kwargs.pop("json", None)  # type: Any

    api_version = "2020-12-01"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/datasets/{datasetName}/rename")
    path_format_arguments = {
        "datasetName": _SERIALIZER.url(
            "dataset_name",
            dataset_name,
            "str",
            max_length=260,
            min_length=1,
            pattern=r"^[A-Za-z0-9_][^<>*#.%&:\\+?/]*$",
        ),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, params=query_parameters, headers=header_parameters, **kwargs)
