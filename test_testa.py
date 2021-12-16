from programma import minimal, maximal, product_float, summa, product_int, product_float_decimal, speed, sovpadenie
import pytest


def test_maximal():
    assert maximal([1, 2, 3, 2, 4, 5, 6]) == 6
    assert maximal([-10, -459, 452, 543.23, 0]) == 543.23
    assert maximal([-122, -1335352, 1, 89, 1000000000, -122.1]) == 1000000000


def test_minimal():
    assert minimal([1, 2, 3, 2, 4, 5, 6, -3]) == -3
    assert minimal([-100, -3449, 2142, 5243.23, 0]) == -3449
    assert minimal([-22, -15352, -4, 9, 10000000, -12200.1]) == -15352


def test_product_float():
    assert product_float([-1, 130, 200, 1]) == -26000
    assert product_float([1, -42, 5.4, 2.111]) == -478.7748000000001
    assert product_float([222, 5, 6987, -45.44, 334]) == -117705975667.2


def test_summa():
    assert summa([1, 2, 3, 4, 5]) == 15
    assert summa([10.12, 21.44, 122.33]) == 153.89
    assert summa([145, 345.032, 1353, 743.213]) == 2586.245

def test_sovpadenie():
    assert sovpadenie([3, 3, 3, 3, 3]) == True
    assert sovpadenie([1, 1, 3, 1, 1]) == False
    assert sovpadenie([2, 2]) == True
