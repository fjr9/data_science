import requests
import hmac
import hashlib
import time

url = 'https://vip.bitcoin.co.id/tapi/'
key = 'my-api-key'
secret = 'my-token-key'
method = 'getInfo'

parameter = {
'method' : method
'nonce' : str(int(time.time())
}

req = '&method=' + method + '&nonce=' + str(int(time.time()))

sign = hmac.new(secret, req, hashlib.sha512).hexdigest()
headers = {
'Sign' : sign
'Key' : key
}

response = requests.post(url, params=parameter, headers=headers)

print response.content
