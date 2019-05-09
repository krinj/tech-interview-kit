#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque


if __name__ == "__main__":
    ll = deque()
    ll.append(5)
    ll.append(6)
    ll.appendleft(7)

    print(len(ll))
    print(ll.pop(), ll.popleft(), ll.popleft())
    print(len(ll))
