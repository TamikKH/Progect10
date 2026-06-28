#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    u = set("abcdefghijklmnopqrstuvwxyz")
    A = {'a', 'b', 'h', 'k', 'o', 'r'}
    B = {'b', 'g', 'h', 'l', 's'}
    C = {'k', 'l', 'z'}
    D = {'g', 'j', 'p', 'q', 'u', 'v'}
    X = (A.intersection(C)).union(B)
    An = u.difference(A)
    Bn = u.difference(B)
    Y = (An.intersection(Bn)).difference(C.union(D))
    print(f"множество x равно {X}")
    print(f"множество y равно {Y}")
