# coding: utf-8

"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from api_video_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from api_video_python_sdk.api_response import AsyncGeneratorResponse
from api_video_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from api_video_python_sdk import schemas  # noqa: F401

from api_video_python_sdk.model.video import Video as VideoSchema
from api_video_python_sdk.model.token_upload_payload import TokenUploadPayload as TokenUploadPayloadSchema
from api_video_python_sdk.model.bad_request import BadRequest as BadRequestSchema

from api_video_python_sdk.type.bad_request import BadRequest
from api_video_python_sdk.type.video import Video
from api_video_python_sdk.type.token_upload_payload import TokenUploadPayload

from ...api_client import Dictionary
from api_video_python_sdk.pydantic.token_upload_payload import TokenUploadPayload as TokenUploadPayloadPydantic
from api_video_python_sdk.pydantic.video import Video as VideoPydantic
from api_video_python_sdk.pydantic.bad_request import BadRequest as BadRequestPydantic

# Query params
TokenSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'token': typing.Union[TokenSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_token = api_client.QueryParameter(
    name="token",
    style=api_client.ParameterStyle.FORM,
    schema=TokenSchema,
    required=True,
    explode=True,
)
# Header params


class ContentRangeSchema(
    schemas.StrSchema
):
    pass
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'Content-Range': typing.Union[ContentRangeSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_content_range = api_client.HeaderParameter(
    name="Content-Range",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ContentRangeSchema,
)
# body param
SchemaForRequestBodyMultipartFormData = TokenUploadPayloadSchema


request_body_token_upload_payload = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationJson = VideoSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Video


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Video


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = BadRequestSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: BadRequest


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: BadRequest


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _upload_mapped_args(
        self,
        token: str,
        file: typing.IO,
        content_range: typing.Optional[str] = None,
        video_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        _body = {}
        if file is not None:
            _body["file"] = file
        if video_id is not None:
            _body["videoId"] = video_id
        args.body = _body
        if token is not None:
            _query_params["token"] = token
        if content_range is not None:
            _header_params["Content-Range"] = content_range
        args.query = _query_params
        args.header = _header_params
        return args

    async def _aupload_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Upload with an delegated upload token
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_token,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_content_range,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/upload',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_token_upload_payload.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _upload_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'multipart/form-data',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Upload with an delegated upload token
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_token,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_content_range,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/upload',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_token_upload_payload.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UploadRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupload(
        self,
        token: str,
        file: typing.IO,
        content_range: typing.Optional[str] = None,
        video_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._upload_mapped_args(
            token=token,
            file=file,
            content_range=content_range,
            video_id=video_id,
        )
        return await self._aupload_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def upload(
        self,
        token: str,
        file: typing.IO,
        content_range: typing.Optional[str] = None,
        video_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._upload_mapped_args(
            token=token,
            file=file,
            content_range=content_range,
            video_id=video_id,
        )
        return self._upload_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
        )

class Upload(BaseApi):

    async def aupload(
        self,
        token: str,
        file: typing.IO,
        content_range: typing.Optional[str] = None,
        video_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> VideoPydantic:
        raw_response = await self.raw.aupload(
            token=token,
            file=file,
            content_range=content_range,
            video_id=video_id,
            **kwargs,
        )
        if validate:
            return VideoPydantic(**raw_response.body)
        return api_client.construct_model_instance(VideoPydantic, raw_response.body)
    
    
    def upload(
        self,
        token: str,
        file: typing.IO,
        content_range: typing.Optional[str] = None,
        video_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> VideoPydantic:
        raw_response = self.raw.upload(
            token=token,
            file=file,
            content_range=content_range,
            video_id=video_id,
        )
        if validate:
            return VideoPydantic(**raw_response.body)
        return api_client.construct_model_instance(VideoPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        token: str,
        file: typing.IO,
        content_range: typing.Optional[str] = None,
        video_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._upload_mapped_args(
            token=token,
            file=file,
            content_range=content_range,
            video_id=video_id,
        )
        return await self._aupload_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        token: str,
        file: typing.IO,
        content_range: typing.Optional[str] = None,
        video_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._upload_mapped_args(
            token=token,
            file=file,
            content_range=content_range,
            video_id=video_id,
        )
        return self._upload_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
        )

