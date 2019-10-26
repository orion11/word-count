# Word Count
Service that takes urls and returns the most used words and the number of times each word was found. 

### Run
Simply run `docker-compose up` to start all servies.

### Endpoints

#### / POST

**Request data**

```
{
    "urls": [
        https://example.com/1,
        ...
    ]
}
```

#### / GET, params: top=\<integer\>

**Response data**

Sorted by highest count descending.

```
[
    ["word1", <integer>],
    ...
]
```


### Examples

Get a word count of Tolstoy's War and Peace

```
curl -X POST \
    --header "Content-Type: application/json" \
    --data '{"urls": ["https://ia802607.us.archive.org/14/items/warandpeace02600gut/wrnpc10.txt"]}' \
    http://localhost:5000/
```

Open a browser to http://localhost:5000 and see the top 10 used words and their count.
Adjust the number of results returned with the `top` query string. eg: http://localhost:5000?top=50

To blast the service with ~200 documents.

```
curl -X POST \
    --header "Content-Type: application/json" \
    --data @urls.json \
    http://localhost:5000/
```

To speed up processing, try scaling the workers with `docker-compose scale worker=5`
