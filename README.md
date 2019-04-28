
REST API para notas.

La aplicacion se corre localmente. Los endpoints son:
http://127.0.0.1:8000/user
http://127.0.0.1:8000/notes

Las notas solo pueden ser accedidas por los usuarios que las crearon.

Crear una cuenta:
- endpoint: POST http://127.0.0.1:8000/user/signup
- payload: {
            "username": "username", 
            "email": "email",
            "password": "password"
            }

Loguearse:
- endpoint: POST http://127.0.0.1:8000/user/login
- payload: {
            "username": "username", 
            "password": "password"
            }
- return: jwtoken

Crear una nota:
- endpoint: POST http://127.0.0.1:8000/notes
- header: {
            "Content-Type" : "application/json"
            "Authorization": "Bearer jwtoken"
            }
- payload: {
            "content": "content", 
            }

Pedir todas las notas:
- endpoint: GET http://127.0.0.1:8000/notes
- header: {
            "Content-Type" : "application/json"
            "Authorization": "Bearer jwtoken"
            }

Pedir una nota:
- endpoint: GET http://127.0.0.1:8000/notes
- header: {
            "Content-Type" : "application/json"
            "Authorization": "Bearer jwtoken"
            }

El jwtoken se envia cuando uno se loguea. 
Para pedir notas se envia el jwtoken en el header y con esta se obtiene el userID.

Iniciar el servidor:
- cd server
- python server.py

Iniciar el cliente:
- cd client
- python client.py
