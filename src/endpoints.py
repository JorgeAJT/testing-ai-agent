from fastapi import APIRouter, HTTPException
from .models import User
from .utils import load_users, save_users

router = APIRouter()

users = load_users()

@router.get("/")
async def root():
    return {"message": "FastAPI app is running"}

@router.post("/users/")
async def create_user(user: User):
    for existing_user in users:
        if existing_user["username"] == user.username:
            raise HTTPException(status_code=400, detail="Username already exists")
        if existing_user["email"] == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")

    new_id = max([u["user_id"] for u in users], default=0) + 1
    new_user = {
        "user_id": new_id,
        "username": user.username,
        "email": user.email,
        "password": user.password,
        "age": user.age,
        "languages": user.languages,
    }

    users.append(new_user)
    save_users(users)
    return {"message": "User created successfully", "user_id": new_id}

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    for user in users:
        if user["user_id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/users/{user_id}")
async def update_user(user_id: int, user: User):
    # Find the user to update
    target_user = None
    for existing_user in users:
        if existing_user["user_id"] == user_id:
            target_user = existing_user
            break
    
    if target_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if username or email already exist in other users
    for existing_user in users:
        if existing_user["user_id"] == user_id:
            continue
        if existing_user["username"] == user.username:
            raise HTTPException(status_code=400, detail="Username already exists")
        if existing_user["email"] == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")
    
    # Update the user
    target_user.update({
        "username": user.username,
        "email": user.email,
        "password": user.password,
        "age": user.age,
        "languages": user.languages
    })
    
    save_users(users)
    return {"message": "User updated successfully"}

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    target_user = None
    for user in users:
        if user["user_id"] == user_id:
            target_user = user
            break
    
    if target_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    users.remove(target_user)
    save_users(users)
    return {"message": "User deleted successfully"}
