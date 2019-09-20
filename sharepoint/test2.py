import requests
# from requests.auth import HTTPBasicAuth
from requests_ntlm import HttpNtlmAuth

username = 'ironmtn\\slogandurai'
password = 'Aug2018!'

response = requests.get(
    'http://scout.ironmountain.com/functions/globalservices/IT/_api/web/',
    auth=HttpNtlmAuth(username, password)
)

print(response.status_code)
print(response.json())