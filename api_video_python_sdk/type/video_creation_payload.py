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

from api_video_python_sdk.type.metadata import Metadata
from api_video_python_sdk.type.video_clip import VideoClip
from api_video_python_sdk.type.video_creation_payload_tags import VideoCreationPayloadTags
from api_video_python_sdk.type.video_watermark import VideoWatermark

class RequiredVideoCreationPayload(TypedDict):
    # The title of your new video.
    title: str

class OptionalVideoCreationPayload(TypedDict, total=False):
    tags: VideoCreationPayloadTags

    # A brief description of your video.
    description: str

    # You can either add a video already on the web, by entering the URL of the video, or you can also enter the `videoId` of one of the videos you already have on your api.video acccount, and this will generate a copy of your video. Creating a copy of a video can be especially useful if you want to keep your original video and trim or apply a watermark onto the copy you would create.
    source: str

    # Default: True. If set to `false` the video will become private. More information on private videos can be found [here](https://docs.api.video/delivery-analytics/video-privacy-access-management)
    public: bool

    # Indicates if your video is a 360/immersive video.
    panoramic: bool

    # Enables mp4 version in addition to streamed version.
    mp4Support: bool

    # The unique identification number for your video player.
    playerId: str

    # A list of key value pairs that you use to provide metadata for your video. These pairs can be made dynamic, allowing you to segment your audience. Read more on [dynamic metadata](https://api.video/blog/endpoints/dynamic-metadata/).
    metadata: typing.List[Metadata]

    clip: VideoClip

    watermark: VideoWatermark

class VideoCreationPayload(RequiredVideoCreationPayload, OptionalVideoCreationPayload):
    pass
