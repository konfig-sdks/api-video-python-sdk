# coding: utf-8

"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

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


class VideoStatus(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def ingest() -> typing.Type['VideoStatusIngest']:
                return VideoStatusIngest
        
            @staticmethod
            def encoding() -> typing.Type['VideoStatusEncoding']:
                return VideoStatusEncoding
            __annotations__ = {
                "ingest": ingest,
                "encoding": encoding,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ingest"]) -> 'VideoStatusIngest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["encoding"]) -> 'VideoStatusEncoding': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ingest", "encoding", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ingest"]) -> typing.Union['VideoStatusIngest', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["encoding"]) -> typing.Union['VideoStatusEncoding', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ingest", "encoding", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ingest: typing.Union['VideoStatusIngest', schemas.Unset] = schemas.unset,
        encoding: typing.Union['VideoStatusEncoding', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VideoStatus':
        return super().__new__(
            cls,
            *args,
            ingest=ingest,
            encoding=encoding,
            _configuration=_configuration,
            **kwargs,
        )

from api_video_python_sdk.model.video_status_encoding import VideoStatusEncoding
from api_video_python_sdk.model.video_status_ingest import VideoStatusIngest