# About

This is the home of Aplos API samples written in Python.

`api_main.py` is a basic example of the flow to request a token
and decrypt it with your private key followed by an API request.

## Private Key

Save your downloaded private key as `private.key` in the project root and surround the key data 
with the following:

```
-----BEGIN PRIVATE KEY-----
key data
-----END PRIVATE KEY-----
```

## key.cfg

Create `key.cfg` from the template file and replace `key` with your Aplos client ID.

## References

* [Requests HTTP Library](https://2.python-requests.org/en/master/)
* [Cryptography Library](https://cryptography.io/en/latest/)
