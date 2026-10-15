from fastapi import FastAPI

app = FastAPI(title="Seed FastAPI service")


@app.get("/")
def root():
    return {"message": "Seed FastAPI service. Add routes, then ship it."}


@app.get("/health")
def health():
    return {"status": "ok"}
