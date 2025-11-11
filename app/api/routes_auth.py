# routes_auth.py: Defines the /login route for user authentication via JWT

# Here, we will define end-point of every api and for every end-point there wil be a dedicated module

from fastapi import APIRouter #(We are not defining our end-pts directly we are defining it indirectly this is why we need --> APIRouter)
from pydantic import BaseModel
from app.core.security import create_token

# Instead of using Fastapi we are using APIRouter
router = APIRouter #(not app = Fastapi())

# We want that when user reaches end-pt he should give two things username *& password
class AuthInput(BaseModel):
    username = str
    password = str

# End-pt named 'login'
@router.post('/login')
def login (auth : AuthInput):
    if (auth.username == 'admin') and (auth.password == 'admin'):
        # create the token(If credentials are correct)
        token = create_token({'sub':auth.username})
        # return the token to the user(If credentials are correct)
        return {'access_token':token}
    #(If credentials are not correct) return 'Invalid credentials' 
    return {'error':'Invalid Credentials'}