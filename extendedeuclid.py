#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# extendedeuclid.py
#
# Copyright (c) 2020 Shinya Hashimoto
#
# Released under the MIT license.
# see https://opensource.org/licenses/mit-license.php
#

def extended_euclid(a, b):
    '''Get a  greatest common divisor of a and b, and get a special solution of ax+by=gcd(a,b).
Returns: (gcd, x, y)
'''
    r0, r1 = a, b
    x0, y0 = 1, 0
    x1, y1 = 0, 1
    while True:
        q = r0 // r1
        r0, r1 = r1, r0 % r1
        if r1 == 0:
            break
        x0, y0, x1, y1 = x1, y1, x0 - x1 * q, y0 - y1 * q
    return r0, x1, y1
