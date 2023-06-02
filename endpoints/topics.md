# Topic Endpoints

## `GET /topics`
Returns a list of all topics.

### Query Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `field` | `string` | The field to search for. This can only be `value` |
| `q` | `string` | The query to search for. |

### Response
```json
{
  "success": true,
  "data": [
    {
      "value": "string",
      "id": 0
    }
  ]
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The topic's ID. |
| `value` | `string` | The topic's value. |

Note: You can search for possible topics by a substring by using the query:
`/topics?field=value&q=<substring>`
This is used internally for autocomplete.


## `POST /topics`
Creates a new topic.

### Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `challenge` | `int` | The challenge's ID. |
| `type` | `string` | Not too sure, seems to always be `challenge` |
| `value` | `string` | The topic's value. |

### Response
```json
{
  "success": true,
  "data": {
    "id": 7,
    "challenge": 1,
    "topic_id": 2,
    "challenge_id": 1,
    "topic": 2
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The topic's unique ID. |
| `challenge` | `int` | The challenge's ID. |
| `challenge_id` | `int` | The challenge's ID. (Exactly the same as `challenge`) |
| `topic_id` | `int` | The topic's ID. |
| `topic` | `int` | The topic's ID. (Exactly the same as `topic_id`) |


## `DELETE /topics`
Deletes a topic from a challenge.

### Query Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `type` | `string` | Not too sure, seems to always be `challenge` |
| `target_id` | `int` | The unique ID of the topic to delete. |

### Response
```json
{
  "success": true
}
```


## `GET /topics/<int:topic_id>`
Gets a topic by ID.

Note: This uses the _topic_ ID, not the unique ID assigned to every topic for each challenge

### Parameters
None

### Response
```json
{
  "success": true,
  "data": {
    "value": "string",
    "id": 0
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `id` | `int` | The topic's ID. |
| `value` | `string` | The topic's value. |


## `DELETE /topics/<int:topic_id>`
Deletes a topic.

Note: This uses the _topic_ ID, not the unique ID assigned to every topic for each challenge

This also means that this deletes this topic from every challenge it is in.

### Parameters
None

### Response
```json
{
  "success": true
}
```