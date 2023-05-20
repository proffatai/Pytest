## Passing data from conftest to our test case
In our conftest file, we can create a fixture that returns any data we wanna
pass in form of a list then we can access those returned data by passing a variable to hold
what is being returned

Quick Note: In our test file `test_fixtures.py`, we did not explicitly import
the fixture file into our script `@pytest.mark.usefixtures("myData")` and `@pytest.mark.usefixtures("myData")`
were not used.Both myData and occupation were imported implicitly
The only catch here is that, we are using fixtures for the purpose of data readability and not as hooks as in Before() or After() operation