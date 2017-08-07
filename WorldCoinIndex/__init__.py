# coding=utf-8
import requests
import json


class Coin(object):
    def __init__(self, key: str):
        self._fetch_url = "https://www.worldcoinindex.com/apiservice/json?key={key}".format(key=key)
        self.raw_data = None
        self.data = None
        self.update_data()

    @staticmethod
    def data_read(raw_data: dict):
        data_dict = dict()
        for crypto in raw_data['Markets']:
            data_dict[crypto['Label'].split('/')[0]] = crypto
        return data_dict

    def update_data(self):
        self.raw_data = json.loads(requests.get(self._fetch_url).content)
        self.data = self.data_read(self.raw_data)

    def get_value_of(self, crypto: str, fiat: str):
        return self.data[crypto.upper()]['Price_{}'.format(fiat.lower())]
