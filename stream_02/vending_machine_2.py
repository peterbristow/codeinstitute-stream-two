from decimal import Decimal

coins = [1, .50, .20, .10, .05, .02, .01]
coins_in_stock = [1, .50, 0.1, 0.05, 0.02, 0.01]

available_items = {
    'coke': .73,
    'biscuits': 1.15,
    'apple': .43
}

def give_change(amount):
    change = []
    amount = Decimal(str(amount))
    for coin in coins:
        if coin in coins_in_stock: # check coin stock
            coin = Decimal(str(coin))
            while coin <= amount:
                amount -= coin
                change.append(float(coin))
    return change


def give_item_and_change(item, coins_given):
    coin_list = coins_given.split()
    float_list = [float(i) for i in coin_list]
    amount = sum(float_list)

    if item not in available_items:
        amount *= 0.9
        return None, amount, "that item isn't available. here is your change less a 10% admin fee :-)"

    cost = available_items[item]

    if amount < cost:
        return None, amount, 'not enough money'

    change_to_return = amount - cost
    coins = give_change(change_to_return)
    return item, coins, "here's your change"

if __name__ == '__main__':
    while True:
        item = raw_input('choose item: %s: ' % available_items)
        coins_given = raw_input('enter the coins tendered. e.g. 1.00 1.00 0.50 0.02 0.02 0.01 ')
        print give_item_and_change(item, coins_given)
