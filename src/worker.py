from cache_helper import generate_cache_connection
from rq import Worker, Queue, Connection
from settings import REDIS_CONFIG, WORKER_QUEUE_NAME

listen = [WORKER_QUEUE_NAME]

conn = generate_cache_connection()

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()