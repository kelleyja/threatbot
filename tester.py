# test function for requests
import json 
import requests

payload = {'text':'This is a test'} 
headers = {'Content-type': 'application/json', 'User-Agent':'curl/7.64.1'} 
url = 'https://hooks.slack.com/services/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'
r = requests.post(url, data=json.dumps(payload))
print(r.text)
