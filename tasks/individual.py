#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_combination(m, n):
    if m == 0 or m == n: #базовый случай
        return 1

    if m < 0 or m > n:
        return 0
    
    return calculate_combination(m, n-1) + calculate_combination(m-1, n-1)


if __name__ == '__main__':
    m = int(input('Введите m: '))
    n = int(input('Введите n: '))
    res = calculate_combination(m, n)
    print(f'C({m}, {n}) = {res}')

