import json, requests
HOST = '192.168.56.101'
PORT = '443'
USER = 'cisco'
PASS = 'cisco123!'

uri_base = "https://{h}:{p}/restconf".format(h=HOST, p=PORT)

headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

intResp = input("Enter name of interface to show details: ")

uri = uri_base+"/data/ietf-interfaces:interfaces/interface="+intResp

try:
    resp = requests.get(uri, auth=(USER, PASS), headers=headers, verify=False)
    print(resp)
    respJSON = resp.json()
    print(respJSON)
except:
    print("An exception happened.")





