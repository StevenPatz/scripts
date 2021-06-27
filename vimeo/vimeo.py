import requests
import json

url = "https://api.vimeo.com/oauth/authorize/client"

payload = json.dumps({
  "grant_type": "client_credentials",
  "scope": "public private upload"
})
headers = {
  'Accept': 'application/vnd.vimeo.*+json;version=3.4',
  'Content-Type': 'application/json',
  'User-Agent': 'spatz_uploader',
  'Authorization': 'Basic MTcxNDJiODU2NDZkYzAzN2FhZDY1MGM4NmNlZDA4ZWUyZTQyZGJhYzpmZGJkNTBlNjA3N2NiM2EwOThhMThmYWQwZDBlYmFhNDVjNzAxNTI2',
  'Cookie': '__ssid=96b79eab-71f4-4815-b951-97471b02323f; has_logged_in=1; has_uploaded=1'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# import requests
# import json

url = "https://api.vimeo.com/me/videos"

payload = json.dumps({
  "upload": {
    "approach": "post",
    "size": "5000",
    "redirect_url": "http://www.stevenpatz.net/~spatz"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/vnd.vimeo.*+json;version=3.4',
  'Authorization': 'Bearer 423ede4c8bdb280078f7e6a4194432fb'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

