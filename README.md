# Mentorship-Task
# Task State Api 

## Project Structure
```
├── absolute_difference.py  
├── common_substring.py
├
└── task_state_api
```

## Installation
* run `` python3 -m venv env `` Then activate the env
* run `` pip install -r requirements.txt ``

### Pre-requisites and Local Development Server
* run `` python3 manage.py makemigrations ``
* run `` python3 manage.py migrate ``
* run `` python3 manage.py runserver ``
- You can login as admin with these credentials ``username = admin`` and ``password = admin``
 
## The application is run at http://127.0.0.1:8000/ by default <hr>

`` LIST & CREATE `` 
## Navigate to http://127.0.0.1:8000/api/tasks/
`` To List All Available Tasks & Create New Tasks `` <hr> 

`` UPDATE , DELETE, DETAIL `` 
## Navigate to http://127.0.0.1:8000/api/tasks/<<int:pk>>/
`` To View Task Detail & Delete & Update(under the predefined state machine) ``


## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE.

In our case, we have one single resource, `tasks`, so we will use the following URLS - `/tasks/` and `/tasks/<id>`

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/tasks` | GET | READ | Get all tasks
`api/tasks`| POST | CREATE | Create a new task
`api/tasks/:id` | GET | READ | Get a single task
`api/tasks/:id` | PUT | UPDATE | Update a task
`api/tasks/:id` | DELETE | DELETE | Delete a task 

## Use
We can test the API using [curl] or we can use [Postman]
```
let's try:
curl  http://127.0.0.1:8000/api/tasks/19/
```
we get:
```
{
    "id": 19,
    "title": "Learn Django 4",
    "state": "active"
}

```
### Commands
```
Get all tasks
curl http://127.0.0.1:8000/api/tasks/ 

Get a single task
curl http://127.0.0.1:8000/api/tasks/{task_id}/   

Create a new task
curl -X POST -d "title=created from curl&state=active" http://127.0.0.1:8000/api/tasks/   

Full update a task
curl -X PUT -d "title=Learn Django&state=active" http://127.0.0.1:8000/api/tasks/19/   

Delete a task
curl -X DELETE http://127.0.0.1:8000/api/tasks/{task_id}/  

```
### note
```
So the workflow of the task: draft → active → done → archived.
The task can not move from draft to done, can not move from active or done to draft, and can not
move from archived backward. But task can move from any state to archive.
The task updated under the defined workflow only.
```
