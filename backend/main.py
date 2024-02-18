import redis.asyncio as aioredis

from fastapi import FastAPI


# constants
REDIS_HOST = "0.0.0.0"
REDIS_PORT = 6379
LEFT_ROAD = "left"
RIGHT_ROAD = "right"
TOP_ROAD = "top"
BOTTOM_ROAD = "bottom"


# Initialize Redis connection
redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}", encoding="utf-8", decode_responses=True)


app = FastAPI()

@app.get("/")
async def home():
    return {
        LEFT_ROAD: int(await redis.get(LEFT_ROAD)),
        RIGHT_ROAD: int(await redis.get(RIGHT_ROAD)),
        TOP_ROAD: int(await redis.get(TOP_ROAD)),
        BOTTOM_ROAD: int(await redis.get(BOTTOM_ROAD)),
    }
