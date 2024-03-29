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

from api_video_python_sdk.type.restreams_request_object import RestreamsRequestObject

class RequiredLiveStreamUpdatePayload(TypedDict):
    pass

class OptionalLiveStreamUpdatePayload(TypedDict, total=False):
    # The name you want to use for your live stream.
    name: str

    # Whether your video can be viewed by everyone, or requires authentication to see it. A setting of false will require a unique token for each view. Learn more about the Private Video feature [here](https://docs.api.video/delivery-analytics/video-privacy-access-management).
    public: bool

    # The unique ID for the player associated with a live stream that you want to update.
    playerId: str

    # Use this parameter to add, edit, or remove RTMP services where you want to restream a live stream. The list can only contain up to 5 destinations. This operation updates all restream destinations in the same request. If you do not want to modify an existing restream destination, you need to include it in your request, otherwise it is removed.
    restreams: typing.List[RestreamsRequestObject]

class LiveStreamUpdatePayload(RequiredLiveStreamUpdatePayload, OptionalLiveStreamUpdatePayload):
    pass
