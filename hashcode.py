#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pprint import pprint

def hashcode(path):
# http://garage.pimentech.net/libcommonPython_src_python_libcommon_javastringhashcode/
# 这个hashCode的方法略为碉堡,
    h = 0
    for c in path:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    hash_code =  ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000
    return hash_code

def hashcode_2(path):
    return path

if __name__ == "__main__":
    pprint(hashcode('lkjljlkjljk'))
    pprint(hashcode_2('lkjljlkjljk'))

