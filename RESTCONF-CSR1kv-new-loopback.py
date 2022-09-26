import requests
ipadd = "192.168.56.101"
uri = "https://"+ipadd+":443/restconf/data/ietf-interfaces:interfaces"

headers = {
  'Authorization': 'Basic Y2lzY286Y2lzY28xMjMh',
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

newLoop = input('Enter the number for the new Loopback interface you wish to create:')

payload="{\n    \"ietf-interfaces:interface\": {\n        \"name\": \"Loopback\"+newLoop,\n        \"description\": \"Configured by RESTCONF\",\n        \"type\": \"iana-if-type:softwareLoopback\",\n        \"enabled\": true,\n        \"ietf-ip:ipv4\": {\n            \"address\": [\n                {\n                    \"ip\": \"172.16.110.1\",\n                    \"netmask\": \"255.255.255.0\"\n                }\n            ]\n        }\n    }\n}"

resp = requests.request("POST", uri, data=payload, headers=headers, verify=False)

print(resp)
print(resp.text)