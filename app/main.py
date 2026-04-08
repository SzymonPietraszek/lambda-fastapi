from fastapi import FastAPI, APIRouter
from app.routers import hello, dynamo
from mangum import Mangum

app = FastAPI()
api_router = APIRouter(prefix="/api")
api_router.include_router(hello.router)
api_router.include_router(dynamo.router)


@api_router.get("/")
async def root():
    return {"message": "Hello World from Root!"}


app.include_router(api_router)
handler = Mangum(app)
