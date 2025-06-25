from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def read_health() -> dict[str, str]:
    """Return application health status."""
    return {"status": "ok"}
