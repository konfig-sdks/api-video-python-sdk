# coding: utf-8

"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from api_video_python_sdk.pydantic.metadata import Metadata
from api_video_python_sdk.pydantic.video_assets import VideoAssets
from api_video_python_sdk.pydantic.video_source import VideoSource
from api_video_python_sdk.pydantic.video_tags import VideoTags

class Video(BaseModel):
    # The unique identifier of the video object.
    video_id: str = Field(alias='videoId')

    tags: typing.Optional[VideoTags] = Field(None, alias='tags')

    # The title of the video content. 
    title: typing.Optional[str] = Field(None, alias='title')

    # A description for the video content. 
    description: typing.Optional[str] = Field(None, alias='description')

    # When a video was created, presented in ISO-8601 format.
    created_at: typing.Optional[datetime] = Field(None, alias='createdAt')

    # The date and time the API created the video. Date and time are provided using ISO-8601 UTC format.
    published_at: typing.Optional[datetime] = Field(None, alias='publishedAt')

    # The date and time the video was updated. Date and time are provided using ISO-8601 UTC format.
    updated_at: typing.Optional[datetime] = Field(None, alias='updatedAt')

    # Metadata you can use to categorise and filter videos. Metadata is a list of dictionaries, where each dictionary represents a key value pair for categorising a video. [Dynamic Metadata](https://api.video/blog/endpoints/dynamic-metadata/) allows you to define a key that allows any value pair. 
    metadata: typing.Optional[typing.List[Metadata]] = Field(None, alias='metadata')

    source: typing.Optional[VideoSource] = Field(None, alias='source')

    assets: typing.Optional[VideoAssets] = Field(None, alias='assets')

    # The id of the player that will be applied on the video. 
    player_id: typing.Optional[str] = Field(None, alias='playerId')

    # Defines if the content is publicly reachable or if a unique token is needed for each play session. Default is true. Tutorials on [private videos](https://api.video/blog/endpoints/private-videos/). 
    public: typing.Optional[bool] = Field(None, alias='public')

    # Defines if video is panoramic. 
    panoramic: typing.Optional[bool] = Field(None, alias='panoramic')

    # This lets you know whether mp4 is supported. If enabled, an mp4 URL will be provided in the response for the video. 
    mp4_support: typing.Optional[bool] = Field(None, alias='mp4Support')
    class Config:
        arbitrary_types_allowed = True
