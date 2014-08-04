Justcoin Python API
===================

Install the sdk:

::

    pip install justcoin-sdk


Get your API key from `Justcoin <https://justcoin.com/client/#settings/apikeys>`_ and then just do:

::

    from justcoin import justcoin
    api = justcoin.JustcoinAPI("my-api-key")
    print api.list_markets()


You can get a list of available endpoints and their explanations from a mixture of the `old docs <http://docs.justcoin.apiary.io/>`_ and the `new docs <http://wiki.justcoin.com/API>`_. I find the old docs to be more comprehensive.

Have fun