import json
import time

from cache_helper import generate_cache_connection
from flask import Flask, request, jsonify
from rq import Queue
from rq.job import Job
from settings import ORDERED_WORD_COUNT_KEY, REDIS_CONFIG, WORKER_QUEUE_NAME
from word_count import WordCount
from worker import conn


app = Flask(__name__)

cache = generate_cache_connection()
q = Queue(WORKER_QUEUE_NAME, connection=cache)

@app.route('/', methods=['POST'])
def generate_counts():
    res = request.get_json()
    urls = res['urls']
    print(urls)
    for url in urls:
        if cache.get(url) is None:
            cache.set(url, '')
            job = q.enqueue_call(func=WordCount().run, args=(url,))

    return ('Accepted', 202)

@app.route('/', methods=['GET'])
def get_counts():
    top = request.args.get('top', 10)
    keys = cache.zrange(ORDERED_WORD_COUNT_KEY, 0, int(top), desc=True)
    words = []
    for key in keys:
        count = cache.get(key)
        words.append([key.decode('utf-8'), int(count)])
    return jsonify(words)