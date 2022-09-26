import json, requests
ipadd = "192.168.56.101"
uri = "https://"+ipadd+":443/restconf/data/ietf-interfaces:interfaces"
payload={}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28xMjMh'
}
resp = requests.request("GET", uri, headers=headers, data=payload, verify=False)

print(resp)
respJSON = json.loads(resp.text)

for interface in respJSON["ietf-interfaces:interfaces"]["interface"]:
    print(interface["name"], interface["ietf-ip:ipv4"]["address"][0]["ip"])