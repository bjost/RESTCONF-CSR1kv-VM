from fcntl import F_SEAL_SHRINK
import json, requests
ipadd = "192.168.56.101"
uri = "https://"+ipadd+":443/restconf/data/ietf-interfaces:interfaces"
payload={}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28xMjMh'
}

intResp = input("Enter name of loopback interface to delete: ")


resp = requests.request("DELETE", uri+'/interface='+intResp, headers=headers, data=payload, verify=False)

if resp.status_code == 201:
    print('Interface ', intResp, " successfully deleted.")
elif resp.status_code == 404:
    print('Interface', intResp, "does not exist.")
else:
    print('Some error occurred. Response code = ', resp.status_code)
