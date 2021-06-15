# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.polling.base_polling import LROBasePolling
from azure.synapse.artifacts.core.rest import HttpRequest

from .. import models as _models
from ..rest import data_flow as rest_data_flow

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class DataFlowOperations(object):
    """DataFlowOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.synapse.artifacts.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def _create_or_update_data_flow_initial(
        self,
        data_flow_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.DataFlowResource"]
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional["_models.DataFlowResource"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        properties = kwargs.pop("properties")  # type: "_models.DataFlow"
        if_match = kwargs.pop("if_match", None)  # type: Optional[str]

        _data_flow = _models.DataFlowResource(properties=properties)
        json = self._serialize.body(_data_flow, "object")

        request = rest_data_flow.build_create_or_update_data_flow_request_initial(
            data_flow_name=data_flow_name,
            if_match=if_match,
            json=json,
            content_type=content_type,
            template_url=self._create_or_update_data_flow_initial.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("DataFlowResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_data_flow_initial.metadata = {"url": "/dataflows/{dataFlowName}"}  # type: ignore

    def begin_create_or_update_data_flow(
        self,
        data_flow_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.DataFlowResource"]
        """Creates or updates a data flow.

        :param data_flow_name: The data flow name.
        :type data_flow_name: str
        :keyword properties: Data flow properties.
        :paramtype properties: ~azure.synapse.artifacts.models.DataFlow
        :keyword if_match: ETag of the data flow entity. Should only be specified for update, for which
         it should match existing entity or can be * for unconditional update.
        :paramtype if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either DataFlowResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.synapse.artifacts.models.DataFlowResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DataFlowResource"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_or_update_data_flow_initial(
                data_flow_name=data_flow_name, cls=lambda x, y, z: x, **kwargs
            )

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        properties = kwargs.pop("properties")  # type: "_models.DataFlow"
        if_match = kwargs.pop("if_match", None)  # type: Optional[str]

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("DataFlowResource", pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        if polling is True:
            polling_method = LROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False:
            polling_method = NoPolling()
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create_or_update_data_flow.metadata = {"url": "/dataflows/{dataFlowName}"}  # type: ignore

    def get_data_flow(
        self,
        data_flow_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DataFlowResource"
        """Gets a data flow.

        :param data_flow_name: The data flow name.
        :type data_flow_name: str
        :keyword if_none_match: ETag of the data flow entity. Should only be specified for get. If the
         ETag matches the existing entity tag, or if * was provided, then no content will be returned.
        :paramtype if_none_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataFlowResource, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.DataFlowResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DataFlowResource"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        if_none_match = kwargs.pop("if_none_match", None)  # type: Optional[str]
        request = rest_data_flow.build_get_data_flow_request(
            data_flow_name=data_flow_name,
            if_none_match=if_none_match,
            template_url=self.get_data_flow.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("DataFlowResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_data_flow.metadata = {"url": "/dataflows/{dataFlowName}"}  # type: ignore

    def _delete_data_flow_initial(
        self,
        data_flow_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        request = rest_data_flow.build_delete_data_flow_request_initial(
            data_flow_name=data_flow_name, template_url=self._delete_data_flow_initial.metadata["url"], **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_data_flow_initial.metadata = {"url": "/dataflows/{dataFlowName}"}  # type: ignore

    def begin_delete_data_flow(
        self,
        data_flow_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """Deletes a data flow.

        :param data_flow_name: The data flow name.
        :type data_flow_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._delete_data_flow_initial(data_flow_name=data_flow_name, cls=lambda x, y, z: x, **kwargs)

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            if cls:
                return cls(pipeline_response, None, {})

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        if polling is True:
            polling_method = LROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False:
            polling_method = NoPolling()
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete_data_flow.metadata = {"url": "/dataflows/{dataFlowName}"}  # type: ignore

    def _rename_data_flow_initial(
        self,
        data_flow_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        new_name = kwargs.pop("new_name", None)  # type: Optional[str]

        _request = _models.ArtifactRenameRequest(new_name=new_name)
        json = self._serialize.body(_request, "object")

        request = rest_data_flow.build_rename_data_flow_request_initial(
            data_flow_name=data_flow_name,
            json=json,
            content_type=content_type,
            template_url=self._rename_data_flow_initial.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    _rename_data_flow_initial.metadata = {"url": "/dataflows/{dataFlowName}/rename"}  # type: ignore

    def begin_rename_data_flow(
        self,
        data_flow_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """Renames a dataflow.

        :param data_flow_name: The data flow name.
        :type data_flow_name: str
        :keyword new_name: New name of the artifact.
        :paramtype new_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._rename_data_flow_initial(data_flow_name=data_flow_name, cls=lambda x, y, z: x, **kwargs)

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        new_name = kwargs.pop("new_name", None)  # type: Optional[str]

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            if cls:
                return cls(pipeline_response, None, {})

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        if polling is True:
            polling_method = LROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False:
            polling_method = NoPolling()
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_rename_data_flow.metadata = {"url": "/dataflows/{dataFlowName}/rename"}  # type: ignore

    def get_data_flows_by_workspace(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.DataFlowListResponse"]
        """Lists data flows.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DataFlowListResponse or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.synapse.artifacts.models.DataFlowListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        cls = kwargs.pop("cls", None)  # type: ClsType["_models.DataFlowListResponse"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = rest_data_flow.build_get_data_flows_by_workspace_request(
                    template_url=self.get_data_flows_by_workspace.metadata["url"], **kwargs
                )._internal_request
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:

                request = rest_data_flow.build_get_data_flows_by_workspace_request(
                    template_url=self.get_data_flows_by_workspace.metadata["url"], **kwargs
                )._internal_request
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

                # little hacky, but this code will soon be replaced with code that won't need the hack
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.method = "GET"
                request.url = self._client.format_url(next_link, **path_format_arguments)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("DataFlowListResponse", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    get_data_flows_by_workspace.metadata = {"url": "/dataflows"}  # type: ignore
