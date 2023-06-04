# Flag Endpoints

Labelling flag endpoints here

## `GET /flags`
Get all flags

### Parameters
None

### Response
```json
{
  "success": true,
  "data": [
    {
      "id": 0,
      "challenge": 0,
      "type": "string",
      "data": "string",
      "challenge_id": 0,
      "content": "string"
    }
  ]
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The flag's ID. |
| `challenge` | `int` | The ID of the challenge the flag is attached to. |
| `type` | `string` | The flag's type. This is either `static` or `regex` |
| `data` | `string` | The flag's data. This seems to only be used for case-sensitivity. When it is case-insensitive, this is set to `case_insensitive`, else it is just an empty string. |
| `challenge_id` | `int` | The ID of the challenge the flag is attached to. (Same value as `challenge`) |
| `content` | `string` | The flag's content. |


## `POST /flags`
Create a new flag

### Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `challenge_id` | `int` | The ID of the challenge the flag is attached to. |
| `type` | `string` | The flag's type. This is either `static` or `regex` |
| `data` | `string` | The flag's data. This seems to only be used for case-sensitivity. When it is case-insensitive, this is set to `case_insensitive`, else it is just an empty string. |
| `content` | `string` | The flag's content. |

### Response
```json
{
  "success": true,
  "data": {
    "id": 0,
    "challenge": 0,
    "type": "string",
    "data": "string",
    "challenge_id": 0,
    "content": "string"
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The flag's ID. |
| `challenge` | `int` | The ID of the challenge the flag is attached to. |
| `type` | `string` | The flag's type. This is either `static` or `regex` |
| `data` | `string` | The flag's data. This seems to only be used for case-sensitivity. When it is case-insensitive, this is set to `case_insensitive`, else it is just an empty string. |
| `challenge_id` | `int` | The ID of the challenge the flag is attached to. (Same value as `challenge`) |
| `content` | `string` | The flag's content. |


## `GET /flags/<int:flag_id>`
Get a specific flag

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
    "data": "string",
    "challenge_id": 0,
    "content": "string"
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The flag's ID. |
| `challenge` | `int` | The ID of the challenge the flag is attached to. |
| `type` | `string` | The flag's type. This is either `static` or `regex` |
| `data` | `string` | The flag's data. This seems to only be used for case-sensitivity. When it is case-insensitive, this is set to `case_insensitive`, else it is just an empty string. |
| `challenge_id` | `int` | The ID of the challenge the flag is attached to. (Same value as `challenge`) |
| `content` | `string` | The flag's content. |


## `PATCH /flags/<int:flag_id>`
Update a specific flag

### Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `type` | `string` | The flag's type. This is either `static` or `regex` |
| `data` | `string` | The flag's data. This seems to only be used for case-sensitivity. When it is case-insensitive, this is set to `case_insensitive`, else it is just an empty string. |
| `content` | `string` | The flag's content. |

### Response
```json
{
  "success": true,
  "data": {
    "id": 0,
    "challenge": 0,
    "type": "string",
    "data": "string",
    "challenge_id": 0,
    "content": "string"
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The flag's ID. |
| `challenge` | `int` | The ID of the challenge the flag is attached to. |
| `type` | `string` | The flag's type. This is either `static` or `regex` |
| `data` | `string` | The flag's data. This seems to only be used for case-sensitivity. When it is case-insensitive, this is set to `case_insensitive`, else it is just an empty string. |
| `challenge_id` | `int` | The ID of the challenge the flag is attached to. (Same value as `challenge`) |
| `content` | `string` | The flag's content. |


## `DELETE /flags/<int:flag_id>`
Delete a specific flag

### Parameters
None

### Response
```json
{
  "success": true
}
```

### Return Values
None


## `GET /flags/types`
Get all flag types

This endpoint is undocumented here, because it is really only meant to be used by the frontend.


## `GET /flags/types/<str:type_name>`
Get a specific flag type

This endpoint is undocumented here, because it is really only meant to be used by the frontend.