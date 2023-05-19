import pytest
@pytest.fixture() # this is to introduce precondition and postcondion
def Calculate(): # Note that the function name does not begin with test since its not a test case. Calculate () is used as a fixture here
    print("Before hook is running") # this will run first. This is the before hook

    yield #yeild is to introduce post condition or tearDown/after hook
    print("After hook is running")

def test_Message(Calculate): #Note that we passed the fixture to the main test case
    print("I am the main test without any mark and I will run second") # This is the main test


#NOTE: The yeild is like after. Any code that is written after yeild keyword will execute last

## Run the code from the location of the file on cmd by using `pytest -v -s`