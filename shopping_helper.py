#!/usr/bin/env python
'''
Shopping Helper

Given a list of store inventories and a shopping list, return the minimum number of
store visits required to satisfy the shopping list.

For example, given the following stores & shopping list:

  Shopping List: 10 apples, 4 pears, 3 avocados, 1 peach

  Kroger: 4 apples, 5 pears, 10 peaches
  CostCo: 3 oranges, 4 apples, 4 pears, 3 avocados
  ALDI: 1 avocado, 10 apples
  Meijer: 2 apples

The minimum number of stores to satisfy this shopping list would be 3:
Kroger, CostCo and ALDI.
or
Kroger, CostCo and Meijer.

Shopping lists and store inventories will be passed in JSON format,
an example of which will be attached in the email.  Sample outputs for the
given inputs should also be attached as well.

Usage: shopping_helper.py (shopping_list.json) (inventories.json)
'''

import argparse
import copy
import json

store_pairs = [][] #map which lists keys as the number of vertices and pairs of lists 

# to help you get started, we have provided some boiler plate code
def satisfy_shopping_list(shopping_list_json, inventory_json):
    # find out minimum combination of stores that would satisfy shopping list
    inventory_list = inventory_json["stores"]
    for stores in inventory_list: #every store is treated as a node here
        while isShoppingListSatisfied(shopping_list_json) is False: # check here whether the 

    # if shopping list is impossible to satisfy
    shopping_list_satisfiable = True
    if shopping_list_satisfiable:
        # print out number of stores and corresponding combinations
        # num_stores = 0
        # print "The shopping list can be satisfied by visiting {} store(s):".format(num_stores)
        # for each valid store_combination:
        # print_store_list(store_combination)
        pass
    else:
         print "No combination of given stores can satisfy this shopping list :("
        pass

def isShoppingListSatisfied(shopping_list_json):
    for key in shopping_list_json:
        if shopping_list_json[key] != 0:
            return False
    return True

def decrementShoppingList(key, shopping_list_json, inventory):
    quantity = shopping_list_json[key]
    if inventory > quantity :
        shopping_list_json[key] = 0
    else:
        shopping_list_json[key] = quantity - inventory;


def print_store_combination(store_combination):
    '''
    Print store combination in the desired format.

    Args:
        store_combination: store list to print
        type: list of str
    '''
    store_combination_copy = copy.deepcopy(store_combination)
    store_combination_copy.sort()
    print ', '.join(store_combination_copy)


def main():
    args = parse_args()
    with open(args.shopping_list_json_path) as shopping_list_json_file, open(args.inventory_json_path) as inventory_json_file:
        shopping_list_json = json.load(shopping_list_json_file)
        inventory_json = json.load(inventory_json_file)
        satisfy_shopping_list(shopping_list_json, inventory_json)


def parse_args():
    p = argparse.ArgumentParser()

    p.add_argument('shopping_list_json_path')
    p.add_argument('inventory_json_path')

    args = p.parse_args()
    return args

if __name__ == '__main__':
    main()
