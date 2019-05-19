# -*- coding: utf-8 -*-

"""
Python binary tree.
"""
from typing import Union

__author__ = "Jakrin Juangbhanich"
__email__ = "juangbhanich.k@gmail.com"


class TNode:
    def __init__(self, key: Union[str, int, float], data=None):
        self.left: TNode = None
        self.right: TNode = None
        self.key: Union[str, int, float] = key
        self.data = data


class Tree:
    def __init__(self):
        pass
