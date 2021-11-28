```properties
Author: Adarsh Pathak
Github: 16umm001
```

[TOC]

# Authentication

## Register

``` 
POST api/auth/register
```

**Parameter**

Name   | Description
-------|---------------
first_name | First Name (Required)
last_name | Last Name (Required)
email | Email (Required)
username | Username (Required)
phone_number | Phone Number (Optional)
password | Password (minimum length 8) (Required)

**Request Body**
```json
{
    "username": "test_user",
    "email": "jon_doe@email.com", 
    "first_name": "Jon",
    "last_name": "Doe", 
    "phone_number": "+12345678901", 
    "password": "strongpassword123"
}
```

**Respose**
```json
{
    "username": "test_user",
    "email": "jon_doe@email.com", 
    "first_name": "Jon",
    "last_name": "Doe", 
    "phone_number": "+12345678901",
    "auth_token": "8215b4cf6f94d13525a7e178bafc6bd221efd4b1cad36d5a34bd346b8c26e90b"
}
```

## Login 
``` 
POST api/auth/login
```

**Request**
```json
{
    "email": "john@doe.com", 
    "password": "12345678"
}
```

**Response**
```json
{
    "username": "John",
    "email": "john@doe.com",
    "first_name": "John",
    "last_name": "Doe",
    "phone_number": "+12345678901",
    "auth_token": "b73ade90fbac4c130895ef73a1bbe7639ebc3797b80c0887fce1b325bef307d8"
}
```

## Logout
```
POST api/auth/logout (requires Authentication)
```

**Response**
```json
{
    "success": true
}
```

## Change Password
``` 
POST /api/auth/change-password
```

**Request**
```json
{
    "current_password": "strongpassword",
    "new_password": "veryStrongPassword"
}
```

**Response**
```json
{
    "success": true
}
```
