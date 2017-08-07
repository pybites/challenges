# PyBites Code Challenge 30 - The Art of Refactoring: Improve Your Code

For this challenge I decided to refactor a Flask route handler because of this [issue](https://github.com/realpython/flask-jwt-auth/issues/9) that was added to the [Flask JWT Auth](https://github.com/realpython/flask-jwt-auth) project. Since this project is the example app built for the [Token-Based Authentication With Flask](https://realpython.com/blog/python/token-based-authentication-with-flask/) blog post, I had to update the blog post as well.

## Issue

Review the actual submitted [issue](https://github.com/realpython/flask-jwt-auth/issues/9) from GitHub for full details.

Essentially, the following code only handles situations where the `Authorization` header has a space between `Bearer` and the actual token:

```
Bearer TOKEN_VALUE
```

Code:

```python
def get(self):
    # get the auth token
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token:
        resp = User.decode_auth_token(auth_token)
```

Even though the correct format for authorization is `Bearer TOKEN_VALUE`, it's best to handle situations where an end-user does not correctly format the auth header.

Test coverage before refactor:

```sh
Name                           Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------
project/__init__.py                0      0      0      0   100%
project/server/__init__.py        11      0      0      0   100%
project/server/auth/views.py      84     16     18      5    79%
project/server/models.py          47      5      6      1    89%
----------------------------------------------------------------
TOTAL                            142     21     24      6    84%
```

## Refactor

You can view the full refactor [here](https://github.com/realpython/flask-jwt-auth/pull/10).

Test:

```python
def test_user_status_malformed_bearer_token(self):
    """ Test for user status with malformed bearer token"""
    with self.client:
        resp_register = register_user(self, 'joe@gmail.com', '123456')
        response = self.client.get(
            '/auth/status',
            headers=dict(
                Authorization='Bearer' + json.loads(
                    resp_register.data.decode()
                )['auth_token']
            )
        )
        data = json.loads(response.data.decode())
        self.assertTrue(data['status'] == 'fail')
        self.assertTrue(data['message'] == 'Bearer token malformed.')
        self.assertEqual(response.status_code, 401)
```

Code:

```python
def get(self):
    # get the auth token
    auth_header = request.headers.get('Authorization')
    if auth_header:
        try:
            auth_token = auth_header.split(" ")[1]
        except IndexError:
            responseObject = {
                'status': 'fail',
                'message': 'Bearer token malformed.'
            }
            return make_response(jsonify(responseObject)), 401
    else:
        auth_token = ''
    if auth_token:
        resp = User.decode_auth_token(auth_token)
```

Test coverage after refactor:

```sh
Name                           Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------------
project/__init__.py                0      0      0      0   100%
project/server/__init__.py        11      0      0      0   100%
project/server/auth/views.py      88     16     18      5    80%
project/server/models.py          47      5      6      1    89%
----------------------------------------------------------------
TOTAL                            146     21     24      6    84%
```
