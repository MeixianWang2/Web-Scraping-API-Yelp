import requests
import json

api_key='1TJnLOeAx6pkSBvcxy7QKEakp_YKcUzRfiKjOSxesn2T93uHj2JAoDll0kGwUTS1Z8PSz7SxEolSj2vhFnwzWCCxlayE0SKITuxCTWIHCwDjN4pXkUZgTSHEDfKOX3Yx'
headers = {'Authorization': 'Bearer %s' % api_key}

url = 'https://api.yelp.com/v3/businesses/search'

for i in range(1,20):
    print(i)
    tmpoffset = 50*i+1
    params = {'term':'restaurant','limit': 50,'offset': tmpoffset,'location':'New York City'}
    req = requests.get(url, params=params, headers=headers)
    business_data = req.json()
    with open('yelp/NY_business.json', 'a') as f:
        json.dump(business_data, f, ensure_ascii=False, indent=4)
        print(business_data)
