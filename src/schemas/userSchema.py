from pydantic import BaseModel
class UserCreate(BaseModel):
    email: str
    username: str
    name: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    username: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: str
    password: str