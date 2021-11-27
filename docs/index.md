```properties
Author: Adarsh Pathak
Github: 16umm001
Email: adarshp199877@gmail.com
```

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
