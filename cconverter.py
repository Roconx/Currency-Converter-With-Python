import requests
import json
from functools import lru_cache


# write your code here!

@lru_cache()
def request(currency):
    global i
    i = not i
    r = requests.get("http://www.floatrates.com/daily/" + currency + ".json")
    r_json = r.json()
    if currency == "usd":
        return r_json["eur"]["rate"]
    return r_json["usd"]["rate"]


def conversion(x, y, z, currency):
    return f"You received {(x * y) / z} {currency.upper()}"


i = True
# 0.311202
# 0.009240
# 0.310908 * 0,00851209
# 3,213346957924435 * 117,479960855677043
eur = request("usd")
usd = request("eur")
second_currency = "a"
first_currency = input().lower()
f_exchange_rate = request(first_currency)
if first_currency == "usd":
    f_exchange_rate = 1
running = True
while running:
    aux = i
    second_currency = input().lower()
    if second_currency == "":
        running = False
        continue
    s_exchange_rate = request(second_currency)
    amount = float(input())
    print("Checking the cache...")
    if aux == i:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
    # if cache else no cache
    if second_currency != "usd":
        s_exchange_rate = 1 / s_exchange_rate
        print(conversion(s_exchange_rate, amount, 1 / f_exchange_rate, second_currency))
    else:
        s_exchange_rate = 1
        print(conversion(f_exchange_rate, amount, s_exchange_rate, second_currency))




