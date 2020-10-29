from src.code import solution

#pytest -v test/test_general.py

def test_general():
    assert solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])
    assert solution([[-3,-2,-1,2,10,15,16,18,19,20]])

def test_positive_numbers():
    assert solution([1,2,3,4,5,6,7] == "1-7")

def test_negative_numbers():
    assert solution([-6,-5,-4,-3,-2,-1] == "-6--1")

def test_from_negative_to_positive():
    assert solution([-3,-2,-1,0,1,2,3,4] == "-3-4")

def test_different_groups():
    assert solution([1,2,3,4,6,7,8,10,11,12,13,14] == "1-4,6-8,10-14")
