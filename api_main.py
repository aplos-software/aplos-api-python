#!/usr/bin/python3
import requests
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import configparser as cp
import base64

config_file = 'key.cfg'
key_file = 'private.key'
aplos_domain = "app.aplos.com"
auth_route = "hermes/api/v1/auth"
accounts_route = "hermes/api/v1/accounts"
payables_route = "hermes/api/v1/payables"


if __name__ == "__main__":
    config = cp.ConfigParser()
    config.read(config_file)
    key = config['Aplos']['key']
    with open(key_file, 'rb') as k:
        api_request = '{}://{}/{}/{}'.format('https', aplos_domain, auth_route, key)
        print("request: {}".format(api_request))

        r = requests.get(api_request)
        if r.status_code == 200:
            token = r.json()['data']['token']
            print("response: {}".format(r.json()))
            print("token: {}".format(token))

        private_key = serialization.load_pem_private_key(
            k.read(),
            password=None,
            backend=default_backend()
        )

    token64 = base64.b64decode(token)
    decryptToken = private_key.decrypt(token64, padding.PKCS1v15())
    decryptTokenUtf8 = str(decryptToken, 'utf-8')
    print("decrypted token: {}".format(decryptTokenUtf8))
        
    accounts = '{}://{}/{}'.format('https', aplos_domain, payables_route)
    h = {'Authorization':'Bearer {}'.format(decryptTokenUtf8)}

    # JSON format response
    response = requests.get(accounts, headers=h, params={"page_size": 2, "page_num": 1})
    print('Status code: {}'.format(response.status_code))
    print('Response data:\n{}'.format(response.text))
