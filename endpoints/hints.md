# Hints Endpoints
Last Updated: 11/6/2023

Labelling hints endpoints here

## `GET /hints`
Get all hints

### Parameters
None

### Response
```json
{
  "success": true,
  "data": [
    {
      "cost": 0,
      "id": 0,
      "challenge_id": 0,
      "challenge": 0,
      "type": "string"
    }
  ]
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `cost` | `int` | The cost of the hint. |
| `id` | `int` | The hint's ID. |
| `challenge_id` | `int` | The ID of the challenge the hint is attached to. (Same value as `challenge`) |
| `challenge` | `int` | The ID of the challenge the hint is attached to. |
| `type` | `string` | The hint's type. (This seems to be unused, will always be `standard`) |


## `POST /hints`
Create a new hint

### Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `challenge_id` | `int` | The ID of the challenge the hint is attached to. |
| `cost` | `int` | The cost of the hint. |
| `content` | `string` | The hint's content. |
| `requirements` | `dict` | The hint's requirements. This dictionary has a single item, `prerequisites`, which is a list of hint IDs required to unlock before this one. (Optional) |

### Response
```json
{
  "success": true,
  "data": {
    "id": 0,
    "challenge": 0,
    "type": "string",
    "challenge_id": 0,
    "cost": 0,
    "requirements": {
      "prerequisites": [
        0
      ]
    },
    "content": "string",
    "html": "string"
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The hint's ID. |
| `challenge` | `int` | The ID of the challenge the hint is attached to. |
| `type` | `string` | The hint's type. (This seems to be unused, will always be `standard`) |
| `challenge_id` | `int` | The ID of the challenge the hint is attached to. (Same value as `challenge`) |
| `cost` | `int` | The cost of the hint. |
| `requirements` | `dict` | The hint's requirements. This dictionary has a single item, `prerequisites`, which is a list of hint IDs required to unlock before this one. (Optional) |
| `content` | `string` | The hint's content. |
| `html` | `string` | The hint's content, with HTML formatting. (You can ignore this) |


## `GET /hints/<int:hint_id>`
Get a hint by ID.

### Parameters
None

### Response
```json
{
  "success": true,
  "data": {
    "id": 0,
    "challenge": 0,
    "type": "string",
    "challenge_id": 0,
    "cost": 0,
    "requirements": {
      "prerequisites": [
        0
      ]
    },
    "content": "string",
    "html": "string"
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The hint's ID. |
| `challenge` | `int` | The ID of the challenge the hint is attached to. |
| `type` | `string` | The hint's type. (This seems to be unused, will always be `standard`) |
| `challenge_id` | `int` | The ID of the challenge the hint is attached to. (Same value as `challenge`) |
| `cost` | `int` | The cost of the hint. |
| `requirements` | `dict` | The hint's requirements. This dictionary has a single item, `prerequisites`, which is a list of hint IDs required to unlock before this one. (Optional) |
| `content` | `string` | The hint's content. |
| `html` | `string` | The hint's content, with HTML formatting. (You can ignore this) |


## `PATCH /hints/<int:hint_id>`
Update a hint by ID.

### Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `challenge_id` | `int` | The ID of the challenge the hint is attached to. |
| `cost` | `int` | The cost of the hint. |
| `content` | `string` | The hint's content. |
| `requirements` | `dict` | The hint's requirements. This dictionary has a single item, `prerequisites`, which is a list of hint IDs required to unlock before this one. (Optional) |

### Response
```json
{
  "success": true,
  "data": {
    "id": 0,
    "challenge": 0,
    "type": "string",
    "challenge_id": 0,
    "cost": 0,
    "requirements": {
      "prerequisites": [
        0
      ]
    },
    "content": "string",
    "html": "string"
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The hint's ID. |
| `challenge` | `int` | The ID of the challenge the hint is attached to. |
| `type` | `string` | The hint's type. (This seems to be unused, will always be `standard`) |
| `challenge_id` | `int` | The ID of the challenge the hint is attached to. (Same value as `challenge`) |
| `cost` | `int` | The cost of the hint. |
| `requirements` | `dict` | The hint's requirements. This dictionary has a single item, `prerequisites`, which is a list of hint IDs required to unlock before this one. (Optional) |
| `content` | `string` | The hint's content. |
| `html` | `string` | The hint's content, with HTML formatting. (You can ignore this) |