from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}


@app.get("/healthy")
def healthy():
    return {"status": "healthy"}

print("teste questao 1 - > commit por push na src + branch dev")
