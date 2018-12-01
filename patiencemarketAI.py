# -*- coding: utf-8 -*-
"""

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University

Program framework for artificially intelligent "patience" to wait for better deals in a market

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Patience Electronic Bartering Platform [Computer software]. Github repository <https://github.com/alanjpan/Patience-Electronic-Bartering-Platform>

Note this software's license is GNU GPLv3.
"""

inventory = [('laptop', 300), ('laptop', 325), ('bed', 75), ('bed', 70), ('television', 150), ('television', 150), ('suv', 20000), ('suv', 18000), ('suv', 17750), ('bed', 75)]
order = [('laptop', 600), ('laptop', 650), ('laptop', 550), ('bed', 155), ('bed', 140), ('bed', 150), ('television', 590), ('suv', 30000), ('suv', 32000)]
sold = []
cash = 0

def transaction():
    global cash
    global sold

    inventorysort = []
    ordersort = []
    inventorysort = sorted(inventory, key=lambda inventory_entry: inventory_entry[1])
    ordersort = sorted(order, key=lambda order_entry: order_entry[1], reverse=True)

    for i in inventorysort:
        for j in ordersort:
            if i[0] == j[0]:
                if i[1] < j[1]:
                    collect = j[1] - i[1]
                    cash += collect
                    ordersort.remove(j)
                    sold.append(i)
                    print(str(i[0]) + ' sold for ' + str(collect) + ' cash')
                    break
    for i in sold:
        if i in inventorysort:
            inventorysort.remove(i)
    sold.clear()
    print('remaining inventory: ' + str(inventorysort))
    print('final cash: ' + str(cash))

