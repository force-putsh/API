from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/route1")
async def proxy_service1():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8001/hello")
        return response.json()

@app.get("/route2")
async def proxy_service2():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8002/goodbye")
        return response.json()
