# Here , we will create the token and validate the token :

# jose is (Encryption/Decryption library)

# We need setting() which is an attribute from security from.py So, to import it the path would be (app--->core--->config)


from datetime import datetime,timezone,timedelta
from jose import jwt,JWTError
from app.core.config import settings

def create_token(data:dict,expire_minutes=30):
        to_encode = data.copy() # making copy of i/p data
        expire = datetime.now(timezone.utc) + timedelta(minutes = expire_minutes)
        to_encode.update({'exp':expire})
        return jwt.encode(
                to_encode,
                settings.JWT_SECRET_KEY,
                algorithm = settings.JWT_ALGORITHM
        )

def verify_token(token:str):
        try:
            payload = jwt.decode(
                   token,settings.JWT_SECRET_KEY,algorithms=[settings.JWT_ALGORITHM]       
            )    
            return payload
        except JWTError:
               return None