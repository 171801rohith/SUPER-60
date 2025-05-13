from fastapi import FastAPI, HTTPException
from book import router

app = FastAPI() 

@app.exception_handler(HTTPException)
async def handle_exception(request, exc):
    return 

app.include_router(router)