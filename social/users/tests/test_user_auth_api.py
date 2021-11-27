from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class UserRegister(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('auth-register')
        self.data = {
            "first_name": "Jon",
            "last_name": "Doe",
            "email": "test@email.com",
            "password": "test1234",
            "username": "test_user",
            "phone_number": "9876543210"
        }

        self.response_keys = {'username', 'email', 'first_name', 'last_name', 'phone_number', 'password', 'auth_token'}

    def test_user_register(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertSetEqual(self.response_keys, set(response.data.keys()))
