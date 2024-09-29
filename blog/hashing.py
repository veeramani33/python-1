from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated='auto')
class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)
    
    def verify(org_pwd, user_pwd):
        return pwd_cxt.verify(user_pwd,org_pwd)