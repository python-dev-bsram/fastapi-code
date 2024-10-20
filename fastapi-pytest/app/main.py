from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()

# Basic FastAPI endpoints
@app.api_route("/",methods=["GET"])
async def read_root():
    return {"message": "Hello World"}

@app.api_route("/items/{item_id}",methods=["GET"])
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


def fake_authentication(token: str):
    if token != "valid-token":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

@app.api_route("/protected", methods=["GET"])
async def protected_route(token: str = Depends(fake_authentication)):
    return {"message": "Authenticated!"}
