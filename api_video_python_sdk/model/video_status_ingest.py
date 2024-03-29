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


class VideoStatusIngest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Details about the capturing, transferring, and storing of your video for use immediately or in the future.
    """


    class MetaOapg:
        
        class properties:
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "uploading": "UPLOADING",
                        "uploaded": "UPLOADED",
                        "ingesting": "INGESTING",
                        "ingested": "INGESTED",
                    }
                
                @schemas.classproperty
                def UPLOADING(cls):
                    return cls("uploading")
                
                @schemas.classproperty
                def UPLOADED(cls):
                    return cls("uploaded")
                
                @schemas.classproperty
                def INGESTING(cls):
                    return cls("ingesting")
                
                @schemas.classproperty
                def INGESTED(cls):
                    return cls("ingested")
            
            
            class filesize(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'filesize':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class receivedBytes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BytesRange']:
                        return BytesRange
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['BytesRange'], typing.List['BytesRange']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'receivedBytes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'BytesRange':
                    return super().__getitem__(i)
        
            @staticmethod
            def receivedParts() -> typing.Type['VideoStatusIngestReceivedParts']:
                return VideoStatusIngestReceivedParts
            __annotations__ = {
                "status": status,
                "filesize": filesize,
                "receivedBytes": receivedBytes,
                "receivedParts": receivedParts,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filesize"]) -> MetaOapg.properties.filesize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receivedBytes"]) -> MetaOapg.properties.receivedBytes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receivedParts"]) -> 'VideoStatusIngestReceivedParts': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "filesize", "receivedBytes", "receivedParts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filesize"]) -> typing.Union[MetaOapg.properties.filesize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receivedBytes"]) -> typing.Union[MetaOapg.properties.receivedBytes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receivedParts"]) -> typing.Union['VideoStatusIngestReceivedParts', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "filesize", "receivedBytes", "receivedParts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        filesize: typing.Union[MetaOapg.properties.filesize, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        receivedBytes: typing.Union[MetaOapg.properties.receivedBytes, list, tuple, schemas.Unset] = schemas.unset,
        receivedParts: typing.Union['VideoStatusIngestReceivedParts', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VideoStatusIngest':
        return super().__new__(
            cls,
            *args,
            status=status,
            filesize=filesize,
            receivedBytes=receivedBytes,
            receivedParts=receivedParts,
            _configuration=_configuration,
            **kwargs,
        )

from api_video_python_sdk.model.bytes_range import BytesRange
from api_video_python_sdk.model.video_status_ingest_received_parts import VideoStatusIngestReceivedParts
