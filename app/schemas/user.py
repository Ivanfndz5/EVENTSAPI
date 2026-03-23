from pydantic import BaseModel,EmailStr, Field



class UserBase(BaseModel):
    name : str
    email : EmailStr

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = False

