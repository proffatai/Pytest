import pytest


@pytest.mark.skip
def test_FirstAddition(): #I wanna skip this
    assert 3 + 4 == 7, "invalid result"


@pytest.mark.ibraz
# @pytest.mark.xfail
def test_SecondAddition():
    assert -3 - 4 == 7, "invalid result"

# Note: The assert statement has an else part that is displayed if the assertion fails
