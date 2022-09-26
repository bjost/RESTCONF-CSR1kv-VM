import json, requests
HOST = '192.168.56.101'
PORT = '443'
USER = 'cisco'
PASS = 'cisco123!'

uri_base = "https://{h}:{p}/restconf".format(h=HOST, p=PORT)

headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

uri = uri_base+"/data/ietf-interfaces:interfaces"

resp = requests.get(uri, auth=(USER, PASS), headers=headers, verify=False)

print(resp)
respJSON = resp.json()

for interface in respJSON["ietf-interfaces:interfaces"]["interface"]:
    print(interface["name"], interface["ietf-ip:ipv4"]["address"][0]["ip"])