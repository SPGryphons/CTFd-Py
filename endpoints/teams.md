# Teams Endpoints
Last Updated: 5/11/2023

## `GET /teams`
Returns all visible teams.

### Parameters
None

### Response
```json
{
  "success": true,
  "data": [
    {
      "email": "string",
      "captain_id": 0,
      "country": "string",
      "affiliation": "string",
      "bracket": "string",
      "id": 0,
      "website": "string",
      "fields": [ ],
      "banned": false,
      "oauth_id": 0,
      "secret": "string",
      "created": "string",
      "name": "string",
      "hidden": false
    },
  ]
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `email` | `string` | The email of the team. |
| `captain_id` | `int` | The ID of the captain of the team. |
| `country` | `string` | The country of the team. |
| `affiliation` | `string` | The affiliation of the team. |
| `bracket` | `string` | The bracket of the team. |
| `id` | `int` | The ID of the team. |
| `website` | `string` | The website of the team. |
| `fields` | `array` | Additional information about the team. This is dependent on your CTFd settings. |
| `banned` | `bool` | Whether the team is banned. |
| `oauth_id` | `int` | The OAuth ID of the team. |
| `secret` | `string` | The secret of the team. |
| `created` | `string` | The date the team was created. |
| `name` | `string` | The name of the team. |
| `hidden` | `bool` | Whether the team is hidden. |

NOTE: If you want to get all teams (including hidden teams) you can use `GET /teams?view=admin` instead.


## `POST /teams`
Create a new team.

### Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `name` | `string` | The name of the team. |
| `email` | `string` | The email of the team. (Optional) |
| `password` | `string` | The password of the team. |
| `website` | `string` | The website of the team. (Optional) |
| `affiliation` | `string` | The affiliation of the team. (Optional) |
| `country` | `string` | The country of the team. (Optional) |
| `hidden` | `bool` | Whether the team is hidden. |
| `banned` | `bool` | Whether the team is banned. |
| `fields` | `list` | Additional information about the team. This is dependent on your CTFd settings. |

### Response
```json
{
  "success": true,
  "data": {
    "id": 0,
    "oauth_id": 0,
    "name": "string",
    "email": "string",
    "password": "string",
    "secret": "string",
    "website": "string",
    "affiliation": "string",
    "country": "string",
    "bracket": "string",
    "hidden": true,
    "banned": true,
    "captain_id": 0,
    "created": "string"
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The ID of the team. |
| `oauth_id` | `int` | The OAuth ID of the team. |
| `name` | `string` | The name of the team. |
| `email` | `string` | The email of the team. |
| `password` | `string` | The password of the team. |
| `secret` | `string` | The secret of the team. |
| `website` | `string` | The website of the team. |
| `affiliation` | `string` | The affiliation of the team. |
| `country` | `string` | The country of the team. |
| `bracket` | `string` | The bracket of the team. |
| `hidden` | `bool` | Whether the team is hidden. |
| `banned` | `bool` | Whether the team is banned. |
| `captain_id` | `int` | The user ID of the captain of the team. |
| `created` | `string` | The date the team was created. |


## `GET /teams/<team_id>`
Get a specific team.

### Parameters
None

### Response
```json
{
  "success": true,
  "data": {
    "email": "string",
    "fields": [ ],
    "members": [ ],
    "oauth_id": 0,
    "secret": "string",
    "id": 0,
    "created": "string",
    "name": "string",
    "captain_id": 0,
    "country": "string",
    "affiliation": "string",
    "bracket": "string",
    "website": "string",
    "banned": true,
    "hidden": true,
    "place": "string",
    "score": 0
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `email` | `string` | The email of the team. |
| `fields` | `array` | Additional information about the team. This is dependent on your CTFd settings. |
| `members` | `array` | The members of the team. |
| `oauth_id` | `int` | The OAuth ID of the team. |
| `secret` | `string` | The secret of the team. |
| `id` | `int` | The ID of the team. |
| `created` | `string` | The date the team was created. |
| `name` | `string` | The name of the team. |
| `captain_id` | `int` | The user ID of the captain of the team. |
| `country` | `string` | The country of the team. |
| `affiliation` | `string` | The affiliation of the team. |
| `bracket` | `string` | The bracket of the team. |
| `website` | `string` | The website of the team. |
| `banned` | `bool` | Whether the team is banned. |
| `hidden` | `bool` | Whether the team is hidden. |
| `place` | `string` | The place of the team. |
| `score` | `int` | The score of the team. |


## `PATCH /teams/<team_id>`

### Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `name` | `string` | The name of the team. (Optional) |
| `email` | `string` | The email of the team. (Optional) |
| `password` | `string` | The password of the team. |
| `website` | `string` | The website of the team. (Optional) |
| `affiliation` | `string` | The affiliation of the team. (Optional) |
| `country` | `string` | The country of the team. (Optional) |
| `captain_id` | `int` | The ID of the captain of the team. (Optional) |
| `hidden` | `bool` | Whether the team is hidden. (Optional) |
| `banned` | `bool` | Whether the team is banned. (Optional) |
| `fields` | `list` | Additional information about the team. This is dependent on your CTFd settings. |

### Response
```json
{
  "success": true,
  "data": {
    "id": 0,
    "oauth_id": 0,
    "name": "string",
    "email": "string",
    "password": "string",
    "secret": "string",
    "website": "string",
    "affiliation": "string",
    "country": "string",
    "bracket": "string",
    "hidden": true,
    "banned": true,
    "captain_id": 0,
    "created": "string"
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The ID of the team. |
| `oauth_id` | `int` | The OAuth ID of the team. |
| `name` | `string` | The name of the team. |
| `email` | `string` | The email of the team. |
| `password` | `string` | The password of the team. |
| `secret` | `string` | The secret of the team. |
| `website` | `string` | The website of the team. |
| `affiliation` | `string` | The affiliation of the team. |
| `country` | `string` | The country of the team. |
| `bracket` | `string` | The bracket of the team. |
| `hidden` | `bool` | Whether the team is hidden. |
| `banned` | `bool` | Whether the team is banned. |
| `captain_id` | `int` | The user ID of the captain of the team. |
| `created` | `string` | The date the team was created. |


## `DELETE /teams/<team_id>`
Delete a team.

### Parameters
None

### Response
```json
{
  "success": true,
}
```

### Return Values
None


## `GET /teams/<team_id>/members`

### Parameters
None

### Response
```json
{
    "success": true,
    "data": [ ]
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `data` | `list` | A list of user IDs in the team |


## `POST /teams/<team_id>/members`
Add a member to a team.

### Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `user_id` | `int` | The ID of the user to add to the team. |

### Response
```json
{
    "success": true,
    "data": [ ]
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `data` | `list` | A list of user IDs in the team |


## `DELETE /teams/<team_id>/members`
Remove a member from a team.

### Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `user_id` | `string` | The ID of the user to remove from the team. |

### Response
```json
{
    "success": true,
    "data": [ ]
}
```