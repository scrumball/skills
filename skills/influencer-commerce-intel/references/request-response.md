# Request and Response Guide

## `GET /api/v1/tiktok/realtime/product/detail`
- operationId: `tiktok_realtime_product_detail`
- summary: 实时采集-商品详情
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `product_id` | `query` | `true` | `string` | 视频ID |
| `region` | `query` | `true` | `string` | country code:US,VN... |
| `user_id` | `query` | `false` | `string` | tiktok user id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_dict_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/tiktok/user/shop/goods/list`
- operationId: `tiktok_user_shop_goods_list`
- summary: 用户带货商品列表
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
| `page` | `query` | `false` | `integer` | 页码 |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_BasePage_TiktokUserShopGoodsItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/tiktok/user/shop/live/list`
- operationId: `tiktok_user_shop_live_list`
- summary: 用户带货直播列表
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
| `sort_field` | `query` | `false` | `string` | 排序字段，live_revenue_amount, live_view_count, live_price, live_revenue_per_thousand |
| `sort_type` | `query` | `false` | `string` | 排序类型, asc:升序, desc:降序 |
| `page` | `query` | `false` | `integer` | 页码 |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_BasePage_TiktokUserShopLiveItem__ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/tiktok/user/shop/sale`
- operationId: `tiktok_user_shop_sale`
- summary: 用户带货数据
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_TiktokUserShopSaleRes_ |
| `422` | application/json: HTTPValidationError |

## `GET /api/v1/tiktok/user/shop/video/ad/list`
- operationId: `tiktok_user_shop_video_ad_list`
- summary: 用户带货视频广告列表
- parameters:
| name | in | required | schema | description |
|---|---|---|---|---|
| `unique_id` | `query` | `true` | `string` | unique_id |
| `sort_field` | `query` | `false` | `string` | 排序字段，revenue_amount, views_count, ads_deal_rate, ads_view_rate, ads_roas_rate |
| `sort_type` | `query` | `false` | `string` | 排序类型, asc:升序, desc:降序 |
| `page` | `query` | `false` | `integer` | 页码 |
- requestBody: none
- responses:
| status | schema hints |
|---|---|
| `200` | application/json: ResponseModel_BasePage_TiktokUserShopVideoAdItem__ |
| `422` | application/json: HTTPValidationError |
