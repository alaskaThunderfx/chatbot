import requests
import json


cache = {}

change_from = input()
change_to = input()
r = requests.get('http://www.floatrates.com/daily/{}.json'.format(change_from.lower()))
new_r = json.loads(r.content)


if change_from == 'usd':
    cache['usdeur'] = new_r['eur']
elif change_from == 'eur':
    cache['eurusd'] = new_r['usd']
else:
    cache['{}usd'.format(change_from)] = new_r['usd']
    cache['{}eur'.format(change_from)] = new_r['eur']


upd = change_from + change_to


while True:
    if len(change_to) != 0:
        amt = float(input())
        print('Checking the cache...')
        if upd in cache:
            print('Oh! It is in the cache!')
            print('You received ' + str(
                round(amt * float(cache[upd]['rate']), 2)) + ' ' + change_to.upper() + '.')
            change_to = input()
            upd = change_from.lower() + change_to
        else:
            print('Sorry, but it is not in the cache!')
            r = requests.get('http://www.floatrates.com/daily/{}.json'.format(change_from.lower()))
            new_r = json.loads(r.content)
            cache[upd] = new_r[change_to]
            print('You received ' + str(
                round(amt * float(cache[upd]['rate']), 2)) + ' ' + change_to.upper() + '.')
            change_to = input()
            upd = change_from.lower() + change_to
    else:
        break
