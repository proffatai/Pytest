def test_Message(Calculate): #Note that we passed the fixture to the main test case
    print("I am the main test from the second test file") # This is the main test


#Note: Calculate() was created inside the conftest file so we can call the method name anywhere in our test case
#Run the code from the location of the file on cmd by using `pytest -v -s`