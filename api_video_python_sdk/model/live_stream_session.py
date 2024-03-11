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


class LiveStreamSession(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def session() -> typing.Type['LiveStreamSessionSession']:
                return LiveStreamSessionSession
        
            @staticmethod
            def location() -> typing.Type['LiveStreamSessionLocation']:
                return LiveStreamSessionLocation
        
            @staticmethod
            def referrer() -> typing.Type['LiveStreamSessionReferrer']:
                return LiveStreamSessionReferrer
        
            @staticmethod
            def device() -> typing.Type['LiveStreamSessionDevice']:
                return LiveStreamSessionDevice
        
            @staticmethod
            def os() -> typing.Type['VideoSessionOs']:
                return VideoSessionOs
        
            @staticmethod
            def client() -> typing.Type['LiveStreamSessionClient']:
                return LiveStreamSessionClient
            __annotations__ = {
                "session": session,
                "location": location,
                "referrer": referrer,
                "device": device,
                "os": os,
                "client": client,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["session"]) -> 'LiveStreamSessionSession': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> 'LiveStreamSessionLocation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referrer"]) -> 'LiveStreamSessionReferrer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["device"]) -> 'LiveStreamSessionDevice': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["os"]) -> 'VideoSessionOs': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client"]) -> 'LiveStreamSessionClient': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["session", "location", "referrer", "device", "os", "client", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["session"]) -> typing.Union['LiveStreamSessionSession', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> typing.Union['LiveStreamSessionLocation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referrer"]) -> typing.Union['LiveStreamSessionReferrer', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["device"]) -> typing.Union['LiveStreamSessionDevice', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["os"]) -> typing.Union['VideoSessionOs', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client"]) -> typing.Union['LiveStreamSessionClient', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["session", "location", "referrer", "device", "os", "client", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        session: typing.Union['LiveStreamSessionSession', schemas.Unset] = schemas.unset,
        location: typing.Union['LiveStreamSessionLocation', schemas.Unset] = schemas.unset,
        referrer: typing.Union['LiveStreamSessionReferrer', schemas.Unset] = schemas.unset,
        device: typing.Union['LiveStreamSessionDevice', schemas.Unset] = schemas.unset,
        os: typing.Union['VideoSessionOs', schemas.Unset] = schemas.unset,
        client: typing.Union['LiveStreamSessionClient', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LiveStreamSession':
        return super().__new__(
            cls,
            *args,
            session=session,
            location=location,
            referrer=referrer,
            device=device,
            os=os,
            client=client,
            _configuration=_configuration,
            **kwargs,
        )

from api_video_python_sdk.model.live_stream_session_client import LiveStreamSessionClient
from api_video_python_sdk.model.live_stream_session_device import LiveStreamSessionDevice
from api_video_python_sdk.model.live_stream_session_location import LiveStreamSessionLocation
from api_video_python_sdk.model.live_stream_session_referrer import LiveStreamSessionReferrer
from api_video_python_sdk.model.live_stream_session_session import LiveStreamSessionSession
from api_video_python_sdk.model.video_session_os import VideoSessionOs