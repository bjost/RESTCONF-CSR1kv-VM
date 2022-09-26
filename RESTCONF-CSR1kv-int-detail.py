import json, requests
ipadd = "192.168.56.101"
uri = "https://"+ipadd+":443/restconf/data/ietf-interfaces:interfaces"
payload={}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28xMjMh'
}

intResp = input("Enter name of interface to show details: ")

try:
    resp = requests.request("GET", uri+'/interface='+intResp, headers=headers, data=payload, verify=False)
    print(resp)
    respJSON = json.loads(resp.text)
    print(respJSON)
except:
    print("An exception happened.")





