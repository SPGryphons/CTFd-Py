# Challenges Endpoints

Labelling all endpoints here

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
      "tags": [],
      "template": "string",
      "script": "string",
    },
    ...
  ]
}
```

### Return Values
- `id`: The challenge's ID.
- `type`: The challenge's type. Is either `standard`, `dynamic` or `hidden`. (Hidden challenges are a special type of challenge that is caused by a challenge requiring another challenge to be solved first. There should be no other place where this appears.)
- `name`: The challenge's name.
- `value`: The challenge's current value.
- `solves`: The number of solves for the challenge.
- `solved_by_me`: Whether or not the current user has solved the challenge.
- `category`: The challenge's category.
- `tags`: A list of tags.
- `template`: (You do not need to worry about this)
- `script`: (You do not need to worry about this)

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
    "type_data": { ... },
    "solves": 0,
    "solved_by_me": false,
    "attempts": 0,
    "files": [
      "string",
    ],
    "tags": [],
    "hints": [{ ... }],
    "view": "string"
  }
}
```

### Return Values
- `id`: The challenge's ID.
- `name`: The challenge's name.
- `value`: The challenge's current value.
- `initial`: The challenge's initial value. (For dynamic challenges only)
- `decay`: The challenge's decay value. (For dynamic challenges only)
- `minimum`: The challenge's minimum value. (For dynamic challenges only)
- `description`: The challenge's description.
- `connection_info`: The challenge's connection info. (Optional)
- `next_id`: The challenge's next ID. (Optional) (For standard challenges only, this seems to be a bug)
- `category`: The challenge's category.
- `state`: The challenge's state. Is either `visible` or `hidden`.
- `max_attempts`: The challenge's maximum number of attempts.
- `type`: The challenge's type. Is either `standard` or `dynamic`.
- `type_data`: The challenge's type data. (You do not need to worry about this)
- `solves`: The number of solves for the challenge.
- `solved_by_me`: Whether or not the current user has solved the challenge.
- `attempts`: The number of attempts for the challenge.
- `files`: A list of endpoints to files for the challenge. (Optional)
- `tags`: A list of tags. (Optional)
- `hints`: A list of dictionaries containing hints. (Optional)
- `view`: The challenge's HTML modal view. (The thing that pops up when you click on a challenge) (You do not need to worry about this)


## `POST /challenges/<int:challenge_id>`
Creates a new challenge.

### Parameters
- `name`: The challenge's name.
- `category`: The challenge's category.
- `description`: The challenge's description.
- `value`: The challenge's value.
- `initial`: The challenge's initial value. (For dynamic challenges only)
- `decay`: The challenge's decay value. (For dynamic challenges only)
- `minimum`: The challenge's minimum value. (For dynamic challenges only)
- `state`: The challenge's state. Is either `visible` or `hidden`. (Optional)
- `type`: The challenge's type. Is either `standard` or `dynamic`.

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
    "type_data": { ... }
  }
}
```

### Return Values
- `id`: The challenge's ID.
- `name`: The challenge's name.
- `value`: The challenge's current value.
- `initial`: The challenge's initial value. (For dynamic challenges only)
- `decay`: The challenge's decay value. (For dynamic challenges only)
- `minimum`: The challenge's minimum value. (For dynamic challenges only)
- `description`: The challenge's description.
- `connection_info`: The challenge's connection info. (Optional)
- `next_id`: The challenge's next ID. (Optional) (For standard challenges only, this seems to be a bug)
- `category`: The challenge's category.
- `state`: The challenge's state. Is either `visible` or `hidden`.
- `max_attempts`: The challenge's maximum number of attempts.
- `type`: The challenge's type. Is either `standard` or `dynamic`.
- `type_data`: The challenge's type data. (You do not need to worry about this)


## `PATCH /challenges/<int:challenge_id>`
Updates a challenge.

### Parameters
- `name`: The challenge's name. (Optional)
- `category`: The challenge's category. (Optional)
- `description`: The challenge's description. (Optional)
- `connection_info`: The challenge's connection info. (Optional)
- `value`: The challenge's value. (Optional) (For standard challenges only)
- `initial`: The challenge's initial value. (For dynamic challenges only) (Optional)
- `decay`: The challenge's decay value. (For dynamic challenges only) (Optional)
- `minimum`: The challenge's minimum value. (For dynamic challenges only) (Optional)
- `max_attempts`: The challenge's maximum number of attempts. (Optional)
- `state`: The challenge's state. Is either `visible` or `hidden`. (Optional)


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
    "type_data": { ... }
  }
}
```

### Return Values
- `id`: The challenge's ID.
- `name`: The challenge's name.
- `value`: The challenge's current value.
- `initial`: The challenge's initial value. (For dynamic challenges only)
- `decay`: The challenge's decay value. (For dynamic challenges only)
- `minimum`: The challenge's minimum value. (For dynamic challenges only)
- `description`: The challenge's description.
- `connection_info`: The challenge's connection info. (Optional)
- `next_id`: The challenge's next ID. (Optional) (For standard challenges only, this seems to be a bug)
- `category`: The challenge's category.
- `state`: The challenge's state. Is either `visible` or `hidden`.
- `max_attempts`: The challenge's maximum number of attempts.
- `type`: The challenge's type. Is either `standard` or `dynamic`.
- `type_data`: The challenge's type data. (You do not need to worry about this)


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