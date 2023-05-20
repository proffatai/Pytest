import pytest
@pytest.fixture()  #this declares the method as a fixture
def myData():
    print("Returning personal record................")
    return ["Ibrahim","Fatai","proffatai@gmail.com"]

@pytest.fixture()  #this declares the method as a fixture
def occupation():
    print("Returning occupation record................")
    return ["QA Engineer","Babban Gona","Gitstart"]