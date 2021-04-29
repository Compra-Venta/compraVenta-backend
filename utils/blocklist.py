import redis
from utils.config import redis_url, redis_password

jwt_redis_blocklist = redis.StrictRedis(
    host=redis_url, port=11437, password = redis_password, db=0, decode_responses=True
)
