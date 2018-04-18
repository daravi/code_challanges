# -*- coding: utf-8 -*-
"""
Coin sums:
Problem 31
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

list_coin_sums = []
counter = 0

def get_coin_sums(goal, coins_list, amount):
    #for coin in reversed(coins_list_copy):
    global list_coin_sums
    global counter
    coin_sums = []
    coin = coins_list[-1]
    #if amount == 0:
    #    counter += 1
    #    #list_coin_sums.append(['hey'])
    #    return ['hey amount 0']
    if len(coins_list) == 1:
        #print [(coin, amount / coin)]
        #list_coin_sums.append(['hey'])
        counter += 1
        return[(coin, amount / coin), 'hey last coin']
    
    else:
        for number_biggest_coin in range(amount/coin + 1):
            new_coins_list = list(coins_list)
            new_coins_list.pop()
            coin_sums += [(coin, number_biggest_coin)]
            coin_sums += get_coin_sums(goal, new_coins_list, amount - number_biggest_coin * coin)
            if amount == goal:
                if not coin_sums in list_coin_sums:
                    list_coin_sums.append(coin_sums)
    
    return coin_sums

        
get_coin_sums(200, [1, 2, 5, 10, 20, 50, 100, 200], 200)
print counter
#print list_coin_sums
           

def get_coin_sums_max(amount, coins_list):
    coin_sums_list = []
    coin_sums = []
    coins_list_copy = list(coins_list)
    while len(coins_list_copy):
        #print "top: ", len(coins_list_copy)
        for coin in reversed(coins_list_copy):
            #print coin
            #print "hey"
            #print "here0", amount, coins_list_copy
            if coin > amount:
                #print coins_list
                new_coins_list = list(coins_list_copy)
                new_coins_list.pop()
                #print "here", amount, coins_list_copy
                #print new_coins_list, amount, "c > a"
                coin_sums = get_coin_sums_max(amount, new_coins_list)
                #print "here2", amount, coins_list_copy
            else:
                #print coins_list, amount, "c <= a"
                lst = get_coin_sums_max(amount - coin, coins_list_copy)
                #print "lst", lst
                lst.append(coin)
                #coin_sums.append(lst)
                coin_sums = lst
        coin_sums_list += coin_sums
        print coin_sums
        #print "buttom: ", len(coins_list_copy)
        coins_list_copy.pop()
    #print "before return", coin_sums
    return coin_sums


def coin_sums(amount, coins_list):
    sorted_coins_list = sorted(coins_list)
    #for coin in reversed(sorted_coins_list):
    #    coin_sums.appendget_coin_sums_max(amount, sorted_coins_list)
    return get_coin_sums_max(amount, sorted_coins_list)

#print coin_sums()

#print get_coin_sums(10, [1,2], 10)



#
#
#while len(coins):
#    get_max_coins
#    pop max coin
#    
#    for coin in reversed(coins_list):
#        #print coin
#        #print "hey"
#        if coin > amount:
#            #print coins_list
#            new_coins_list = coins_list
#            new_coins_list.pop()
#            #print new_coins_list, amount, "c > a"
#            return get_coin_sums_max(amount, new_coins_list)
#        else:
#            #print coins_list, amount, "c <= a"
#            lst = get_coin_sums_max(amount - coin, coins_list)
#            #print "lst", lst
#            lst.append(coin)
#            #coin_sums.append(lst)
#            return lst
#    
















