from os import environ


class _REDIS_CONFIG:
    host = environ.get('REDIS_HOST', 'redis')
    port = environ.get('REDIS_PORT', 6379)

REDIS_CONFIG = _REDIS_CONFIG()


ORDERED_WORD_COUNT_KEY = 'orderings'
WORKER_QUEUE_NAME = 'counts'
