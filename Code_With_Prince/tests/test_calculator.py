from Scripts.calculator import add, subtract, multiply, division 
from pytest import mark 


@mark.parametrize("x, y, expected_result", [
    (20, 10, 30),
    (40, 10, 50),
    (30000, 10, 30010),
    (2000, 10, 2010)
])    
def test_add_function(x, y, expected_result): 
    assert add(x, y) == expected_result
    
    
@mark.parametrize("x, y, expected_result", [
    (20, 10, 10),
    (40, 10, 30),
    (30000, 10, 29990),
    (2000, 10, 1990)
])    
def test_subtract_function(x, y, expected_result): 
    assert subtract(x, y) == expected_result
    
@mark.parametrize("x, y, expected_result", [
    (20, 10, 200),
    (40, 10, 400),
    (30000, 10, 300000),
    (2000, 10, 20000)
])    
def test_multiply_function(x, y, expected_result): 
    assert multiply(x, y) == expected_result


@mark.parametrize("x, y, expected_result", [
    (20, 10, 2),
    (40, 10, 4),
    (30000, 10, 3000),
    (2000, 10, 200)
])    
def test_division_function(x, y, expected_result): 
    assert division(x, y) == expected_result