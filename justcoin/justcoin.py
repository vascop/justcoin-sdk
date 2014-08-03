import requests
import json


class JustcoinAPI():

    def __init__(self, API_KEY):
        self.base = "https://justcoin.com/api/v1"
        self.key = "?key=" + API_KEY

    def list_markets(self):
        return self._request("/markets")

    def get_market(self, market):
        return self._request("/markets/" + market + "/depth")

    def list_orders(self):
        return self._request("/orders")

    def create_order(
            self, market, amount,
            price=None, type="bid", aon=False):
        payload = {
            'market': str(market),
            'amount': str(amount),
            'price': str(price),
            'type': str(type),
            'aon': str(aon)
        }
        return self._request("/orders", payload)

    def cancel_order(self, id):
        return self._request("/orders/" + str(id), type="DELETE")

    def list_balances(self):
        return self._request("/balances")

    def list_invoices(self):
        return self._request("/invoices")

    def get_invoice(self, id):
        return self._request("/invoices/" + str(id))

    def create_invoice(
            self, amount, currency,
            orderId=None,
            settleCurrency="currency",
            merchantData=None):
        pass

    def create_merchant_invoice(
            self, merchantKey, amount, currency,
            orderId=None,
            merchantData=None):
        pass

    def _request(self, endpoint, type="GET", payload=None):
        if type == "GET":
            r = self._get(endpoint)
        elif type == "POST":
            r = self._post(endpoint, payload)
        elif type == "DELETE":
            r = self._delete(endpoint)

        return r.json()

    def _delete(self, endpoint):
        url = self.base + endpoint + self.key
        return requests.delete(url)

    def _post(self, endpoint, payload):
        url = self.base + endpoint + self.key
        return requests.post(
            url,
            data=json.dumps(payload),
            headers={'content-type': 'application/json'})

    def _get(self, endpoint):
        url = self.base + endpoint + self.key
        return requests.get(url)
