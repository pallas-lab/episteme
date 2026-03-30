# The main entry point for the Episteme API.
# Sets up the FastAPI application and defines a simple health check endpoint.
from fastapi import FastAPI

# Create the FastAPI application instance with metadata.
app = FastAPI(
    title="Episteme API",
    description="Research intelligence system powered by GraphRAG and agentic reasoning",
    version="0.1.0",
)

# Basic health check endpoint to verify that the API is running.
@app.get("/health")
async def health():
    return {"status": "ok", "version": "0.1.0"}