#!/usr/bin/env python

""" Prints out a summary of JSON object structure.
    Currently assumes that all objects in a given list
    have the same structure, so it recursevely reads only
    the first element. This may be too optimistic and if
    it's not true in your case you are in schema hell anyway
"""

import json
import argparse

def traverse_json(json_obj,padding=''):
    if (type(json_obj) is dict):
        for k in json_obj:
            print "%s%s %s" % (padding, k, type(json_obj[k]))
            traverse_json(json_obj[k], padding+'----')
    elif type(json_obj) is list:
        print "%slist of length %d" % (padding, len(json_obj))
        if len(json_obj) > 0:
                print "%s%s" % (padding, type(json_obj[0]))
                traverse_json(json_obj[0], padding+'----')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Summarize JSON objects')
    parser.add_argument('path', help="path to json file")
    args = parser.parse_args()

    json_file = open(args.path,'r')
    json_dict = json.load(json_file)

    traverse_json(json_dict)
