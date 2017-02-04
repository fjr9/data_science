import requests
import hmac
import hashlib
import time

url = 'https://vip.bitcoin.co.id/tapi/'
key = 'my_api_key'
secret = 'my_token_secret'
method = 'getInfo'

post_data = '&method=' + method + '&nonce=' + str(int(time.time()))

sign = hmac.new(secret, post_data, hashlib.sha512).hexdigest()
headers = {
'Sign' : sign
'Key' : key
}

response = requests.post(url, headers=headers)

print response.content
