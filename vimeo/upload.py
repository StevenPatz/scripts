import requests
import json
import os
import sys
from dotenv import load_dotenv

load_dotenv()
if len(sys.argv) != 3:
    raise ValueError('Need two arguments. Filename first, followed my Vimeo name')

file_name = sys.argv[1]
video_name = sys.argv[2]
token = "Bearer " + os.environ['ACCESS_TOKEN']
file_size = os.path.getsize(file_name)
url = "https://api.vimeo.com/me/videos?fields=uri,upload.upload_link"

payload = json.dumps({
  "upload": {
    "approach": "tus",
    "size": file_size
  },
  "name": video_name
 })
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/vnd.vimeo.*+json;version=3.4',
  'Authorization': token
}

response = requests.request("POST", url, headers=headers, data=payload)
upload = response.json()
vimeo_url = upload['uri']
upload_link = (upload["upload"]["upload_link"])
# print(upload_link)


############################


with open(file_name, 'rb') as f:
    data = f.read()
res = requests.patch(url=upload_link,
                    data=data,
                    headers={'Tus-Resumable': '1.0.0',
                             'Upload-Offset': '0',
                            'Content-Type': 'application/offset+octet-stream',
                            'Accept': 'application/vnd.vimeo.*+json;version=3.4'})

 
bytes_uploaded = int(res.headers["Upload-Offset"])
if(bytes_uploaded != file_size):
    print("Upload did not complete.\n")
    print(bytes_uploaded + " bytes uploaded.")
    #TODO Restart upload using Patch, Set Upload-Offset to what whatever is in bytes_uploaded.

# We need to get the numeric part of the vimeo_url and then append that to the print below.
done_url = name = vimeo_url.split('/')[1]
print("File was uploaded and is available here: " + "https://www.vimeo.com" + done_url)
