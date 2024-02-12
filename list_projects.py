# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://sagar8340103595.atlassian.net//rest/api/3/project"

API_TOKEN="ATATT3xFfGF0PUv_PsQsX8FsxTI6fWIQXfbQ3rH6rQuRGzf2pX1GkOcK5BQ5oYOqhl3r4QJz6GhqeoHH92LuPimO4fgXxMhP9LjoGqOAxS9uYzDVdRSunI3n38TkIM3jPjcHW_xeKFTV9NCIWR0Fqt-Su8qtc5Lbi3D5CsXOS4A9vkokmTbYpOY=F3FD9889"

auth = HTTPBasicAuth("kumarsagar8340103595@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)