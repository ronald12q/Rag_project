from fastapi import FastAPI

from .routes import router

app = FastAPI()


app.include_router(router)


@app.get("/")
def raiz():
    return {"message": "server running"}


@app.get("/health")
def health():
    return {"status": "ok"}
