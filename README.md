# Story-Creation-WebApp

# Overview
Develop a full-stack "Collaborative and Fun Story Creator" web application where
authenticated users can collaboratively write short stories in a fun and structured way. The
backend will be built using Django with the MVC (Model-View-Controller) pattern, and the
frontend will be developed using React/Next.js.

# Instructions

### 1. Project Done with below configurations:
python.exe --version - Python 3.12.6 <br />
node.exe --version - v22.9.0 <br />
npm.cmd --version - 10.8.3 <br />
database settings.py - sqlite (Default) 

### 2. Virtual Environment:
Create Virtual Environment
python -m venv venv
Activate virtual environment .\venv\Scripts\activate
Virtual Environment is Started!

### 3. Frontend:
cd frontend
Install all node_modules npm i or npm install
Run server npm run dev
Frontend is started!

### 4. Backend:
cd backend
Install python site-packages pip install .\requirements.txt
Make migrations python manage.py makemigrations and than python manage.py migrate
After successful migration create a superuser for accessing the admin panel and control over the project python manage.py createsuperuser
Than start backend server python.exe .\manage.py runserver
Backend is started!
