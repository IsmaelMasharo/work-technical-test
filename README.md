
# REST API for personal notes.

The application running locally has the following endpoints:
http://127.0.0.1:8000/user
http://127.0.0.1:8000/notes

Notes can only be seen by the account owner.

Create an account:
- endpoint: POST http://127.0.0.1:8000/user/signup
- payload: {
            "username": "username", 
            "email": "email",
            "password": "password"
            }

Loguing:
- endpoint: POST http://127.0.0.1:8000/user/login
- payload: {
            "username": "username", 
            "password": "password"
            }
- return: jwtoken

Create a personal note:
- endpoint: POST http://127.0.0.1:8000/notes
- header: {
            "Content-Type" : "application/json"
            "Authorization": "Bearer jwtoken"
            }
- payload: {
            "content": "content", 
            }

Retrieve all personal notes:
- endpoint: GET http://127.0.0.1:8000/notes
- header: {
            "Content-Type" : "application/json"
            "Authorization": "Bearer jwtoken"
            }

Retrieve specific note:
- endpoint: GET http://127.0.0.1:8000/notes
- header: {
            "Content-Type" : "application/json"
            "Authorization": "Bearer jwtoken"
            }

JWT its being sent at loguing. Should be sent back in the header for user authentication.

Run server side:
- cd server
- python server.py

Run client side:
- cd client
- python client.py
