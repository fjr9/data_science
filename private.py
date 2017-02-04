import requests
import hmac
import hashlib
import time

url = 'https://vip.bitcoin.co.id/tapi/'
key = 'MYLKGOG6-34NVQVPW-KH11EJBY-JXX0KMLV-BEMBVZ2V'
secret = 'a4d1668f6cc9f5ee9b7256d2072b7bbba87bcf93d55db881a1ddcefbcd76832c396ce78360e13260'
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
