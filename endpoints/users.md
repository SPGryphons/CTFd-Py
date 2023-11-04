# Users Endpoints
Last Updated: 5/11/2023

## `GET /users`
Returns all visible users.

### Parameters
None

### Response
```json
{
  "success": true,
  "data": [
    {
      "country": "string",
      "bracket": null,
      "affiliation": null,
      "fields": [ ],
      "website": "string",
      "oauth_id": null,
      "team_id": 0,
      "id": 0,
      "name": "string"
    },
  ]
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `country` | `string` | The country of the user. |
| `bracket` | `string` | The bracket of the user. |
| `affiliation` | `string` | The affiliation of the user. |
| `fields` | `list` | Additional information about the user. This is dependent on your CTFd settings. |
| `website` | `string` | The website of the user. |
| `oauth_id` | `string` | The OAuth ID of the user. |
| `team_id` | `int` | The ID of the team the user is on. (Only when Teams mode is enabled) |
| `id` | `int` | The ID of the user. |
| `name` | `string` | The name of the user. |

NOTE: If you want to get all users (including hidden users) you can use `GET /users?view=admin` instead.


## `POST /users`
Creates a new user.

### Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `name` | `string` | The name of the user. |
| `email` | `string` | The email of the user. |
| `password` | `string` | The password of the user. |
| `website` | `string` | The website of the user. (Optional) |
| `affiliation` | `string` | The affiliation of the user. (Optional) |
| `country` | `string` | The country of the user. (Optional) |
| `type` | `string` | The type of the user. |
| `verified` | `bool` | Whether the user is verified. |
| `hidden` | `bool` | Whether the user is hidden. |
| `banned` | `bool` | Whether the user is banned. |
| `fields` | `list` | Additional information about the user. This is dependent on your CTFd settings. |

### Response
```json
{
  "success": true,
  "data": {
    "id": 0,
    "oauth_id": 0,
    "name": "string",
    "email": "string",
    "type": "string",
    "secret": "string",
    "website": "string",
    "affiliation": "string",
    "country": "string",
    "bracket": "string",
    "hidden": true,
    "banned": true,
    "verified": true,
    "language": "string",
    "team_id": 0,
    "created": "string"
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The ID of the user. |
| `oauth_id` | `int` | The OAuth ID of the user. |
| `name` | `string` | The name of the user. |
| `password` | `string` | The password of the user. |
| `email` | `string` | The email of the user. |
| `type` | `string` | The type of the user. |
| `secret` | `string` | The secret of the user. |
| `website` | `string` | The website of the user. |
| `affiliation` | `string` | The affiliation of the user. |
| `country` | `string` | The country of the user. |
| `bracket` | `string` | The bracket of the user. |
| `hidden` | `bool` | Whether the user is hidden. |
| `banned` | `bool` | Whether the user is banned. |
| `verified` | `bool` | Whether the user is verified. |
| `language` | `string` | The language of the user. |
| `team_id` | `int` | The ID of the team the user is on. (Only when Teams mode is enabled) |
| `created` | `string` | The date the user was created. |


## `GET /users/<int:user_id>`
Get a user by ID

### Parameters
None

### Response
```json
{
  "success": true,
  "data": {
    "email": "string",
    "fields": [ ],
    "type": "string",
    "oauth_id": 0,
    "secret": "string",
    "team_id": 0,
    "language": null,
    "id": 0,
    "created": "string",
    "name": "string",
    "country": "string",
    "affiliation": "string",
    "bracket": null,
    "website": "string",
    "banned": true,
    "verified": true,
    "hidden": true,
    "place": "string",
    "score": 0
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `email` | `string` | The email of the user. |
| `fields` | `list` | Additional information about the user. This is dependent on your CTFd settings. |
| `type` | `string` | The type of the user. Either `user` or `admin` |
| `oauth_id` | `int` | The OAuth ID of the user. |
| `secret` | `string` | The secret of the user. |
| `team_id` | `int` | The ID of the team the user is on. (Only when Teams mode is enabled) |
| `language` | `string` | The language of the user. |
| `id` | `int` | The ID of the user. |
| `created` | `string` | The date the user was created. |
| `name` | `string` | The name of the user. |
| `country` | `string` | The country of the user. |
| `affiliation` | `string` | The affiliation of the user. |
| `bracket` | `string` | The bracket of the user. |
| `website` | `string` | The website of the user. |
| `banned` | `bool` | Whether the user is banned. |
| `verified` | `bool` | Whether the user is verified. |
| `hidden` | `bool` | Whether the user is hidden. |
| `place` | `string` | The place of the user. |
| `score` | `int` | The score of the user. |


## `PATCH /users/<int:user_id>`
Edits a user.

### Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `name` | `string` | The name of the user. |
| `email` | `string` | The email of the user. |
| `password` | `string` | The password of the user. |
| `website` | `string` | The website of the user. |
| `affiliation` | `string` | The affiliation of the user. |
| `country` | `string` | The country of the user. |
| `type` | `string` | The type of the user. |
| `verified` | `bool` | Whether the user is verified. |
| `hidden` | `bool` | Whether the user is hidden. |
| `banned` | `bool` | Whether the user is banned. |
| `fields` | `list` | Additional information about the user. This is dependent on your CTFd settings. |

### Response
None


## `DELETE /users/<int:user_id>`
Deletes a user.

### Parameters
None

### Response
```json
{
  "success": true
}
```