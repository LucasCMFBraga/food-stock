# food-stock

It is a food stock system, the idea is create a app to control the food stock of your house, in the future the app can give suggestion of foods if the details of current stock.

## Backend
Backend was developed with Django and DRF

The backend the as the routes to authentication and register a new user.

The backend is consuming a third party API to resolve the qr code in the product details.

To run the backend we need set some env variables, so rename the file .env_default to .env and feel this variables.
```
SECRET_KEY=cryptographic signing
DEBUG=debug mode   
TOKEN=token to access the third party API.
```
Install the backend dependencies
```
poetry install
```

Run the backend
```
poetry shell # to activate virtual env
python3 manage.py runserver 0.0.0.0:8000 
```

## Frontend 

Frontend was developed the Flutter framework, so the app can be compiled for different platforms.

It was not developed the register screen and the login screen. So to access the backend you have to

Register a user
```
curl --location 'http://127.0.0.1:8000/api/v1/users/' \
--header 'Content-Type: application/json' \
--data '{
    "username":"",
    "first_name":"",
    "last_name":"",
    "email":"",
    "password":""
}'
```

Get the token
```
curl --location 'http://127.0.0.1:8000/api-token-auth/' \
--header 'Content-Type: application/json' \
--data '{
    "username":"",
    "password":""
}'
```

Set the TOKEN in the file constants in flutter project.

Now the frontend can send authenticated requests to the backend. Once the registration and login screens have been developed, this procedure will no longer be needed
