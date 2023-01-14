import json
import requests

def get_matched_quote_id():
    """Handling matching quote"""

dict={}
def parse_json():
    counter=0
    json_file=json.load(open('authors.json'))
    for i in json_file:
        dict[counter]("id:", i['id'])
        dict[counter]("author:", i['author'])
        dict[counter]("quoteIds:", i['quoteIds'])
        counter+=1

def Send_requests():
    url = 'http://localhost:8000/Tag/'
    json_file=json.load(open('authors.json'))
    for i in range(len(json_file)):
        requests.post(url,json_file[i])

Send_requests()
