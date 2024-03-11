# coding: utf-8

"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from api_video_python_sdk.paths.webhooks.post import CreateWebhookEventRaw
from api_video_python_sdk.paths.webhooks_webhook_id.delete import DeleteWebhookRaw
from api_video_python_sdk.paths.webhooks_webhook_id.get import GetDetailsByIdRaw
from api_video_python_sdk.paths.webhooks.get import ListAllRaw


class WebhooksApiRaw(
    CreateWebhookEventRaw,
    DeleteWebhookRaw,
    GetDetailsByIdRaw,
    ListAllRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
