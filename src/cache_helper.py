import redis
from settings import REDIS_CONFIG

def generate_cache_connection():
    cache = redis.Redis(host=REDIS_CONFIG.host, port=REDIS_CONFIG.port)
    return cache