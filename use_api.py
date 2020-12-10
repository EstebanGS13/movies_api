import urllib.request
import json

base_url = 'http://127.0.0.1:5000/api/v1/resources/movies'

query = '?directed_by=Christopher+Nolan'

url = base_url + query
response = urllib.request.urlopen(url)
data = json.loads(response.read())
print(json.dumps(data, indent=4, ensure_ascii=False))