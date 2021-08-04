# importing the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "http://34.90.165.158:80/v1/models/flowers-sample-gpu:predict"

# your source code here
headers_t = {
            'host': "flowers-sample-gpu.experiment1.example.com",
            'content-type': "application/json",
            'cache-control': "no-cache"
        }

# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, headers=headers_t, data=open('input3.json', 'rb'))

# extracting response text
response_json = r.json()
print(response_json)