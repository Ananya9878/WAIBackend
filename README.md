Note: For testing please use "test.py" script or use below-mentioned endpoints. Cause django-restframework requires trailing slash at the end of each endpoint.

# WAIBackend
Waterdip AI Backend Assignment
###Stack
1. Language: Python
2. Framework: Django, Django-RestFramework
3. Database: SQLite
###Installation Steps
1. git clone https://github.com/Ananya9878/WAIBackend.git
2. cd ./WAIBackend
3. Create venv and install requirements.txt (pip install -r ./requirements.txt)
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py runserver 0.0.0.0:5000

###Test
1. python test.py

### Endpoint:
1. create a new tasks: <b>POST</b> http://localhost:5000/v1/tasks/
2. List all tasks: <b>GET</b> http://localhost:5000/v1/tasks/
3. Get task: <b>GET</b> http://localhost:5000/v1/tasks/<id>/
4. Update task: <b>PUT</b> http://localhost:5000/v1/tasks/<id>/
5. Delete a task: <b>DELETE</b> http://localhost:5000/v1/tasks/<id>/
6. create bulk tasks: <b>POST</b> http://localhost:5000/v1/tasks/
7. Delete bulk tasks: <b>DELETE</b> http://localhost:5000/v1/tasks/