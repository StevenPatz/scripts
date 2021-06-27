import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


token = "Bearer " + os.environ['ACCESS_TOKEN']

url = "https://api.vimeo.com/me/videos?fields=upload.upload_link"

payload = json.dumps({
  "upload": {
    "approach": "tus",
    "size": 93508404
  },
  "name": "Chopped Test One"
 })
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/vnd.vimeo.*+json;version=3.4',
  'Authorization': token
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
