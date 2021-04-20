from fastapi import FastAPI,Response,Request,status
from hashlib import sha512


app=FastAPI()

@app.get("/") # dekorator
def root():
    return {"message": "Hello world!"}

#@app.get("/auth")
#def auth_view(response:Response, password: str =None , pass_hash= str=None):
#    response.status_code=status.HTTP_401_UNAUTHORIZED
#    if not(password and pass_hash):
#        return 
#    if sha512(password.encode()).hexdigest() == pass_hash:
#        response.status_code=status.HTTP_204_NO_CONTENT
