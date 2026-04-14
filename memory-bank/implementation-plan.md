# Implementation Plan

## Goals

Create a funtional API

## Rules

- Follow steps IN ORDER, one at a time
- Do not implement the next step until the current one is verified by a human
- Lines starting with "Human test:" are NOT for the agent, skip them

## Steps

1. ✅ Create the simplest, minimal and functional FastAPI app
✅ Human test: run the server and verify it starts without errors

2. ✅ Create project structure following memory-bank/app-description.md
   - Use __init__.py to expose src as a Python module for clean imports
   - Move the health check endpoint GET / from main.py to src/endpoints.py
   - main.py must only initialize the app and register routers from src/endpoints.py
   - Create .gitignore with .venv/ and memory.json excluded
✅ Human test: run the server and verify it starts without errors

3. ✅ Create a POST /users/ endpoint
    - Use the data structure defined in memory-bank/app-description.md
    - When an username or email already exist in the database (memory.json) throw an error
✅ Human test: run the server and try the POST endpoint using Postman

4. ✅ Create a GET /users/<int:user_id> endpoint
✅ Human test: run the server, and try the POST endpoint using Postman

5. ✅ Create a PUT /users/<int:user_id> endpoint
    - When an username or email already exist in the database (memory.json) throw an error
✅ Human test: run the server and try the PUT endpoint using Postman

6. ✅ Create a DELETE /users/<int:user_id> endpoint
✅ Human test: run the server, and try the DELETE endpoint using Postman
