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

from api_video_python_sdk.pydantic.webhook_events import WebhookEvents

class Webhook(BaseModel):
    # Unique identifier of the webhook
    webhook_id: typing.Optional[str] = Field(None, alias='webhookId')

    # When an webhook was created, presented in ISO-8601 format.
    created_at: typing.Optional[datetime] = Field(None, alias='createdAt')

    events: typing.Optional[WebhookEvents] = Field(None, alias='events')

    # URL of the webhook
    url: typing.Optional[str] = Field(None, alias='url')
    class Config:
        arbitrary_types_allowed = True
