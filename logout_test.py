import pytest


@pytest.mark.ibraz
def testFirstMessage():
    print(f"This is for valid calculation")

def test_SecondMessage():
    print("This is for invalid calculation")


