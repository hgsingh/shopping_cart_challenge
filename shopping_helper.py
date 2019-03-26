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
import ast


node_map = {}
# to help you get started, we have provided some boiler plate code
def satisfy_shopping_list(shopping_list_json, inventory_json):
    # find out minimum combination of stores that would satisfy shopping list
    stores = inventory_json["stores"]
    stores_list = []
    #initialize node map
    for store in stores:
        stores_list.append(store['name'])
        #visited_nodes[store["name"]] = False
    for store in stores_list:
        node_set = set(stores_list)
        node_map[store] = set(node_set - set([store]))
    print node_map
    # for stores in inventory_list: #every store is treated as a node here
    #     while isShoppingListSatisfied(shopping_list_json) is False: # check here whether the 

    # if shopping list is impossible to satisfy
    shopping_list_satisfiable = False
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
        shopping_list_json[key] = quantity - inventory



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

def json_load_byteified(file_handle):
    return _byteify(
        json.load(file_handle, object_hook=_byteify),
        ignore_dicts=True
    )

def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data

def main():
    args = parse_args()
    with open(args.shopping_list_json_path) as shopping_list_json_file, open(args.inventory_json_path) as inventory_json_file:
        shopping_list_json = json_load_byteified(shopping_list_json_file)
        inventory_json = json_load_byteified(inventory_json_file)
        satisfy_shopping_list(shopping_list_json, inventory_json)


def parse_args():
    p = argparse.ArgumentParser()

    p.add_argument('shopping_list_json_path')
    p.add_argument('inventory_json_path')

    args = p.parse_args()
    return args


if __name__ == '__main__':
    main()
