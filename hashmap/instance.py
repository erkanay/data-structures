#!/usr/bin/python
# -*- coding: utf-8 -*-

from hashmap import HashMap

h = HashMap(4)  #  4 cells

h.add('erkan', '444-44-44')
h.add('maxime', '333-33-33')
h.add('bob', '555-55-55')
h.add('mike', '666-66-66')
h.add('aude', '777-77-77')
h.add('kosta', '888-88-88')

h.get('mike')
h.delete('bob')

h.show()
