import uvicorn

# This file serves as the entry point for running the FastAPI application.
if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=7860, reload=True)