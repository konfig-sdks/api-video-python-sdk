# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from api_video_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    AUTH_APIKEY = "/auth/api-key"
    AUTH_REFRESH = "/auth/refresh"
    VIDEOS = "/videos"
    VIDEOS_VIDEO_ID_SOURCE = "/videos/{videoId}/source"
    WATERMARKS = "/watermarks"
    WATERMARKS_WATERMARK_ID = "/watermarks/{watermarkId}"
    VIDEOS_VIDEO_ID_THUMBNAIL = "/videos/{videoId}/thumbnail"
    VIDEOS_VIDEO_ID = "/videos/{videoId}"
    VIDEOS_VIDEO_ID_STATUS = "/videos/{videoId}/status"
    UPLOADTOKENS = "/upload-tokens"
    UPLOADTOKENS_UPLOAD_TOKEN = "/upload-tokens/{uploadToken}"
    UPLOAD = "/upload"
    LIVESTREAMS = "/live-streams"
    LIVESTREAMS_LIVE_STREAM_ID = "/live-streams/{liveStreamId}"
    LIVESTREAMS_LIVE_STREAM_ID_THUMBNAIL = "/live-streams/{liveStreamId}/thumbnail"
    VIDEOS_VIDEO_ID_CAPTIONS_LANGUAGE = "/videos/{videoId}/captions/{language}"
    VIDEOS_VIDEO_ID_CAPTIONS = "/videos/{videoId}/captions"
    VIDEOS_VIDEO_ID_CHAPTERS_LANGUAGE = "/videos/{videoId}/chapters/{language}"
    VIDEOS_VIDEO_ID_CHAPTERS = "/videos/{videoId}/chapters"
    PLAYERS = "/players"
    PLAYERS_PLAYER_ID = "/players/{playerId}"
    PLAYERS_PLAYER_ID_LOGO = "/players/{playerId}/logo"
    ANALYTICS_VIDEOS_PLAYS = "/analytics/videos/plays"
    ANALYTICS_LIVESTREAMS_PLAYS = "/analytics/live-streams/plays"
    WEBHOOKS = "/webhooks"
    WEBHOOKS_WEBHOOK_ID = "/webhooks/{webhookId}"
