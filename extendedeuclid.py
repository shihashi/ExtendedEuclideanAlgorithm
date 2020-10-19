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

import sys


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


def main():
    if(len(sys.argv) != 3):
        sys.exit(1)
    try:
        a, b = int(sys.argv[1]), int(sys.argv[2])
        if a <= 0 or b <= 0:
            raise ValueError("The auguments must be positive integer: '{}' '{}'".format(a, b))
    except ValueError as e:
        print(e, file = sys.stderr)
        sys.exit(1)
    gcd, x, y = extended_euclid(a, b)
    print("{}x({})+{}x({})={}".format(a, x, b, y, gcd))


if __name__ == '__main__':
    main()