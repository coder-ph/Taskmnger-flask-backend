import redis
from src.config.config_map import Config

redis_client = redis.Redis.from_url(Config.REDIS_URL)

def cache_data(key: str, value:str, expire_seconds: int = 3600):
    """Cache data in redis with an optional expiry."""
    
    redis_client.setex(key, expire_seconds, value)
    
def get_cached_data(key: str):
    """retreive cached data from redis"""
    return redis_client.get(key)

def invalidate_cache(key: str):
    """delete cached data"""
    
    redis_client.delete(key)