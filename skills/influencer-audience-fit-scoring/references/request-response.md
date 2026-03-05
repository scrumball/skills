# Request and Response Guide

## `GET /api/v1/audience/instagram/age`
- operationId: `audience_instagram_age`
- summary: 年龄(age)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_Dict_str__str__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/instagram/brand_opportunities`
- operationId: `audience_instagram_brand_opportunities`
- summary: 营销路径(brand opportunities)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
| `X-Language` | `header` | `false` | `string` | 语言代码,支持: ['en', 'zh-CN', 'ja', 'ko'] |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_AudienceBrandOpportunitiesItem_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/instagram/content_style`
- operationId: `audience_instagram_content_style`
- summary: 社交人格(content style)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
| `X-Language` | `header` | `false` | `string` | 语言代码,支持: ['en', 'zh-CN', 'ja', 'ko'] |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_AudienceContentStyleItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/instagram/device`
- operationId: `audience_instagram_device`
- summary: 设备占比(device)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_AudienceDevicePercentageItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/instagram/follower_authenticity`
- operationId: `audience_instagram_follower_authenticity`
- summary: 粉丝真实性(follower authenticity)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_AudienceFollowerAuthenticityRep_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/instagram/gender`
- operationId: `audience_instagram_gender`
- summary: 性别(gender)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_Dict_str__Dict_str__str___ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/instagram/gender_overall`
- operationId: `audience_instagram_gender_overall`
- summary: 整体性别(gender overall)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_Dict_str__str__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/instagram/geography`
- operationId: `audience_instagram_geography`
- summary: 地理位置(geography)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_Dict_str__str__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/instagram/interactive_behavior`
- operationId: `audience_instagram_interactive_behavior`
- summary: 互动行为(interactive behavior)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
| `X-Language` | `header` | `false` | `string` | 语言代码,支持: ['en', 'zh-CN', 'ja', 'ko'] |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_AudienceInteractiveBehaviorItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/instagram/interest`
- operationId: `audience_instagram_interest`
- summary: 兴趣(interest)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
| `X-Language` | `header` | `false` | `string` | 语言代码,支持: ['en', 'zh-CN', 'ja', 'ko'] |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_AudienceInterestItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/instagram/language`
- operationId: `audience_instagram_language`
- summary: 语言(language)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_Dict_str__str__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/instagram/rating_tier`
- operationId: `audience_instagram_rating_tier`
- summary: 评级等级(rating tier)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `username` | `query` | `true` | `string` | username |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_AudienceRatingTierRep_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/tiktok/age`
- operationId: `audience_tiktok_age`
- summary: 年龄(age)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_Dict_str__str__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/tiktok/brand_opportunities`
- operationId: `audience_tiktok_brand_opportunities`
- summary: 营销路径(brand opportunities)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
| `X-Language` | `header` | `false` | `string` | 语言代码,支持: ['en', 'zh-CN', 'ja', 'ko'] |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_AudienceBrandOpportunitiesItem_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/tiktok/content_style`
- operationId: `audience_tiktok_content_style`
- summary: 社交人格(content style)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
| `X-Language` | `header` | `false` | `string` | 语言代码,支持: ['en', 'zh-CN', 'ja', 'ko'] |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_AudienceContentStyleItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/tiktok/device`
- operationId: `audience_tiktok_device`
- summary: 设备占比(device)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_AudienceDevicePercentageItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/tiktok/follower_authenticity`
- operationId: `audience_tiktok_follower_authenticity`
- summary: 粉丝真实性(follower authenticity)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_AudienceFollowerAuthenticityRep_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/tiktok/gender`
- operationId: `audience_tiktok_gender`
- summary: 性别(gender)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_Dict_str__Dict_str__str___ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/tiktok/gender_overall`
- operationId: `audience_tiktok_gender_overall`
- summary: 整体性别(gender overall)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_Dict_str__str__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/tiktok/geography`
- operationId: `audience_tiktok_geography`
- summary: 地理位置(geography)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_Dict_str__str__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/tiktok/interactive_behavior`
- operationId: `audience_tiktok_interactive_behavior`
- summary: 互动行为(interactive behavior)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
| `X-Language` | `header` | `false` | `string` | 语言代码,支持: ['en', 'zh-CN', 'ja', 'ko'] |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_AudienceInteractiveBehaviorItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/tiktok/interest`
- operationId: `audience_tiktok_interest`
- summary: 兴趣(interest)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
| `X-Language` | `header` | `false` | `string` | 语言代码,支持: ['en', 'zh-CN', 'ja', 'ko'] |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_AudienceInterestItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/tiktok/language`
- operationId: `audience_tiktok_language`
- summary: 语言(language)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_Dict_str__str__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/tiktok/rating_tier`
- operationId: `audience_tiktok_rating_tier`
- summary: 评级等级(rating tier)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_AudienceRatingTierRep_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/youtube/age`
- operationId: `audience_youtube_age`
- summary: 年龄(age)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `true` | `string` | 频道ID |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_Dict_str__str__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/youtube/brand_opportunities`
- operationId: `audience_youtube_brand_opportunities`
- summary: 营销路径(brand opportunities)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `true` | `string` | 频道ID |
| `X-Language` | `header` | `false` | `string` | 语言代码,支持: ['en', 'zh-CN', 'ja', 'ko'] |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_AudienceBrandOpportunitiesItem_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/youtube/content_style`
- operationId: `audience_youtube_content_style`
- summary: 社交人格(content style)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `true` | `string` | 频道ID |
| `X-Language` | `header` | `false` | `string` | 语言代码,支持: ['en', 'zh-CN', 'ja', 'ko'] |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_AudienceContentStyleItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/youtube/follower_authenticity`
- operationId: `audience_youtube_follower_authenticity`
- summary: 粉丝真实性(follower authenticity)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `true` | `string` | 频道ID |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_AudienceFollowerAuthenticityRep_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/youtube/gender`
- operationId: `audience_youtube_gender`
- summary: 性别(gender)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `true` | `string` | 频道ID |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_Dict_str__Dict_str__str___ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/youtube/gender_overall`
- operationId: `audience_youtube_gender_overall`
- summary: 整体性别(gender overall)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `true` | `string` | 频道ID |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_Dict_str__str__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/youtube/geography`
- operationId: `audience_youtube_geography`
- summary: 地理位置(geography)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `true` | `string` | 频道ID |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_Dict_str__str__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/youtube/interactive_behavior`
- operationId: `audience_youtube_interactive_behavior`
- summary: 互动行为(interactive behavior)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `true` | `string` | 频道ID |
| `X-Language` | `header` | `false` | `string` | 语言代码,支持: ['en', 'zh-CN', 'ja', 'ko'] |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_AudienceInteractiveBehaviorItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/youtube/interest`
- operationId: `audience_youtube_interest`
- summary: 兴趣(interest)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `true` | `string` | 频道ID |
| `X-Language` | `header` | `false` | `string` | 语言代码,支持: ['en', 'zh-CN', 'ja', 'ko'] |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_list_AudienceInterestItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/youtube/language`
- operationId: `audience_youtube_language`
- summary: 语言(language)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `true` | `string` | 频道ID |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_Dict_str__str__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/audience/youtube/rating_tier`
- operationId: `audience_youtube_rating_tier`
- summary: 评级等级(rating tier)
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `channel_id` | `query` | `true` | `string` | 频道ID |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_AudienceRatingTierRep_ |
| `422` | application/json: HTTPValidationError |
