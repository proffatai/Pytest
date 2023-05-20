import pytest

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
    assert 11*num == output


#in this example, num reps the first number in the turple while output is paired with the second number
