import pytest
@pytest.fixture() # this is to introduce precondition and postcondion
def Calculate(): # Note that the function name does not begin with test since its not a test case. Calculate () is used as a fixture here
    print("Before hook is running") # this will run first. This is the before hook

    yield #yeild is to introduce post condition or tearDown/after hook
    print("After hook is running")

@pytest.fixture(scope="class") # this is to introduce precondition and postcondion
def Greetings(): # Note that the function name does not begin with test since its not a test case. Calculate () is used as a fixture here
    print("Good morning from Before") # this will run first. This is the before hook

    yield #yeild is to introduce post condition or tearDown/after hook
    print("Good night from After")