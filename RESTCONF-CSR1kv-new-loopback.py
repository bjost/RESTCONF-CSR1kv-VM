import requests
ipadd = "192.168.56.101"
uri = "https://"+ipadd+":443/restconf/data/ietf-interfaces:interfaces"

headers = {
  'Authorization': 'Basic Y2lzY286Y2lzY28xMjMh',
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

#newLoop = input('Enter the number for the new Loopback interface you wish to create:')
#newIP = input('Enter the IP address for this new Loopback: ')
newMask = input('Enter the subnet mask for the new Loopback: ')

#payload="{\n    \"ietf-interfaces:interface\": {\n        \"name\": \"Loopback\"+newLoop,\n        \"description\": \"Configured by RESTCONF\",\n        \"type\": \"iana-if-type:softwareLoopback\",\n        \"enabled\": true,\n        \"ietf-ip:ipv4\": {\n            \"address\": [\n                {\n                    \"ip\": newIP,\n                    \"netmask\": newMask\n                }\n            ]\n        }\n    }\n}"
payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback110",
        "description": "Configured by RESTCONF",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.0.0.1",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}
resp = requests.request("POST", uri, data=payload, headers=headers, verify=False)

print(resp)
print(resp.text)