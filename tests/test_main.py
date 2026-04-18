import pytest
from polynomial import add_polynomials, multiply_polynomials

def test_add_polynomials():
    poly1 = [(2, 3), (1, 2), (3, 1)]
    poly2 = [(1, 3), (2, 2), (4, 1)]
    result = add_polynomials(poly1, poly2)
    assert result == [(3, 3), (3, 2), (7, 1)]

def test_multiply_polynomials():
    poly1 = [(2, 3), (1, 2), (3, 1)]
    poly2 = [(1, 3), (2, 2), (4, 1)]
    result = multiply_polynomials(poly1, poly2)
    assert result == [(2, 6), (4, 5), (7, 4), (4, 3), (11, 2), (14, 1)]

def test_add_polynomials_empty():
    poly1 = []
    poly2 = [(1, 3), (2, 2), (4, 1)]
    result = add_polynomials(poly1, poly2)
    assert result == [(1, 3), (2, 2), (4, 1)]

def test_multiply_polynomials_empty():
    poly1 = []
    poly2 = [(1, 3), (2, 2), (4, 1)]
    result = multiply_polynomials(poly1, poly2)
    assert result == []

def test_add_polynomials_same_degree():
    poly1 = [(2, 3), (1, 2), (3, 1)]
    poly2 = [(2, 3), (1, 2), (3, 1)]
    result = add_polynomials(poly1, poly2)
    assert result == [(4, 3), (2, 2), (6, 1)]

def test_multiply_polynomials_same_degree():
    poly1 = [(2, 3), (1, 2), (3, 1)]
    poly2 = [(2, 3), (1, 2), (3, 1)]
    result = multiply_polynomials(poly1, poly2)
    assert result == [(4, 6), (4, 5), (7, 4), (4, 3), (11, 2), (14, 1)]
