# Tags Endpoints
Last Updated: 4/6/2023

Labelling tags endpoints here

## `GET /tags`
Returns all tags.

### Parameters
None

### Response
```json
{
  "success": true,
  "data": [
    {
      "challenge": 0,
      "value": "string",
      "challenge_id": 0,
      "id": 0
    }
  ]
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `challenge` | `int` | The ID of the challenge the tag is attached to. |
| `value` | `string` | The tag's value. |
| `challenge_id` | `int` | The ID of the challenge the tag is attached to. (Same value as `challenge`) |
| `id` | `int` | The tag's ID. |


## `POST /tags`
Creates a new tag.

### Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `challenge` | `int` | The ID of the challenge the tag is attached to. |
| `value` | `string` | The tag's value. |

### Response
```json
{
  "success": true,
  "data": {
    "challenge": 0,
    "value": "string",
    "challenge_id": 0,
    "id": 0
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `challenge` | `int` | The ID of the challenge the tag is attached to. |
| `value` | `string` | The tag's value. |
| `challenge_id` | `int` | The ID of the challenge the tag is attached to. (Same value as `challenge`) |
| `id` | `int` | The tag's ID. |


## `GET /tags/<int:tag_id>`
Gets a tag by ID.

### Parameters
None

### Response
```json
{
  "success": true,
  "data": {
    "challenge": 0,
    "value": "string",
    "challenge_id": 0,
    "id": 0
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `challenge` | `int` | The ID of the challenge the tag is attached to. |
| `value` | `string` | The tag's value. |
| `challenge_id` | `int` | The ID of the challenge the tag is attached to. (Same value as `challenge`) |
| `id` | `int` | The tag's ID. |


## `PATCH /tags/<int:tag_id>`
Updates a tag by ID.

### Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `challenge` | `int` | The ID of the challenge the tag is attached to. (Optional) |
| `value` | `string` | The tag's value. (Optional) |
| `challenge_id` | `int` | The ID of the challenge the tag is attached to. (Same value as `challenge`) (Optional) |

### Response
```json
{
  "success": true,
  "data": {
    "challenge": 0,
    "value": "string",
    "challenge_id": 0,
    "id": 0
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `challenge` | `int` | The ID of the challenge the tag is attached to. |
| `value` | `string` | The tag's value. |
| `challenge_id` | `int` | The ID of the challenge the tag is attached to. (Same value as `challenge`) |
| `id` | `int` | The tag's ID. |


## `DELETE /tags/<int:tag_id>`
Deletes a tag by ID.

### Parameters
None

### Response
```json
{
  "success": true
}
```