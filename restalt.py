import json
import requests
import sys
from argparse import ArgumentParser
from collections import OrderedDict
import urllib3

ipadd = "192.168.56.101"
uri = "https://"+ipadd+":443/restconf/data/ietf-interfaces:interfaces"

headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}
response = requests.get(uri,
                        auth = ("cisco", "cisco123!"),
                        headers=headers,
                        verify = False)
print(response.json()["ietf-interfaces:interfaces"]["interface"])
