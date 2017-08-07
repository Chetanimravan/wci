# WorldCoinIndex

Fetch crypto currency rate from worldcoinindex.com,example:
```
# coding=utf-8
import WorldCoinIndex

if __name__ == '__main__':
    coin = WorldCoinIndex.Coin(key='feHxid4IFfyrYNJSP4k9aNQdz')
    wallet = {'LTC': 15.5778, 'DOGE': 100000, 'NMC': 0.1735, 'XMR': 15.659}
    cny_balance = 0
    for crypto in wallet:
        cny_balance += coin.get_cny_value_of(crypto, 'CNY') * wallet[crypto]
    print(cny_balance)

```
Per worldcoinindex.com's term,API request are restricted to 1 API KEY per IP and a maximum of 70 requests per hour.

 Please get your free api here:
[https://www.worldcoinindex.com/apiservice](https://www.worldcoinindex.com/apiservice)