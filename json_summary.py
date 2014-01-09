#!/usr/bin/env python

""" Prints out a summary of JSON object structure."""

import json
import argparse

PADDING = '----'

def traverse_json(json_obj,explode_lists,explode_to_level,level=0):
    if (type(json_obj) is dict):
        for key in json_obj:
            # what type value for the key is
            print "%s%s %s" % (PADDING * level, key, type(json_obj[key]))
            traverse_json(json_obj[key],explode_lists,explode_to_level,level+1)
    elif type(json_obj) is list:
        l = len(json_obj)
        print "%slist of length %d" % (PADDING * level, l)
        if l > 0:
            # descend into lists only if we explode them and desired level
            # is not yet reached
            scan_to = l-1 if explode_lists and level < explode_to_level else 1
            for i in  range(0, scan_to):
                print "%s%s" % (PADDING * level, type(json_obj[i]))
                traverse_json(json_obj[i],explode_lists,explode_to_level,level + 1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Summarize JSON objects')
    parser.add_argument("--explode-lists",dest="explode_lists",\
                        action="store_true", help="Parse structure for each item of in all lists")
    parser.add_argument("--explode-to-level", dest="explode_to_level",\
                        type=int, default=2, help="Only dive into lists till this level")
    parser.add_argument('path', help="path to json file")
    args = parser.parse_args()

    json_file = open(args.path,'r')
    json_dict = json.load(json_file)

    traverse_json(json_dict,args.explode_lists,args.explode_to_level)
