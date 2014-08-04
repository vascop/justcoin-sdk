# Justcoin Python API

Install the sdk:

	pip install justcoin-sdk


Get your API key from [Justcoin](https://justcoin.com/client/#settings/apikeys) and then just do:

	import justcoin-sdk
    api = JustcoinAPI("my-api-key")
    print api.list_markets()


You can get a list of available endpoints and their explanations from a mixture of the [old docs](http://docs.justcoin.apiary.io/) and the [new docs](http://wiki.justcoin.com/API). I find the old docs to be more comprehensive.

Have fun