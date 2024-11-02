from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hass_password(password : str):
    hashed_password = pwd_context.hash(password)
    return hashed_password

def verify_passwords(plain_password,hash_password):
    return pwd_context.verify(plain_password,hash_password)

