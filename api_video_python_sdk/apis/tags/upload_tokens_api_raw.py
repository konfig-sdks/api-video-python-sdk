# coding: utf-8

"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.

    The version of the OpenAPI document: 1
    Generated by: https://konfigthis.com
"""

from api_video_python_sdk.paths.upload_tokens_upload_token.delete import DeleteTokenRaw
from api_video_python_sdk.paths.upload_tokens.post import GenerateTokenRaw
from api_video_python_sdk.paths.upload_tokens_upload_token.get import GetDetailsRaw
from api_video_python_sdk.paths.upload_tokens.get import ListActiveDelegatedTokensRaw


class UploadTokensApiRaw(
    DeleteTokenRaw,
    GenerateTokenRaw,
    GetDetailsRaw,
    ListActiveDelegatedTokensRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass