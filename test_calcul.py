from calcul import addition,multiplication,division
import  pytest
def test_add():
    assert addition(2,3)==5

def test_multi():
    assert multiplication(4,3) == 12
def test_divi():
    assert  division(10,2) == 5

def test_division_par_zero():
    with pytest.raises(ValueError):
        division(10,0)