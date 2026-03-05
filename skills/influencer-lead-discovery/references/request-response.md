# Request and Response Guide

## `GET /api/ping`
- operationId: `ping`
- summary: ping
- parameters: none
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: string |

## `GET /api/v1/instagram/user/brands`
- operationId: `instagram_user_brands`
- summary: 合作品牌
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
| `page` | `query` | `false` | `integer` | 页码 |
| `page_size` | `query` | `false` | `integer` | 每页数量 |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_BasePage_VideoBrandCollaborationItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/instagram/user/hashtag/engagement`
- operationId: `instagram_user_hashtag_engagement`
- summary: 用户top10 hashtag互动数据
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_KolHashtagEngagementRes__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/instagram/user/info`
- operationId: `instagram_db_user_info`
- summary: 用户信息
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_InstagramUserInfoRes_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/instagram/user/medias`
- operationId: `instagram_db_user_medias`
- summary: 用户贴文
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
| `publish_at_start` | `query` | `false` | `string` | 发布时间开始 |
| `publish_at_end` | `query` | `false` | `string` | 发布时间结束 |
| `media_code` | `query` | `false` | `string` | 帖子Code |
| `is_paid` | `query` | `false` | `object` | 是否合作帖子，1:是 |
| `page` | `query` | `false` | `integer` | Page number |
| `page_size` | `query` | `false` | `integer` | Page size |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_BasePage_InstagramUserMediaItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/instagram/user/similar`
- operationId: `instagram_user_similar`
- summary: 相似用户推荐
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_InstagramUserSimilarItem__ |
| `422` | application/json: HTTPValidationError |

## `POST /api/v1/search/instagram/media`
- operationId: `search_instagram_media`
- summary: 搜索instagram帖文
- parameters: none
- requestBody:
| content-type | schema |
|---|---|
| `application/json` | `SearchInstagramMediaReq` |
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_BasePage_SearchInstagramMediaRep__ |
| `422` | application/json: HTTPValidationError |

## `POST /api/v1/search/instagram/user`
- operationId: `search_instagram_user`
- summary: 搜索instagram用户
- parameters: none
- requestBody:
| content-type | schema |
|---|---|
| `application/json` | `SearchInstagramUserReq` |
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_BasePage_SearchInstagramUserRep__ |
| `422` | application/json: HTTPValidationError |

## `POST /api/v1/search/suggest`
- operationId: `search_instagram_suggest`
- summary: 搜索联想
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `platform` | `query` | `true` | `string` | 平台: youtube/tiktok/instagram |
| `query` | `query` | `true` | `string` | 搜索关键词 |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_SearchSuggestItem__ |
| `422` | application/json: HTTPValidationError |

## `POST /api/v1/search/tiktok/user`
- operationId: `search_tiktok_user`
- summary: 搜索tiktok用户
- parameters: none
- requestBody:
| content-type | schema |
|---|---|
| `application/json` | `SearchTiktokUserReq` |
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_BasePage_SearchTiktokUserRep__ |
| `422` | application/json: HTTPValidationError |

## `POST /api/v1/search/tiktok/video`
- operationId: `search_tiktok_video`
- summary: 搜索tiktok视频
- parameters: none
- requestBody:
| content-type | schema |
|---|---|
| `application/json` | `SearchTiktokVideoReq` |
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_BasePage_SearchTiktokVideoRep__ |
| `422` | application/json: HTTPValidationError |

## `POST /api/v1/search/youtube/user`
- operationId: `search_youtube_user`
- summary: 搜索youtube用户
- parameters: none
- requestBody:
| content-type | schema |
|---|---|
| `application/json` | `SearchYoutubeUserReq` |
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_BasePage_SearchYoutubeUserRep__ |
| `422` | application/json: HTTPValidationError |

## `POST /api/v1/search/youtube/video`
- operationId: `search_youtube_video`
- summary: 搜索youtube视频
- parameters: none
- requestBody:
| content-type | schema |
|---|---|
| `application/json` | `SearchYoutubeVideoReq` |
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_BasePage_SearchYoutubeVideoRep__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/tiktok/user/brands`
- operationId: `tiktok_user_brands`
- summary: 合作品牌
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
| `page` | `query` | `false` | `integer` | 页码 |
| `page_size` | `query` | `false` | `integer` | 每页数量 |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_BasePage_VideoBrandCollaborationItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/tiktok/user/hashtag/engagement`
- operationId: `tiktok_user_hashtag_engagement`
- summary: 用户top10 hashtag互动数据
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_KolHashtagEngagementRes__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/tiktok/user/info`
- operationId: `tiktok_db_user_info`
- summary: 用户信息
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `false` | `string` | unique_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_TiktokUserInfoRes_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/tiktok/user/similar`
- operationId: `tiktok_user_similar`
- summary: 相似用户推荐
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `false` | `string` | unique_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_TiktokUserSimilarItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/tiktok/user/videos`
- operationId: `tiktok_db_user_videos`
- summary: 用户视频
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
| `publish_at_start` | `query` | `false` | `string` | 发布时间开始 |
| `publish_at_end` | `query` | `false` | `string` | 发布时间结束 |
| `video_id` | `query` | `false` | `string` | 视频ID |
| `is_paid` | `query` | `false` | `object` | 是否合作视频，1:是 |
| `page` | `query` | `false` | `integer` | Page number |
| `page_size` | `query` | `false` | `integer` | Page size |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_BasePage_TiktokUserVideoInfoItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/youtube/user/brands`
- operationId: `youtube_user_brands`
- summary: 合作品牌
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `true` | `string` | 频道ID |
| `page` | `query` | `false` | `integer` | 页码 |
| `page_size` | `query` | `false` | `integer` | 每页数量 |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_BasePage_VideoBrandCollaborationItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/youtube/user/hashtag/engagement`
- operationId: `youtube_user_hashtag_engagement`
- summary: 用户top10 hashtag互动数据
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `true` | `string` | 频道ID |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_KolHashtagEngagementRes__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/youtube/user/info`
- operationId: `youtube_db_user_info`
- summary: 用户信息
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `false` | `string` | channel_id |
| `username` | `query` | `false` | `string` | username |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_YoutubeUserInfoRes_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/youtube/user/similar`
- operationId: `youtube_user_similar`
- summary: 相似用户推荐
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `false` | `string` | channel_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_YoutubeUserSimilarItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/youtube/user/videos`
- operationId: `youtube_db_user_videos`
- summary: 用户视频
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `true` | `string` | 频道ID |
| `publish_at_start` | `query` | `false` | `string` | 发布时间开始 |
| `publish_at_end` | `query` | `false` | `string` | 发布时间结束 |
| `video_id` | `query` | `false` | `string` | 视频ID |
| `is_paid` | `query` | `false` | `object` | 是否合作视频，1:是 |
| `page` | `query` | `false` | `integer` | Page number |
| `page_size` | `query` | `false` | `integer` | Page size |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_BasePage_YoutubeUserVideoInfoItem__ |
| `422` | application/json: HTTPValidationError |
