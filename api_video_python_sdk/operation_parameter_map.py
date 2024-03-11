operation_parameter_map = {
    '/auth/api-key-POST': {
        'parameters': [
            {
                'name': 'apiKey'
            },
        ]
    },
    '/auth/refresh-POST': {
        'parameters': [
            {
                'name': 'refreshToken'
            },
        ]
    },
    '/analytics/live-streams/plays-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'dimension'
            },
            {
                'name': 'to'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'currentPage'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/analytics/videos/plays-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'dimension'
            },
            {
                'name': 'to'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'currentPage'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/videos/{videoId}/captions/{language}-DELETE': {
        'parameters': [
            {
                'name': 'videoId'
            },
            {
                'name': 'language'
            },
        ]
    },
    '/videos/{videoId}/captions/{language}-GET': {
        'parameters': [
            {
                'name': 'videoId'
            },
            {
                'name': 'language'
            },
        ]
    },
    '/videos/{videoId}/captions-GET': {
        'parameters': [
            {
                'name': 'videoId'
            },
            {
                'name': 'currentPage'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/videos/{videoId}/captions/{language}-PATCH': {
        'parameters': [
            {
                'name': 'videoId'
            },
            {
                'name': 'language'
            },
            {
                'name': 'default'
            },
        ]
    },
    '/videos/{videoId}/captions/{language}-POST': {
        'parameters': [
            {
                'name': 'videoId'
            },
            {
                'name': 'language'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/videos/{videoId}/chapters/{language}-DELETE': {
        'parameters': [
            {
                'name': 'videoId'
            },
            {
                'name': 'language'
            },
        ]
    },
    '/videos/{videoId}/chapters/{language}-GET': {
        'parameters': [
            {
                'name': 'videoId'
            },
            {
                'name': 'language'
            },
        ]
    },
    '/videos/{videoId}/chapters-GET': {
        'parameters': [
            {
                'name': 'videoId'
            },
            {
                'name': 'currentPage'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/videos/{videoId}/chapters/{language}-POST': {
        'parameters': [
            {
                'name': 'videoId'
            },
            {
                'name': 'language'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/live-streams-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'public'
            },
            {
                'name': 'playerId'
            },
            {
                'name': 'restreams'
            },
        ]
    },
    '/live-streams/{liveStreamId}-DELETE': {
        'parameters': [
            {
                'name': 'liveStreamId'
            },
        ]
    },
    '/live-streams/{liveStreamId}/thumbnail-DELETE': {
        'parameters': [
            {
                'name': 'liveStreamId'
            },
        ]
    },
    '/live-streams/{liveStreamId}-GET': {
        'parameters': [
            {
                'name': 'liveStreamId'
            },
        ]
    },
    '/live-streams-GET': {
        'parameters': [
            {
                'name': 'streamKey'
            },
            {
                'name': 'name'
            },
            {
                'name': 'sortBy'
            },
            {
                'name': 'sortOrder'
            },
            {
                'name': 'currentPage'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/live-streams/{liveStreamId}-PATCH': {
        'parameters': [
            {
                'name': 'liveStreamId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'public'
            },
            {
                'name': 'playerId'
            },
            {
                'name': 'restreams'
            },
        ]
    },
    '/live-streams/{liveStreamId}/thumbnail-POST': {
        'parameters': [
            {
                'name': 'liveStreamId'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/players/{playerId}-DELETE': {
        'parameters': [
            {
                'name': 'playerId'
            },
        ]
    },
    '/players/{playerId}-GET': {
        'parameters': [
            {
                'name': 'playerId'
            },
        ]
    },
    '/players-GET': {
        'parameters': [
            {
                'name': 'sortBy'
            },
            {
                'name': 'sortOrder'
            },
            {
                'name': 'currentPage'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/players-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'text'
            },
            {
                'name': 'link'
            },
            {
                'name': 'linkHover'
            },
            {
                'name': 'linkActive'
            },
            {
                'name': 'trackPlayed'
            },
            {
                'name': 'trackUnplayed'
            },
            {
                'name': 'trackBackground'
            },
            {
                'name': 'backgroundTop'
            },
            {
                'name': 'backgroundBottom'
            },
            {
                'name': 'backgroundText'
            },
            {
                'name': 'enableApi'
            },
            {
                'name': 'enableControls'
            },
            {
                'name': 'forceAutoplay'
            },
            {
                'name': 'hideTitle'
            },
            {
                'name': 'forceLoop'
            },
        ]
    },
    '/players/{playerId}/logo-DELETE': {
        'parameters': [
            {
                'name': 'playerId'
            },
        ]
    },
    '/players/{playerId}-PATCH': {
        'parameters': [
            {
                'name': 'playerId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'text'
            },
            {
                'name': 'link'
            },
            {
                'name': 'linkHover'
            },
            {
                'name': 'linkActive'
            },
            {
                'name': 'trackPlayed'
            },
            {
                'name': 'trackUnplayed'
            },
            {
                'name': 'trackBackground'
            },
            {
                'name': 'backgroundTop'
            },
            {
                'name': 'backgroundBottom'
            },
            {
                'name': 'backgroundText'
            },
            {
                'name': 'enableApi'
            },
            {
                'name': 'enableControls'
            },
            {
                'name': 'forceAutoplay'
            },
            {
                'name': 'hideTitle'
            },
            {
                'name': 'forceLoop'
            },
        ]
    },
    '/players/{playerId}/logo-POST': {
        'parameters': [
            {
                'name': 'playerId'
            },
            {
                'name': 'file'
            },
            {
                'name': 'link'
            },
        ]
    },
    '/upload-tokens/{uploadToken}-DELETE': {
        'parameters': [
            {
                'name': 'uploadToken'
            },
        ]
    },
    '/upload-tokens-POST': {
        'parameters': [
            {
                'name': 'ttl'
            },
        ]
    },
    '/upload-tokens/{uploadToken}-GET': {
        'parameters': [
            {
                'name': 'uploadToken'
            },
        ]
    },
    '/upload-tokens-GET': {
        'parameters': [
            {
                'name': 'sortBy'
            },
            {
                'name': 'sortOrder'
            },
            {
                'name': 'currentPage'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/videos-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'description'
            },
            {
                'name': 'source'
            },
            {
                'name': 'public'
            },
            {
                'name': 'panoramic'
            },
            {
                'name': 'mp4Support'
            },
            {
                'name': 'playerId'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'clip'
            },
            {
                'name': 'watermark'
            },
        ]
    },
    '/videos/{videoId}-DELETE': {
        'parameters': [
            {
                'name': 'videoId'
            },
        ]
    },
    '/videos/{videoId}-GET': {
        'parameters': [
            {
                'name': 'videoId'
            },
        ]
    },
    '/videos/{videoId}/status-GET': {
        'parameters': [
            {
                'name': 'videoId'
            },
        ]
    },
    '/videos/{videoId}/source-POST': {
        'parameters': [
            {
                'name': 'videoId'
            },
            {
                'name': 'file'
            },
            {
                'name': 'Content-Range'
            },
        ]
    },
    '/videos-GET': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'tags[]'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'description'
            },
            {
                'name': 'liveStreamId'
            },
            {
                'name': 'sortBy'
            },
            {
                'name': 'sortOrder'
            },
            {
                'name': 'currentPage'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/videos/{videoId}/thumbnail-PATCH': {
        'parameters': [
            {
                'name': 'timecode'
            },
            {
                'name': 'videoId'
            },
        ]
    },
    '/videos/{videoId}-PATCH': {
        'parameters': [
            {
                'name': 'videoId'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'playerId'
            },
            {
                'name': 'public'
            },
            {
                'name': 'panoramic'
            },
            {
                'name': 'mp4Support'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/upload-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'file'
            },
            {
                'name': 'Content-Range'
            },
            {
                'name': 'videoId'
            },
        ]
    },
    '/videos/{videoId}/thumbnail-POST': {
        'parameters': [
            {
                'name': 'videoId'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/watermarks-GET': {
        'parameters': [
            {
                'name': 'sortBy'
            },
            {
                'name': 'sortOrder'
            },
            {
                'name': 'currentPage'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/watermarks-POST': {
        'parameters': [
            {
                'name': 'file'
            },
        ]
    },
    '/watermarks/{watermarkId}-DELETE': {
        'parameters': [
            {
                'name': 'watermarkId'
            },
        ]
    },
    '/webhooks-POST': {
        'parameters': [
            {
                'name': 'events'
            },
            {
                'name': 'url'
            },
        ]
    },
    '/webhooks/{webhookId}-DELETE': {
        'parameters': [
            {
                'name': 'webhookId'
            },
        ]
    },
    '/webhooks/{webhookId}-GET': {
        'parameters': [
            {
                'name': 'webhookId'
            },
        ]
    },
    '/webhooks-GET': {
        'parameters': [
            {
                'name': 'events'
            },
            {
                'name': 'currentPage'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
};