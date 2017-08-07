# coding=utf-8
import WorldCoinIndex

if __name__ == '__main__':
    coin = WorldCoinIndex.Coin(key='feHxid4IFfyrYNJSP4k9aNQdz')
    wallet = {'LTC': 15.5778, 'DOGE': 100000, 'NMC': 0.1735, 'XMR': 15.659}
    cny_balance = 0
    for crypto in wallet:
        cny_balance += coin.get_cny_value_of(crypto, 'CNY') * wallet[crypto]
    print(cny_balance)
