
import json
import requests


def omdbget(movieid):
    print("http://www.omdbapi.com/?apikey=ad9a897d&i="+movieid)
    resp = requests.get("http://www.omdbapi.com/?apikey=ad9a897d&i="+movieid)
    print(resp)
    return resp
