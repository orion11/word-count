import json
import requests

from cache_helper import generate_cache_connection
from collections import Counter
from inscriptis import get_text
from nltk.corpus import stopwords
from settings import ORDERED_WORD_COUNT_KEY
from string import punctuation


class WordCount:
    def text_from_url(self,url):
        res = requests.get(url)
        html = res.text
        text = get_text(html)
        return text

    def text_to_counts(self,text):
        words = map(str.lower, text.split())
        counts = Counter(words)
        return counts

    def cleanse_words(self,counts):
        REMOVE = set(stopwords.words()).union(set(punctuation), set(["—", "•"]))
        counts_cleansed = counts.copy()
        for word in REMOVE:
            counts_cleansed.pop(word, None)
        return counts_cleansed

    def save_counts(self,counts, cache):
        for word, count in counts.items():
            new_count = cache.incr(word, amount=count)
            cache.zadd(ORDERED_WORD_COUNT_KEY, {word: new_count})

    def run(self, url):
        cache = generate_cache_connection()
        text = self.text_from_url(url)
        counts = self.text_to_counts(text)
        global_counts = self.save_counts(counts, cache)
        return global_counts
