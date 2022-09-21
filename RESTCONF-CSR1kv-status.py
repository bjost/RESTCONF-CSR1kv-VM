import json, requests

uri = "https://192.168.56.101:443/restconf/data/ietf-interfaces:interfaces-state/"
payload={}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28xMjMh'
}
resp = requests.request("GET", uri, headers=headers, data=payload, verify=False)

print(resp)
respJSON = json.loads(resp.text)

for interface in respJSON["ietf-interfaces:interfaces-state"]["interface"]:
    print(interface["name"], interface["admin-status"])

