# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, AsyncIterable, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class PlantingDataOperations:
    """PlantingDataOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.agrifood.farming.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_farmer_id(
        self,
        farmer_id: str,
        min_avg_planting_rate: Optional[float] = None,
        max_avg_planting_rate: Optional[float] = None,
        min_total_material: Optional[float] = None,
        max_total_material: Optional[float] = None,
        min_avg_material: Optional[float] = None,
        max_avg_material: Optional[float] = None,
        sources: Optional[List[str]] = None,
        associated_boundary_ids: Optional[List[str]] = None,
        operation_boundary_ids: Optional[List[str]] = None,
        min_operation_start_date_time: Optional[datetime.datetime] = None,
        max_operation_start_date_time: Optional[datetime.datetime] = None,
        min_operation_end_date_time: Optional[datetime.datetime] = None,
        max_operation_end_date_time: Optional[datetime.datetime] = None,
        min_operation_modified_date_time: Optional[datetime.datetime] = None,
        max_operation_modified_date_time: Optional[datetime.datetime] = None,
        min_area: Optional[float] = None,
        max_area: Optional[float] = None,
        ids: Optional[List[str]] = None,
        names: Optional[List[str]] = None,
        property_filters: Optional[List[str]] = None,
        statuses: Optional[List[str]] = None,
        min_created_date_time: Optional[datetime.datetime] = None,
        max_created_date_time: Optional[datetime.datetime] = None,
        min_last_modified_date_time: Optional[datetime.datetime] = None,
        max_last_modified_date_time: Optional[datetime.datetime] = None,
        max_page_size: Optional[int] = 50,
        skip_token: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PlantingDataListResponse"]:
        """Returns a paginated list of planting data resources under a particular farm.

        :param farmer_id: ID of the associated farmer.
        :type farmer_id: str
        :param min_avg_planting_rate: Minimum AvgPlantingRate value(inclusive).
        :type min_avg_planting_rate: float
        :param max_avg_planting_rate: Maximum AvgPlantingRate value (inclusive).
        :type max_avg_planting_rate: float
        :param min_total_material: Minimum TotalMaterial value(inclusive).
        :type min_total_material: float
        :param max_total_material: Maximum TotalMaterial value (inclusive).
        :type max_total_material: float
        :param min_avg_material: Minimum AvgMaterial value(inclusive).
        :type min_avg_material: float
        :param max_avg_material: Maximum AvgMaterial value (inclusive).
        :type max_avg_material: float
        :param sources: Sources of the operation data.
        :type sources: list[str]
        :param associated_boundary_ids: Boundary IDs associated with operation data.
        :type associated_boundary_ids: list[str]
        :param operation_boundary_ids: Operation boundary IDs associated with operation data.
        :type operation_boundary_ids: list[str]
        :param min_operation_start_date_time: Minimum start date-time of the operation data, sample
         format: yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type min_operation_start_date_time: ~datetime.datetime
        :param max_operation_start_date_time: Maximum start date-time of the operation data, sample
         format: yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type max_operation_start_date_time: ~datetime.datetime
        :param min_operation_end_date_time: Minimum end date-time of the operation data, sample format:
         yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type min_operation_end_date_time: ~datetime.datetime
        :param max_operation_end_date_time: Maximum end date-time of the operation data, sample format:
         yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type max_operation_end_date_time: ~datetime.datetime
        :param min_operation_modified_date_time: Minimum modified date-time of the operation data,
         sample format: yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type min_operation_modified_date_time: ~datetime.datetime
        :param max_operation_modified_date_time: Maximum modified date-time of the operation data,
         sample format: yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type max_operation_modified_date_time: ~datetime.datetime
        :param min_area: Minimum area for which operation was applied (inclusive).
        :type min_area: float
        :param max_area: Maximum area for which operation was applied (inclusive).
        :type max_area: float
        :param ids: Ids of the resource.
        :type ids: list[str]
        :param names: Names of the resource.
        :type names: list[str]
        :param property_filters: Filters on key-value pairs within the Properties object.
         eg. "{testKey} eq {testValue}".
        :type property_filters: list[str]
        :param statuses: Statuses of the resource.
        :type statuses: list[str]
        :param min_created_date_time: Minimum creation date of resource (inclusive).
        :type min_created_date_time: ~datetime.datetime
        :param max_created_date_time: Maximum creation date of resource (inclusive).
        :type max_created_date_time: ~datetime.datetime
        :param min_last_modified_date_time: Minimum last modified date of resource (inclusive).
        :type min_last_modified_date_time: ~datetime.datetime
        :param max_last_modified_date_time: Maximum last modified date of resource (inclusive).
        :type max_last_modified_date_time: ~datetime.datetime
        :param max_page_size: Maximum number of items needed (inclusive).
         Minimum = 10, Maximum = 1000, Default value = 50.
        :type max_page_size: int
        :param skip_token: Skip token for getting next set of results.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PlantingDataListResponse or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.agrifood.farming.models.PlantingDataListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PlantingDataListResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-31-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_farmer_id.metadata['url']  # type: ignore
                path_format_arguments = {
                    'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                    'farmerId': self._serialize.url("farmer_id", farmer_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if min_avg_planting_rate is not None:
                    query_parameters['minAvgPlantingRate'] = self._serialize.query("min_avg_planting_rate", min_avg_planting_rate, 'float')
                if max_avg_planting_rate is not None:
                    query_parameters['maxAvgPlantingRate'] = self._serialize.query("max_avg_planting_rate", max_avg_planting_rate, 'float')
                if min_total_material is not None:
                    query_parameters['minTotalMaterial'] = self._serialize.query("min_total_material", min_total_material, 'float')
                if max_total_material is not None:
                    query_parameters['maxTotalMaterial'] = self._serialize.query("max_total_material", max_total_material, 'float')
                if min_avg_material is not None:
                    query_parameters['minAvgMaterial'] = self._serialize.query("min_avg_material", min_avg_material, 'float')
                if max_avg_material is not None:
                    query_parameters['maxAvgMaterial'] = self._serialize.query("max_avg_material", max_avg_material, 'float')
                if sources is not None:
                    query_parameters['sources'] = [self._serialize.query("sources", q, 'str') if q is not None else '' for q in sources]
                if associated_boundary_ids is not None:
                    query_parameters['associatedBoundaryIds'] = [self._serialize.query("associated_boundary_ids", q, 'str') if q is not None else '' for q in associated_boundary_ids]
                if operation_boundary_ids is not None:
                    query_parameters['operationBoundaryIds'] = [self._serialize.query("operation_boundary_ids", q, 'str') if q is not None else '' for q in operation_boundary_ids]
                if min_operation_start_date_time is not None:
                    query_parameters['minOperationStartDateTime'] = self._serialize.query("min_operation_start_date_time", min_operation_start_date_time, 'iso-8601')
                if max_operation_start_date_time is not None:
                    query_parameters['maxOperationStartDateTime'] = self._serialize.query("max_operation_start_date_time", max_operation_start_date_time, 'iso-8601')
                if min_operation_end_date_time is not None:
                    query_parameters['minOperationEndDateTime'] = self._serialize.query("min_operation_end_date_time", min_operation_end_date_time, 'iso-8601')
                if max_operation_end_date_time is not None:
                    query_parameters['maxOperationEndDateTime'] = self._serialize.query("max_operation_end_date_time", max_operation_end_date_time, 'iso-8601')
                if min_operation_modified_date_time is not None:
                    query_parameters['minOperationModifiedDateTime'] = self._serialize.query("min_operation_modified_date_time", min_operation_modified_date_time, 'iso-8601')
                if max_operation_modified_date_time is not None:
                    query_parameters['maxOperationModifiedDateTime'] = self._serialize.query("max_operation_modified_date_time", max_operation_modified_date_time, 'iso-8601')
                if min_area is not None:
                    query_parameters['minArea'] = self._serialize.query("min_area", min_area, 'float')
                if max_area is not None:
                    query_parameters['maxArea'] = self._serialize.query("max_area", max_area, 'float')
                if ids is not None:
                    query_parameters['ids'] = [self._serialize.query("ids", q, 'str') if q is not None else '' for q in ids]
                if names is not None:
                    query_parameters['names'] = [self._serialize.query("names", q, 'str') if q is not None else '' for q in names]
                if property_filters is not None:
                    query_parameters['propertyFilters'] = [self._serialize.query("property_filters", q, 'str') if q is not None else '' for q in property_filters]
                if statuses is not None:
                    query_parameters['statuses'] = [self._serialize.query("statuses", q, 'str') if q is not None else '' for q in statuses]
                if min_created_date_time is not None:
                    query_parameters['minCreatedDateTime'] = self._serialize.query("min_created_date_time", min_created_date_time, 'iso-8601')
                if max_created_date_time is not None:
                    query_parameters['maxCreatedDateTime'] = self._serialize.query("max_created_date_time", max_created_date_time, 'iso-8601')
                if min_last_modified_date_time is not None:
                    query_parameters['minLastModifiedDateTime'] = self._serialize.query("min_last_modified_date_time", min_last_modified_date_time, 'iso-8601')
                if max_last_modified_date_time is not None:
                    query_parameters['maxLastModifiedDateTime'] = self._serialize.query("max_last_modified_date_time", max_last_modified_date_time, 'iso-8601')
                if max_page_size is not None:
                    query_parameters['$maxPageSize'] = self._serialize.query("max_page_size", max_page_size, 'int', maximum=1000, minimum=10)
                if skip_token is not None:
                    query_parameters['$skipToken'] = self._serialize.query("skip_token", skip_token, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                    'farmerId': self._serialize.url("farmer_id", farmer_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('PlantingDataListResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_farmer_id.metadata = {'url': '/farmers/{farmerId}/planting-data'}  # type: ignore

    def list(
        self,
        min_avg_planting_rate: Optional[float] = None,
        max_avg_planting_rate: Optional[float] = None,
        min_total_material: Optional[float] = None,
        max_total_material: Optional[float] = None,
        min_avg_material: Optional[float] = None,
        max_avg_material: Optional[float] = None,
        sources: Optional[List[str]] = None,
        associated_boundary_ids: Optional[List[str]] = None,
        operation_boundary_ids: Optional[List[str]] = None,
        min_operation_start_date_time: Optional[datetime.datetime] = None,
        max_operation_start_date_time: Optional[datetime.datetime] = None,
        min_operation_end_date_time: Optional[datetime.datetime] = None,
        max_operation_end_date_time: Optional[datetime.datetime] = None,
        min_operation_modified_date_time: Optional[datetime.datetime] = None,
        max_operation_modified_date_time: Optional[datetime.datetime] = None,
        min_area: Optional[float] = None,
        max_area: Optional[float] = None,
        ids: Optional[List[str]] = None,
        names: Optional[List[str]] = None,
        property_filters: Optional[List[str]] = None,
        statuses: Optional[List[str]] = None,
        min_created_date_time: Optional[datetime.datetime] = None,
        max_created_date_time: Optional[datetime.datetime] = None,
        min_last_modified_date_time: Optional[datetime.datetime] = None,
        max_last_modified_date_time: Optional[datetime.datetime] = None,
        max_page_size: Optional[int] = 50,
        skip_token: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.PlantingDataListResponse"]:
        """Returns a paginated list of planting data resources across all farmers.

        :param min_avg_planting_rate: Minimum AvgPlantingRate value(inclusive).
        :type min_avg_planting_rate: float
        :param max_avg_planting_rate: Maximum AvgPlantingRate value (inclusive).
        :type max_avg_planting_rate: float
        :param min_total_material: Minimum TotalMaterial value(inclusive).
        :type min_total_material: float
        :param max_total_material: Maximum TotalMaterial value (inclusive).
        :type max_total_material: float
        :param min_avg_material: Minimum AvgMaterial value(inclusive).
        :type min_avg_material: float
        :param max_avg_material: Maximum AvgMaterial value (inclusive).
        :type max_avg_material: float
        :param sources: Sources of the operation data.
        :type sources: list[str]
        :param associated_boundary_ids: Boundary IDs associated with operation data.
        :type associated_boundary_ids: list[str]
        :param operation_boundary_ids: Operation boundary IDs associated with operation data.
        :type operation_boundary_ids: list[str]
        :param min_operation_start_date_time: Minimum start date-time of the operation data, sample
         format: yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type min_operation_start_date_time: ~datetime.datetime
        :param max_operation_start_date_time: Maximum start date-time of the operation data, sample
         format: yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type max_operation_start_date_time: ~datetime.datetime
        :param min_operation_end_date_time: Minimum end date-time of the operation data, sample format:
         yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type min_operation_end_date_time: ~datetime.datetime
        :param max_operation_end_date_time: Maximum end date-time of the operation data, sample format:
         yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type max_operation_end_date_time: ~datetime.datetime
        :param min_operation_modified_date_time: Minimum modified date-time of the operation data,
         sample format: yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type min_operation_modified_date_time: ~datetime.datetime
        :param max_operation_modified_date_time: Maximum modified date-time of the operation data,
         sample format: yyyy-MM-ddTHH:mm:ssZ (inclusive).
        :type max_operation_modified_date_time: ~datetime.datetime
        :param min_area: Minimum area for which operation was applied (inclusive).
        :type min_area: float
        :param max_area: Maximum area for which operation was applied (inclusive).
        :type max_area: float
        :param ids: Ids of the resource.
        :type ids: list[str]
        :param names: Names of the resource.
        :type names: list[str]
        :param property_filters: Filters on key-value pairs within the Properties object.
         eg. "{testKey} eq {testValue}".
        :type property_filters: list[str]
        :param statuses: Statuses of the resource.
        :type statuses: list[str]
        :param min_created_date_time: Minimum creation date of resource (inclusive).
        :type min_created_date_time: ~datetime.datetime
        :param max_created_date_time: Maximum creation date of resource (inclusive).
        :type max_created_date_time: ~datetime.datetime
        :param min_last_modified_date_time: Minimum last modified date of resource (inclusive).
        :type min_last_modified_date_time: ~datetime.datetime
        :param max_last_modified_date_time: Maximum last modified date of resource (inclusive).
        :type max_last_modified_date_time: ~datetime.datetime
        :param max_page_size: Maximum number of items needed (inclusive).
         Minimum = 10, Maximum = 1000, Default value = 50.
        :type max_page_size: int
        :param skip_token: Skip token for getting next set of results.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PlantingDataListResponse or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.agrifood.farming.models.PlantingDataListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PlantingDataListResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-31-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if min_avg_planting_rate is not None:
                    query_parameters['minAvgPlantingRate'] = self._serialize.query("min_avg_planting_rate", min_avg_planting_rate, 'float')
                if max_avg_planting_rate is not None:
                    query_parameters['maxAvgPlantingRate'] = self._serialize.query("max_avg_planting_rate", max_avg_planting_rate, 'float')
                if min_total_material is not None:
                    query_parameters['minTotalMaterial'] = self._serialize.query("min_total_material", min_total_material, 'float')
                if max_total_material is not None:
                    query_parameters['maxTotalMaterial'] = self._serialize.query("max_total_material", max_total_material, 'float')
                if min_avg_material is not None:
                    query_parameters['minAvgMaterial'] = self._serialize.query("min_avg_material", min_avg_material, 'float')
                if max_avg_material is not None:
                    query_parameters['maxAvgMaterial'] = self._serialize.query("max_avg_material", max_avg_material, 'float')
                if sources is not None:
                    query_parameters['sources'] = [self._serialize.query("sources", q, 'str') if q is not None else '' for q in sources]
                if associated_boundary_ids is not None:
                    query_parameters['associatedBoundaryIds'] = [self._serialize.query("associated_boundary_ids", q, 'str') if q is not None else '' for q in associated_boundary_ids]
                if operation_boundary_ids is not None:
                    query_parameters['operationBoundaryIds'] = [self._serialize.query("operation_boundary_ids", q, 'str') if q is not None else '' for q in operation_boundary_ids]
                if min_operation_start_date_time is not None:
                    query_parameters['minOperationStartDateTime'] = self._serialize.query("min_operation_start_date_time", min_operation_start_date_time, 'iso-8601')
                if max_operation_start_date_time is not None:
                    query_parameters['maxOperationStartDateTime'] = self._serialize.query("max_operation_start_date_time", max_operation_start_date_time, 'iso-8601')
                if min_operation_end_date_time is not None:
                    query_parameters['minOperationEndDateTime'] = self._serialize.query("min_operation_end_date_time", min_operation_end_date_time, 'iso-8601')
                if max_operation_end_date_time is not None:
                    query_parameters['maxOperationEndDateTime'] = self._serialize.query("max_operation_end_date_time", max_operation_end_date_time, 'iso-8601')
                if min_operation_modified_date_time is not None:
                    query_parameters['minOperationModifiedDateTime'] = self._serialize.query("min_operation_modified_date_time", min_operation_modified_date_time, 'iso-8601')
                if max_operation_modified_date_time is not None:
                    query_parameters['maxOperationModifiedDateTime'] = self._serialize.query("max_operation_modified_date_time", max_operation_modified_date_time, 'iso-8601')
                if min_area is not None:
                    query_parameters['minArea'] = self._serialize.query("min_area", min_area, 'float')
                if max_area is not None:
                    query_parameters['maxArea'] = self._serialize.query("max_area", max_area, 'float')
                if ids is not None:
                    query_parameters['ids'] = [self._serialize.query("ids", q, 'str') if q is not None else '' for q in ids]
                if names is not None:
                    query_parameters['names'] = [self._serialize.query("names", q, 'str') if q is not None else '' for q in names]
                if property_filters is not None:
                    query_parameters['propertyFilters'] = [self._serialize.query("property_filters", q, 'str') if q is not None else '' for q in property_filters]
                if statuses is not None:
                    query_parameters['statuses'] = [self._serialize.query("statuses", q, 'str') if q is not None else '' for q in statuses]
                if min_created_date_time is not None:
                    query_parameters['minCreatedDateTime'] = self._serialize.query("min_created_date_time", min_created_date_time, 'iso-8601')
                if max_created_date_time is not None:
                    query_parameters['maxCreatedDateTime'] = self._serialize.query("max_created_date_time", max_created_date_time, 'iso-8601')
                if min_last_modified_date_time is not None:
                    query_parameters['minLastModifiedDateTime'] = self._serialize.query("min_last_modified_date_time", min_last_modified_date_time, 'iso-8601')
                if max_last_modified_date_time is not None:
                    query_parameters['maxLastModifiedDateTime'] = self._serialize.query("max_last_modified_date_time", max_last_modified_date_time, 'iso-8601')
                if max_page_size is not None:
                    query_parameters['$maxPageSize'] = self._serialize.query("max_page_size", max_page_size, 'int', maximum=1000, minimum=10)
                if skip_token is not None:
                    query_parameters['$skipToken'] = self._serialize.query("skip_token", skip_token, 'str')
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('PlantingDataListResponse', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/planting-data'}  # type: ignore

    async def get(
        self,
        farmer_id: str,
        planting_data_id: str,
        **kwargs: Any
    ) -> "_models.PlantingData":
        """Get a specified planting data resource under a particular farmer.

        :param farmer_id: ID of the associated farmer resource.
        :type farmer_id: str
        :param planting_data_id: ID of the planting data resource.
        :type planting_data_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PlantingData, or the result of cls(response)
        :rtype: ~azure.agrifood.farming.models.PlantingData
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PlantingData"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-31-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'farmerId': self._serialize.url("farmer_id", farmer_id, 'str'),
            'plantingDataId': self._serialize.url("planting_data_id", planting_data_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('PlantingData', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/farmers/{farmerId}/planting-data/{plantingDataId}'}  # type: ignore

    async def create_or_update(
        self,
        farmer_id: str,
        planting_data_id: str,
        planting_data: Optional["_models.PlantingData"] = None,
        **kwargs: Any
    ) -> "_models.PlantingData":
        """Creates or updates an planting data resource under a particular farmer.

        :param farmer_id: ID of the associated farmer.
        :type farmer_id: str
        :param planting_data_id: ID of the planting data resource.
        :type planting_data_id: str
        :param planting_data: Planting data resource payload to create or update.
        :type planting_data: ~azure.agrifood.farming.models.PlantingData
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PlantingData, or the result of cls(response)
        :rtype: ~azure.agrifood.farming.models.PlantingData
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PlantingData"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-31-preview"
        content_type = kwargs.pop("content_type", "application/merge-patch+json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'farmerId': self._serialize.url("farmer_id", farmer_id, 'str'),
            'plantingDataId': self._serialize.url("planting_data_id", planting_data_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        if planting_data is not None:
            body_content = self._serialize.body(planting_data, 'PlantingData')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize('PlantingData', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('PlantingData', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/farmers/{farmerId}/planting-data/{plantingDataId}'}  # type: ignore

    async def delete(
        self,
        farmer_id: str,
        planting_data_id: str,
        **kwargs: Any
    ) -> None:
        """Deletes a specified planting data resource under a particular farmer.

        :param farmer_id: ID of the associated farmer resource.
        :type farmer_id: str
        :param planting_data_id: ID of the planting data.
        :type planting_data_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-31-preview"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
            'farmerId': self._serialize.url("farmer_id", farmer_id, 'str'),
            'plantingDataId': self._serialize.url("planting_data_id", planting_data_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/farmers/{farmerId}/planting-data/{plantingDataId}'}  # type: ignore
