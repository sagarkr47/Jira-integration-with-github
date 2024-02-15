# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://sagar8340103595.atlassian.net//rest/api/3/issue"

API_TOKEN="ATATT3xFfGF0PdfTjWDiQcIvtU8r3TykNsDYCMMjl2u20vVTRoh52KhcnGgEFqcaUKflo1Qg2Sa5PVG2ci_deTZ7QlyG3RtzF02OJ-0rgcECfqLt4WVABkECrYLbYAnrtfCy4MDNr_ztXXDe_mCVizexgMq4VVnvetS1a6G2nq93m8u06ndLLiY=F4D28576"


auth = HTTPBasicAuth("kumarsagar8340103595@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "AB"
    },
    "issuetype": {
      "id": "10001"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

 return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
