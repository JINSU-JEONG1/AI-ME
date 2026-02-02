from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
)
# Global Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
content={"message": "Internal Server Error", "detail": str(exc)},    )

@app.get("/")
def read_root():
    return {"message": "Welcome to AI-ME API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="[IP_ADDRESS]", port=8000, reload=True)
