import os
import requests
import json
from pprint import pprint
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":
    token = os.environ["NETBOX_TOKEN"]
    url ="https://netbox.lasthop.io/api/dcim/devices/"
#    url = "https://www.facebook.com"
    http_headers = {
        "Content-type":"application/json; version=2.4;",
        "authorization" : "Token {}".format(token),
    }
    post_data = {
        "name": "arista9",
        "device_role": 3,  # Distribution Switch
        "device_type": 2,  # vEOS
        "display_name": "arista8",
        "platform": 4,  # Arista EOS
        "rack": 1,  # RK1
        "site": 1,  # Fremont Data Center
        "status": 1,  # Active
    }

    response = requests.post(
        url, headers=http_headers, data=json.dumps(post_data), verify=False
    )   
#    response = requests.get(url,headers=http_headers,verify=False)
    response= response.json()
#    print(response._content.decode())

    print()
    pprint(response)
