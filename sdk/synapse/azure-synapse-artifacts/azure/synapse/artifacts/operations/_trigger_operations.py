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
from ..rest import trigger as rest_trigger

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class TriggerOperations(object):
    """TriggerOperations operations.

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

    def get_triggers_by_workspace(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.TriggerListResponse"]
        """Lists triggers.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either TriggerListResponse or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.synapse.artifacts.models.TriggerListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        cls = kwargs.pop("cls", None)  # type: ClsType["_models.TriggerListResponse"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        def prepare_request(next_link=None):
            if not next_link:

                request = rest_trigger.build_get_triggers_by_workspace_request(
                    template_url=self.get_triggers_by_workspace.metadata["url"], **kwargs
                )._internal_request
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.endpoint", self._config.endpoint, "str", skip_quote=True
                    ),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:

                request = rest_trigger.build_get_triggers_by_workspace_request(
                    template_url=self.get_triggers_by_workspace.metadata["url"], **kwargs
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
            deserialized = self._deserialize("TriggerListResponse", pipeline_response)
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

    get_triggers_by_workspace.metadata = {"url": "/triggers"}  # type: ignore

    def _create_or_update_trigger_initial(
        self,
        trigger_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.TriggerResource"]
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional["_models.TriggerResource"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        properties = kwargs.pop("properties")  # type: "_models.Trigger"
        if_match = kwargs.pop("if_match", None)  # type: Optional[str]

        _trigger = _models.TriggerResource(properties=properties)
        json = self._serialize.body(_trigger, "object")

        request = rest_trigger.build_create_or_update_trigger_request_initial(
            trigger_name=trigger_name,
            if_match=if_match,
            json=json,
            content_type=content_type,
            template_url=self._create_or_update_trigger_initial.metadata["url"],
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
            deserialized = self._deserialize("TriggerResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_trigger_initial.metadata = {"url": "/triggers/{triggerName}"}  # type: ignore

    def begin_create_or_update_trigger(
        self,
        trigger_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.TriggerResource"]
        """Creates or updates a trigger.

        :param trigger_name: The trigger name.
        :type trigger_name: str
        :keyword properties: Properties of the trigger.
        :paramtype properties: ~azure.synapse.artifacts.models.Trigger
        :keyword if_match: ETag of the trigger entity.  Should only be specified for update, for which
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
        :return: An instance of LROPoller that returns either TriggerResource or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.synapse.artifacts.models.TriggerResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.TriggerResource"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_or_update_trigger_initial(
                trigger_name=trigger_name, cls=lambda x, y, z: x, **kwargs
            )

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        properties = kwargs.pop("properties")  # type: "_models.Trigger"
        if_match = kwargs.pop("if_match", None)  # type: Optional[str]

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("TriggerResource", pipeline_response)

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

    begin_create_or_update_trigger.metadata = {"url": "/triggers/{triggerName}"}  # type: ignore

    def get_trigger(
        self,
        trigger_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.TriggerResource"]
        """Gets a trigger.

        :param trigger_name: The trigger name.
        :type trigger_name: str
        :keyword if_none_match: ETag of the trigger entity. Should only be specified for get. If the
         ETag matches the existing entity tag, or if * was provided, then no content will be returned.
        :paramtype if_none_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TriggerResource, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.TriggerResource or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional["_models.TriggerResource"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        if_none_match = kwargs.pop("if_none_match", None)  # type: Optional[str]
        request = rest_trigger.build_get_trigger_request(
            trigger_name=trigger_name,
            if_none_match=if_none_match,
            template_url=self.get_trigger.metadata["url"],
            **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 304]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("TriggerResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_trigger.metadata = {"url": "/triggers/{triggerName}"}  # type: ignore

    def _delete_trigger_initial(
        self,
        trigger_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        request = rest_trigger.build_delete_trigger_request_initial(
            trigger_name=trigger_name, template_url=self._delete_trigger_initial.metadata["url"], **kwargs
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

    _delete_trigger_initial.metadata = {"url": "/triggers/{triggerName}"}  # type: ignore

    def begin_delete_trigger(
        self,
        trigger_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """Deletes a trigger.

        :param trigger_name: The trigger name.
        :type trigger_name: str
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
            raw_result = self._delete_trigger_initial(trigger_name=trigger_name, cls=lambda x, y, z: x, **kwargs)

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

    begin_delete_trigger.metadata = {"url": "/triggers/{triggerName}"}  # type: ignore

    def _subscribe_trigger_to_events_initial(
        self,
        trigger_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.TriggerSubscriptionOperationStatus"]
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional["_models.TriggerSubscriptionOperationStatus"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        request = rest_trigger.build_subscribe_trigger_to_events_request_initial(
            trigger_name=trigger_name, template_url=self._subscribe_trigger_to_events_initial.metadata["url"], **kwargs
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
            deserialized = self._deserialize("TriggerSubscriptionOperationStatus", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _subscribe_trigger_to_events_initial.metadata = {"url": "/triggers/{triggerName}/subscribeToEvents"}  # type: ignore

    def begin_subscribe_trigger_to_events(
        self,
        trigger_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.TriggerSubscriptionOperationStatus"]
        """Subscribe event trigger to events.

        :param trigger_name: The trigger name.
        :type trigger_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either TriggerSubscriptionOperationStatus or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.synapse.artifacts.models.TriggerSubscriptionOperationStatus]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.TriggerSubscriptionOperationStatus"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._subscribe_trigger_to_events_initial(
                trigger_name=trigger_name, cls=lambda x, y, z: x, **kwargs
            )

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("TriggerSubscriptionOperationStatus", pipeline_response)

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

    begin_subscribe_trigger_to_events.metadata = {"url": "/triggers/{triggerName}/subscribeToEvents"}  # type: ignore

    def get_event_subscription_status(
        self,
        trigger_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.TriggerSubscriptionOperationStatus"
        """Get a trigger's event subscription status.

        :param trigger_name: The trigger name.
        :type trigger_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TriggerSubscriptionOperationStatus, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.TriggerSubscriptionOperationStatus
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.TriggerSubscriptionOperationStatus"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        request = rest_trigger.build_get_event_subscription_status_request(
            trigger_name=trigger_name, template_url=self.get_event_subscription_status.metadata["url"], **kwargs
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

        deserialized = self._deserialize("TriggerSubscriptionOperationStatus", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_event_subscription_status.metadata = {"url": "/triggers/{triggerName}/getEventSubscriptionStatus"}  # type: ignore

    def _unsubscribe_trigger_from_events_initial(
        self,
        trigger_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.TriggerSubscriptionOperationStatus"]
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional["_models.TriggerSubscriptionOperationStatus"]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        request = rest_trigger.build_unsubscribe_trigger_from_events_request_initial(
            trigger_name=trigger_name,
            template_url=self._unsubscribe_trigger_from_events_initial.metadata["url"],
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
            deserialized = self._deserialize("TriggerSubscriptionOperationStatus", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _unsubscribe_trigger_from_events_initial.metadata = {"url": "/triggers/{triggerName}/unsubscribeFromEvents"}  # type: ignore

    def begin_unsubscribe_trigger_from_events(
        self,
        trigger_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.TriggerSubscriptionOperationStatus"]
        """Unsubscribe event trigger from events.

        :param trigger_name: The trigger name.
        :type trigger_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either TriggerSubscriptionOperationStatus or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.synapse.artifacts.models.TriggerSubscriptionOperationStatus]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        polling = kwargs.pop("polling", True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.TriggerSubscriptionOperationStatus"]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._unsubscribe_trigger_from_events_initial(
                trigger_name=trigger_name, cls=lambda x, y, z: x, **kwargs
            )

        kwargs.pop("error_map", None)
        kwargs.pop("content_type", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize("TriggerSubscriptionOperationStatus", pipeline_response)

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

    begin_unsubscribe_trigger_from_events.metadata = {"url": "/triggers/{triggerName}/unsubscribeFromEvents"}  # type: ignore

    def _start_trigger_initial(
        self,
        trigger_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        request = rest_trigger.build_start_trigger_request_initial(
            trigger_name=trigger_name, template_url=self._start_trigger_initial.metadata["url"], **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    _start_trigger_initial.metadata = {"url": "/triggers/{triggerName}/start"}  # type: ignore

    def begin_start_trigger(
        self,
        trigger_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """Starts a trigger.

        :param trigger_name: The trigger name.
        :type trigger_name: str
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
            raw_result = self._start_trigger_initial(trigger_name=trigger_name, cls=lambda x, y, z: x, **kwargs)

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

    begin_start_trigger.metadata = {"url": "/triggers/{triggerName}/start"}  # type: ignore

    def _stop_trigger_initial(
        self,
        trigger_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        request = rest_trigger.build_stop_trigger_request_initial(
            trigger_name=trigger_name, template_url=self._stop_trigger_initial.metadata["url"], **kwargs
        )._internal_request
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    _stop_trigger_initial.metadata = {"url": "/triggers/{triggerName}/stop"}  # type: ignore

    def begin_stop_trigger(
        self,
        trigger_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """Stops a trigger.

        :param trigger_name: The trigger name.
        :type trigger_name: str
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
            raw_result = self._stop_trigger_initial(trigger_name=trigger_name, cls=lambda x, y, z: x, **kwargs)

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

    begin_stop_trigger.metadata = {"url": "/triggers/{triggerName}/stop"}  # type: ignore
