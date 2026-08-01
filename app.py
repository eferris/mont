from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from your remote frontend domain(s)
origins = [
    "https://redhairedlion.com",
    "http://127.0.0.1:8080",  # For local testing
    "http://localhost:8080",  # For local testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Or ["*"] to allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/Data")
def read_data():
    return {"message": "Hello from the remote FastAPI server!"}


