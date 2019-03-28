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


minimum_number_to_visit = list()
# to help you get started, we have provided some boiler plate code
def satisfy_shopping_list(shopping_list_json, inventory_json):
    # find out minimum combination of stores that would satisfy shopping list
    stores = inventory_json['stores']
    stores_with_scores = {}
    #initialize node map
    for store in stores:
        current_score = find_score(store['inventory'], shopping_list_json)
        if current_score > 0:
            stores_with_scores[store['name']] = current_score
    combo = find_store_combos(stores_with_scores, stores, shopping_list_json)
    shopping_list_satisfiable = len(combo) > 0
    if shopping_list_satisfiable:
        # print out number of stores and corresponding combinations
        num_stores = len(combo) 
        print "The shopping list can be satisfied by visiting {} store(s):".format(num_stores)
        print_store_combination(combo)
        pass
    else:
        print "No combination of given stores can satisfy this shopping list :("
        pass
def find_store_combos(scores, stores, shopping_list):
    combo = []
    print shopping_list
    for key in sorted(scores.items(), key=lambda x: x[1], reverse=True): #start with the highest scores first
        for store in stores:
            if is_shopping_list_satisfied(shopping_list):
                break
            elif key[0] == store['name']:
                print shopping_list
                if decrement_shopping_list(store['inventory'], shopping_list):
                    combo.append(key[0])
        if is_shopping_list_satisfied(shopping_list): break
    print combo
    print shopping_list
    return combo

def find_score(store, shopping_list):
    score = 0
    for item in shopping_list:
        for inventory in store:
            if item == inventory:
                score = score  + 1
                if store[inventory] >= shopping_list[item]:
                    score = score + 10
    return score


def compare_distance(satisfiable_list):
    global minimum_number_to_visit
    if not minimum_number_to_visit:
        minimum_number_to_visit = copy.deepcopy(satisfiable_list)
        return
    if len(satisfiable_list) < len(minimum_number_to_visit):
        minimum_number_to_visit = copy.deepcopy(satisfiable_list)
    
def is_shopping_list_satisfied(shopping_list_json):
    for key in shopping_list_json:
        if shopping_list_json[key] != 0:
            return False
    return True

def decrement_shopping_list(inventory, shopping_list):
    item_found = False
    for item in shopping_list:
        if item in inventory and shopping_list[item] > 0:
            if inventory[item] >= shopping_list[item]:
                item_found = True
                shopping_list[item] = 0
    return item_found



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
