from fastapi import FastAPI

app = FastAPI()

@app.get("/api/info")
def get_info():
    info = {
        "version": "6.5.0",
        "success": True
    }
    return info

