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


class VideoStatusEncoding(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            playable = schemas.BoolSchema
            
            
            class qualities(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Quality']:
                        return Quality
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Quality'], typing.List['Quality']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'qualities':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Quality':
                    return super().__getitem__(i)
        
            @staticmethod
            def metadata() -> typing.Type['VideoStatusEncodingMetadata']:
                return VideoStatusEncodingMetadata
            __annotations__ = {
                "playable": playable,
                "qualities": qualities,
                "metadata": metadata,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["playable"]) -> MetaOapg.properties.playable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["qualities"]) -> MetaOapg.properties.qualities: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'VideoStatusEncodingMetadata': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["playable", "qualities", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["playable"]) -> typing.Union[MetaOapg.properties.playable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["qualities"]) -> typing.Union[MetaOapg.properties.qualities, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['VideoStatusEncodingMetadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["playable", "qualities", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        playable: typing.Union[MetaOapg.properties.playable, bool, schemas.Unset] = schemas.unset,
        qualities: typing.Union[MetaOapg.properties.qualities, list, tuple, schemas.Unset] = schemas.unset,
        metadata: typing.Union['VideoStatusEncodingMetadata', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VideoStatusEncoding':
        return super().__new__(
            cls,
            *args,
            playable=playable,
            qualities=qualities,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )

from api_video_python_sdk.model.quality import Quality
from api_video_python_sdk.model.video_status_encoding_metadata import VideoStatusEncodingMetadata
