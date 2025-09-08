
# Task Management API

A Django REST Framework (DRF) project for managing tasks with authentication and permissions.


## Table of Contents
1. [Introduction](#introduction)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Tech Stack](#TechStack) 
6. [Watch](#watch)  
7. [License](#license)
8. [Conclusion](#conclusion)
## Introduction
The (**Task Management API**) is a Django-based project that allows users to register, log in, and manage their daily tasks.  
It provides a clean web interface along with REST API endpoints, making it easy to integrate with other applications.  
This project was built as part of a capstone to demonstrate backend development skills, authentication, and CRUD functionality.


## Features

- User registration and authentication (JWT)
- Create, Read, Update, and Delete (CRUD) tasks
- Permissions (only owners can update/delete their tasks)
- Token-based authentication
- Mark tasks as completed 
- Due dates for tasks 

## Installation

Install my-project 

```bash
  git clone https://github.com/Ahad0015/Alx_DjangoLearnLab.git
  cd my-project
```
Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

```
Install dependencies
```bash
  pip install -r requirements.txt

```
Apply migrations
```bash
  python manage.py migrate

```
Run the development server
```bash
 python manage.py runserver
```
Open
```bash
 http://127.0.0.1:8000/
```


## Usage
- Register a new account

- Log in to manage your tasks

- Add new tasks with title, description, and due date

- Edit or delete tasks anytime
## Tech Stack
- Backend: Django
- Database: SQLite 
- Frontend: HTML, Bootstrap (via Django templates)
## Watch the full series!

  https://www.loom.com/share/a171ea6e79d3445fad1cd83f498fa18b?sid=6c0b914e-248f-45ee-a2d9-e9a3fb4593c4

## License

MIT License – feel free to use and modify.


## Conclusion
This project demonstrates Django + Django REST Framework for building real-world APIs with authentication and CRUD functionality.
It serves as a foundation for more complex applications like project management tools or productivity apps.