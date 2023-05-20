import pytest
@pytest.mark.usefixtures("Greetings")
class Test:
    def test_case1(self): #Note that we passed the fixture to the main test case
        print("I am the test case 1") # This is the main test
    def test_case2(self): #Note that we passed the fixture to the main test case
        print("I am the test case 2") # This is the main test
    def test_case3(self): #Note that we passed the fixture to the main test case
        print("I am the test case 3") # This is the main test
    def test_case4(self): #Note that we passed the fixture to the main test case
        print("I am the test case 4") # This is the main test



#Note: Greetings() was created inside the conftest file so we can call the method name anywhere in our test case
#Run the code from the location of the file on cmd by using `pytest -v -s`