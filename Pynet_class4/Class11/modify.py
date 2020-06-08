import os
import requests
import json
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":
    token = os.environ["NETBOX_TOKEN"]

    # Arista6
    url = "https://netbox.lasthop.io/api/dcim/devices/8/"
    http_headers = {
        "accept": "application/json; version=2.4;",
        "authorization": "Token {}".format(token),
    }
    response = requests.get(url, headers=http_headers, verify=False)
    arista6 = response.json()

    http_headers = {
        "Content-Type": "application/json; version=2.4;",
        "authorization": "Token {}".format(token),
    }

    # Reformat to get the proper structure for the existing object
    for field in ["device_role", "device_type", "platform", "site", "rack"]:
        arista6[field] = arista6[field]["id"]
    arista6["status"] = 1
    arista6["rack"] = 2

    response = requests.put(
        url, headers=http_headers, data=json.dumps(arista6), verify=False
    )
    response = response.json()
    print()
    pprint(response)
    # print(response._content.decode())
    print()
