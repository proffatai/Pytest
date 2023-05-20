#METHOD 1
import pytest
def test_case(myData): #Note that we passed the fixture to the main test case
    print(myData)
    print(myData[0])
    print(myData[2])

#METHOD 2: Using class
class Test:
    def test_case(self,occupation):  #We passed another argument 'occupation' to the function because we wanna
                                # hold the returned data coming from the fixture in a variable so we can use it later on
        print(occupation)
        print(occupation[1])
#NB: If we were not going to get data from the conftest file, we need not include the extra parameter, self is sufficient
#enough for us to access whatever we had written inside the conftest file