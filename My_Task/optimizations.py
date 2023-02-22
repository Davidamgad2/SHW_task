import json
import requests

def get_matched_quote_id():
    """Handling matching quote"""

di={}

def Send_requests_quote():
    url = 'http://localhost:8000/Quote/'
    json_file=json.load(open('quotes.json'))
    for i in range(len(json_file)):
        json_file[i]['quoteId']=json_file[i]['id']
        del(json_file[i]['id'])
        requests.post(url,json_file[i])

def Send_requests_author():
    url = 'http://localhost:8000/Author/'
    json_file=json.load(open('authors.json'))
    for i in range(len(json_file)):
        requests.post(url,json_file[i])

