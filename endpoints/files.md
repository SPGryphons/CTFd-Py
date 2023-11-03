# Files Endpoints
Last Updated: 4/6/2023

Labelling files endpoints here

## `GET /files`
Get all files

### Parameters
None

### Response
```json
{
  "success": true,
  "data": [
    {
      "location": "string",
      "type": "string",
      "id": 0
    }
  ]
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `location` | `string` | The file's location. |
| `type` | `string` | The file's type. Not exactly documented, seems to always be `challenge` |
| `id` | `int` | The file's ID. |


## `POST /files`
Create a new file

### Parameters
| Name | Type | Description |
| ---- | ---- | ----------- |
| `file` | `File` | The file to upload. |
| `challenge_id` | `int` | The ID of the challenge to upload the file to. |
| `type` | `string` | The type of the file. Not exactly documented, seems to always be `challenge` |

**Note: This is not sent with a normal JSON payload, it instead uses the a `multipart/form-data` content type.
Addtionally, I cannot seem to get this endpoint to work with API tokens. However, logging in via `example.ctfd.org/login`, taking the session cookie, and sending the POST request works.**

### Response
```json
{
  "success": true,
  "data": [
    {
      "location": "string",
      "type": "string",
      "id": 0
    }
  ]
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `location` | `string` | The file's location. |
| `type` | `string` | The file's type. Not exactly documented, seems to always be `challenge` |
| `id` | `int` | The file's ID. |

**Note: This only returns the files uploaded in the request, not all files.**


## `GET /files/<int:file_id>`
Get a file

### Parameters
None

### Response
```json
{
  "success": true,
  "data": {
    "location": "string",
    "type": "string",
    "id": 0
  }
}
```

### Return Values
| Name | Type | Description |
| ---- | ---- | ----------- |
| `location` | `string` | The file's location. |
| `type` | `string` | The file's type. Not exactly documented, seems to always be `challenge` |
| `id` | `int` | The file's ID. |


## `DELETE /files/<int:file_id>`
Delete a file

### Parameters
None

### Response
```json
{
  "success": true
}
```