#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Hashmap implementation


"""


class HashMap(object):
    def __init__(self, n):
        self.size = n
        self.map = [None] * n

    def _get_hash(self, key):
        hash = 0
        for chr in key:
            hash += ord(chr)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def swap(self, f_key, s_key):
        f_key_hash = self._get_hash(f_key)
        s_key_hash = self._get_hash(s_key)
        temp = None
        if self.map[f_key_hash] is not None:
            if self.map[s_key_hash] is not None:
                temp = self.map[f_key_hash]
                self.map[f_key_hash] = self.map[s_key_hash]
                self.map[s_key_hash] = temp
                return True
        return False

    def show(self):
        for item in self.map:
            if item is not None:
                print(str(item))
