# Challenges Endpoints

Labelling challenge endpoints here

## `GET /challenges`
Returns all visible challenges.

### Parameters
None

### Response
```json
{
  "success": true,
  "data": [
    {
      "id": 0,
      "type": "string",
      "name": "string",
      "value": 0,
      "solves": 0,
      "solved_by_me": false,
      "category": "string",
      "tags": [ ],
      "template": "string",
      "script": "string",
    },
  ]
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The challenge's ID. |
| `type` | `string` | The challenge's type. Is either `standard`, `dynamic` or `hidden`. (Hidden challenges are a special type of challenge that is caused by a challenge requiring another challenge to be solved first. There should be no other place where this appears.) |
| `name` | `string` | The challenge's name. |
| `value` | `int` | The challenge's current value. |
| `solves` | `int` | The number of solves for the challenge. |
| `solved_by_me` | `bool` | Whether or not the current user has solved the challenge. |
| `category` | `string` | The challenge's category. |
| `tags` | `list` | A list of tags. |
| `template` | `string` | (You do not need to worry about this) |
| `script` | `string` | (You do not need to worry about this) |

NOTE: If you want to get all challenges (including hidden challenges), use `GET /challenges?view=admin` instead.


## `GET /challenges/<int:challenge_id>`
Gets a challenge by ID.

### Parameters
None

### Response
```json
{
  "success": true,
  "data": {
    "id": 0,
    "name": "string",
    "value": 0,
    "initial": 0,
    "decay": 0,
    "minimum": 0,
    "description": "string",
    "connection_info": "string",
    "next_id": 0,
    "category": "string",
    "state": "string",
    "max_attempts": 0,
    "type": "string",
    "type_data": { },
    "solves": 0,
    "solved_by_me": false,
    "attempts": 0,
    "files": [
      "string",
    ],
    "tags": [ ],
    "hints": [{ }],
    "view": "string"
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The challenge's ID. |
| `name` | `string` | The challenge's name. |
| `value` | `int` | The challenge's current value. |
| `initial` | `int` | The challenge's initial value. (For dynamic challenges only) |
| `decay` | `int` | The challenge's decay value. (For dynamic challenges only) |
| `minimum` | `int` | The challenge's minimum value. (For dynamic challenges only) |
| `description` | `string` | The challenge's description. |
| `connection_info` | `string` | The challenge's connection info. (Optional) |
| `next_id` | `int` | The challenge's next ID. (Optional) (For standard challenges only, this seems to be a bug) |
| `category` | `string` | The challenge's category. |
| `state` | `string` | The challenge's state. Is either `visible` or `hidden`. |
| `max_attempts` | `int` | The challenge's maximum number of attempts. |
| `type` | `string` | The challenge's type. Is either `standard` or `dynamic`. |
| `type_data` | `dict` | The challenge's type data. (You do not need to worry about this) |
| `solves` | `int` | The number of solves for the challenge. |
| `solved_by_me` | `bool` | Whether or not the current user has solved the challenge. |
| `attempts` | `int` | The number of attempts for the challenge. |
| `files` | `list` | A list of endpoints to files for the challenge. (Optional) |
| `tags` | `list` | A list of tags. (Optional) |
| `hints` | `list` | A list of dictionaries containing hints. (Optional) |
| `view` | `string` | The challenge's HTML modal view. (The thing that pops up when you click on a challenge) (You do not need to worry about this) |


## `POST /challenges/<int:challenge_id>`
Creates a new challenge.

### Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `name` | `string` | The challenge's name. |
| `category` | `string` | The challenge's category. |
| `description` | `string` | The challenge's description. |
| `value` | `int` | The challenge's value. |
| `initial` | `int` | The challenge's initial value. (For dynamic challenges only) |
| `decay` | `int` | The challenge's decay value. (For dynamic challenges only) |
| `minimum` | `int` | The challenge's minimum value. (For dynamic challenges only) |
| `state` | `string` | The challenge's state. Is either `visible` or `hidden`. (Optional) |
| `type` | `string` | The challenge's type. Is either `standard` or `dynamic`. |


### Response
```json
{
  "success": true,
  "data": {
    "id": 0,
    "name": "string",
    "value": 0,
    "initial": 0,
    "decay": 0,
    "minimum": 0,
    "description": "string",
    "connection_info": "string",
    "next_id": 0,
    "category": "string",
    "state": "string",
    "max_attempts": 0,
    "type": "string",
    "type_data": { }
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The challenge's ID. |
| `name` | `string` | The challenge's name. |
| `value` | `int` | The challenge's current value. |
| `initial` | `int` | The challenge's initial value. (For dynamic challenges only) |
| `decay` | `int` | The challenge's decay value. (For dynamic challenges only) |
| `minimum` | `int` | The challenge's minimum value. (For dynamic challenges only) |
| `description` | `string` | The challenge's description. |
| `connection_info` | `string` | The challenge's connection info. (Optional) |
| `next_id` | `int` | The challenge's next ID. (Optional) (For standard challenges only, this seems to be a bug) |
| `category` | `string` | The challenge's category. |
| `state` | `string` | The challenge's state. Is either `visible` or `hidden`. |
| `max_attempts` | `int` | The challenge's maximum number of attempts. |
| `type` | `string` | The challenge's type. Is either `standard` or `dynamic`. |
| `type_data` | `dict` | The challenge's type data. (You do not need to worry about this) |


## `PATCH /challenges/<int:challenge_id>`
Updates a challenge.

### Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `name` | `string` | The challenge's name. (Optional) |
| `category` | `string` | The challenge's category. (Optional) |
| `description` | `string` | The challenge's description. (Optional) |
| `connection_info` | `string` | The challenge's connection info. (Optional) |
| `value` | `int` | The challenge's value. (Optional) (For standard challenges only) |
| `initial` | `int` | The challenge's initial value. (For dynamic challenges only) (Optional) |
| `decay` | `int` | The challenge's decay value. (For dynamic challenges only) (Optional) |
| `minimum` | `int` | The challenge's minimum value. (For dynamic challenges only) (Optional) |
| `max_attempts` | `int` | The challenge's maximum number of attempts. (Optional) |
| `state` | `string` | The challenge's state. Is either `visible` or `hidden`. (Optional) |


### Response
```json
{
  "success": true,
  "data": {
    "id": 0,
    "name": "string",
    "value": 0,
    "initial": 0,
    "decay": 0,
    "minimum": 0,
    "description": "test",
    "connection_info": null,
    "next_id": 0,
    "category": "string",
    "state": "visible",
    "max_attempts": 0,
    "type": "standard",
    "type_data": { }
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The challenge's ID. |
| `name` | `string` | The challenge's name. |
| `value` | `int` | The challenge's current value. |
| `initial` | `int` | The challenge's initial value. (For dynamic challenges only) |
| `decay` | `int` | The challenge's decay value. (For dynamic challenges only) |
| `minimum` | `int` | The challenge's minimum value. (For dynamic challenges only) |
| `description` | `string` | The challenge's description. |
| `connection_info` | `string` | The challenge's connection info. (Optional) |
| `next_id` | `int` | The challenge's next ID. (Optional) (For standard challenges only, this seems to be a bug) |
| `category` | `string` | The challenge's category. |
| `state` | `string` | The challenge's state. Is either `visible` or `hidden`. |
| `max_attempts` | `int` | The challenge's maximum number of attempts. |
| `type` | `string` | The challenge's type. Is either `standard` or `dynamic`. |
| `type_data` | `dict` | The challenge's type data. (You do not need to worry about this) |


## `DELETE /challenges/<int:challenge_id>`
Deletes a challenge.

### Parameters
None

### Response
```json
{
  "success": true
}
```

## `GET /challenges/<int:challenge_id>/files`
Gets a challenge's files.

### Parameters
None

### Response
```json
{
  "success": true,
  "data": [
    {
      "id": 0,
      "type": "string",
      "location": "string"
    }
  ]
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The file's ID. |
| `type` | `string` | The file's type. Not exactly documented, seems to always be `challenge` |
| `location` | `string` | The file's location. |


# `GET /challenges/<int:challenge_id>/flags`
Gets a challenge's flags.

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


## `GET /challenges/<int:challenge_id>/hints`
Gets a challenge's hints.

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
      "challenge_id": 0,
      "cost": 0,
      "requirements": {
        "prerequisites": [
          0
        ]
      },
      "content": "string"
    }
  ]
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


## `GET /challenges/<int:challenge_id>/requirements`
Gets a challenge's requirements.

### Parameters
None

### Response
```json
{
  "success": true,
  "data": {
    "prerequisites": [
      0
    ]
  }  
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `prerequisites` | `list` | A list of prerequisite challenge IDs. |


## `GET /challenges/<int:challenge_id>/solves`
TODO


## `GET /challenges/<int:challenge_id>/tags`
Gets a challenge's tags.

### Parameters
None

### Response
```json
{
  "success": true,
  "data": [
    {
      "id": 0,
      "challenge_id": 0,
      "value": "string"
    }
  ]
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The tag's ID. |
| `challenge_id` | `int` | The ID of the challenge the tag is attached to. |
| `value` | `string` | The tag's value. |


## `GET /challenges/<int:challenge_id>/topics`
Gets a challenge's topics.

### Parameters
None

### Response
```json
{
  "success": true,
  "data": [
    {
      "id": 6,
      "challenge_id": 1,
      "topic_id": 1,
      "value": "string"
    }
  ]
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The topic's unique ID. This is generated for each topic in a challenge. |
| `challenge_id` | `int` | The challenge's ID. |
| `topic_id` | `int` | The topic's ID based on the topic's string. |
| `value` | `string` | The topic string. |
