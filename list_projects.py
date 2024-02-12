# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://sagar8340103595.atlassian.net//rest/api/3/project"

API_TOKEN="ATATT3xFfGF0PdfTjWDiQcIvtU8r3TykNsDYCMMjl2u20vVTRoh52KhcnGgEFqcaUKflo1Qg2Sa5PVG2ci_deTZ7QlyG3RtzF02OJ-0rgcECfqLt4WVABkECrYLbYAnrtfCy4MDNr_ztXXDe_mCVizexgMq4VVnvetS1a6G2nq93m8u06ndLLiY=F4D28576"

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
