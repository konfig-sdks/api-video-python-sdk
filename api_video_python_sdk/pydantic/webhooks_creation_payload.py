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

from api_video_python_sdk.pydantic.webhooks_creation_payload_events import WebhooksCreationPayloadEvents

class WebhooksCreationPayload(BaseModel):
    events: WebhooksCreationPayloadEvents = Field(alias='events')

    # The the url to which HTTP notifications are sent. It could be any http or https URL.
    url: str = Field(alias='url')
    class Config:
        arbitrary_types_allowed = True
