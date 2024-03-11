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


class PlayerThemeUpdatePayload(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            text = schemas.StrSchema
            link = schemas.StrSchema
            linkHover = schemas.StrSchema
            linkActive = schemas.StrSchema
            trackPlayed = schemas.StrSchema
            trackUnplayed = schemas.StrSchema
            trackBackground = schemas.StrSchema
            backgroundTop = schemas.StrSchema
            backgroundBottom = schemas.StrSchema
            backgroundText = schemas.StrSchema
            enableApi = schemas.BoolSchema
            enableControls = schemas.BoolSchema
            forceAutoplay = schemas.BoolSchema
            hideTitle = schemas.BoolSchema
            forceLoop = schemas.BoolSchema
            __annotations__ = {
                "name": name,
                "text": text,
                "link": link,
                "linkHover": linkHover,
                "linkActive": linkActive,
                "trackPlayed": trackPlayed,
                "trackUnplayed": trackUnplayed,
                "trackBackground": trackBackground,
                "backgroundTop": backgroundTop,
                "backgroundBottom": backgroundBottom,
                "backgroundText": backgroundText,
                "enableApi": enableApi,
                "enableControls": enableControls,
                "forceAutoplay": forceAutoplay,
                "hideTitle": hideTitle,
                "forceLoop": forceLoop,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linkHover"]) -> MetaOapg.properties.linkHover: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linkActive"]) -> MetaOapg.properties.linkActive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trackPlayed"]) -> MetaOapg.properties.trackPlayed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trackUnplayed"]) -> MetaOapg.properties.trackUnplayed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trackBackground"]) -> MetaOapg.properties.trackBackground: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["backgroundTop"]) -> MetaOapg.properties.backgroundTop: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["backgroundBottom"]) -> MetaOapg.properties.backgroundBottom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["backgroundText"]) -> MetaOapg.properties.backgroundText: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enableApi"]) -> MetaOapg.properties.enableApi: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enableControls"]) -> MetaOapg.properties.enableControls: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forceAutoplay"]) -> MetaOapg.properties.forceAutoplay: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hideTitle"]) -> MetaOapg.properties.hideTitle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forceLoop"]) -> MetaOapg.properties.forceLoop: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "text", "link", "linkHover", "linkActive", "trackPlayed", "trackUnplayed", "trackBackground", "backgroundTop", "backgroundBottom", "backgroundText", "enableApi", "enableControls", "forceAutoplay", "hideTitle", "forceLoop", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> typing.Union[MetaOapg.properties.text, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union[MetaOapg.properties.link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linkHover"]) -> typing.Union[MetaOapg.properties.linkHover, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linkActive"]) -> typing.Union[MetaOapg.properties.linkActive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trackPlayed"]) -> typing.Union[MetaOapg.properties.trackPlayed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trackUnplayed"]) -> typing.Union[MetaOapg.properties.trackUnplayed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trackBackground"]) -> typing.Union[MetaOapg.properties.trackBackground, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["backgroundTop"]) -> typing.Union[MetaOapg.properties.backgroundTop, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["backgroundBottom"]) -> typing.Union[MetaOapg.properties.backgroundBottom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["backgroundText"]) -> typing.Union[MetaOapg.properties.backgroundText, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enableApi"]) -> typing.Union[MetaOapg.properties.enableApi, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enableControls"]) -> typing.Union[MetaOapg.properties.enableControls, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forceAutoplay"]) -> typing.Union[MetaOapg.properties.forceAutoplay, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hideTitle"]) -> typing.Union[MetaOapg.properties.hideTitle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forceLoop"]) -> typing.Union[MetaOapg.properties.forceLoop, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "text", "link", "linkHover", "linkActive", "trackPlayed", "trackUnplayed", "trackBackground", "backgroundTop", "backgroundBottom", "backgroundText", "enableApi", "enableControls", "forceAutoplay", "hideTitle", "forceLoop", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        text: typing.Union[MetaOapg.properties.text, str, schemas.Unset] = schemas.unset,
        link: typing.Union[MetaOapg.properties.link, str, schemas.Unset] = schemas.unset,
        linkHover: typing.Union[MetaOapg.properties.linkHover, str, schemas.Unset] = schemas.unset,
        linkActive: typing.Union[MetaOapg.properties.linkActive, str, schemas.Unset] = schemas.unset,
        trackPlayed: typing.Union[MetaOapg.properties.trackPlayed, str, schemas.Unset] = schemas.unset,
        trackUnplayed: typing.Union[MetaOapg.properties.trackUnplayed, str, schemas.Unset] = schemas.unset,
        trackBackground: typing.Union[MetaOapg.properties.trackBackground, str, schemas.Unset] = schemas.unset,
        backgroundTop: typing.Union[MetaOapg.properties.backgroundTop, str, schemas.Unset] = schemas.unset,
        backgroundBottom: typing.Union[MetaOapg.properties.backgroundBottom, str, schemas.Unset] = schemas.unset,
        backgroundText: typing.Union[MetaOapg.properties.backgroundText, str, schemas.Unset] = schemas.unset,
        enableApi: typing.Union[MetaOapg.properties.enableApi, bool, schemas.Unset] = schemas.unset,
        enableControls: typing.Union[MetaOapg.properties.enableControls, bool, schemas.Unset] = schemas.unset,
        forceAutoplay: typing.Union[MetaOapg.properties.forceAutoplay, bool, schemas.Unset] = schemas.unset,
        hideTitle: typing.Union[MetaOapg.properties.hideTitle, bool, schemas.Unset] = schemas.unset,
        forceLoop: typing.Union[MetaOapg.properties.forceLoop, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PlayerThemeUpdatePayload':
        return super().__new__(
            cls,
            *args,
            name=name,
            text=text,
            link=link,
            linkHover=linkHover,
            linkActive=linkActive,
            trackPlayed=trackPlayed,
            trackUnplayed=trackUnplayed,
            trackBackground=trackBackground,
            backgroundTop=backgroundTop,
            backgroundBottom=backgroundBottom,
            backgroundText=backgroundText,
            enableApi=enableApi,
            enableControls=enableControls,
            forceAutoplay=forceAutoplay,
            hideTitle=hideTitle,
            forceLoop=forceLoop,
            _configuration=_configuration,
            **kwargs,
        )
