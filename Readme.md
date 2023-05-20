## Use of conftest.py
Assumming we have a fixture file whose content we wish to use across different tests. We can just
create a file with the name `conftest.py` and paste that fixture file there. Then all tests files
(Files whose name starts with `test`) will be able to access whatever is being declared inside the conftest.py

Now we can go to our test file, create our test case and pass the name of the method we created inside the conftest.py
and run it. We can have multiple test cases where we just need to pass the method name we created in the conftest.py file,
and we will be able to invoke whatever we have written in the fixtures file

## Using conftest.py method in multiple test cases as in beforeEach
See the file: `test_fixtures_3`. We had to create a class and pass those multiple test cases as a method
of that class while passing self as an argument to each method. 
We also created a global variable with name equal to that of our fixture in the conftest.py file. 
We created this variable using a marker    `@pytest.mark.usefixtures("nameOfFixtureMethod")`

NB: By passing self into each test case (methods of the class), the argument of usefixtures (nameOfFixtureMethod)
is automatically applied and treated as self

## Using conftest.py method in multiple test cases as in before()
Here, we want to run content of our fixtures file once then run all our test cases and finally
run the after test. Unlike in the previous instance where we ran beforeEach and afterEach test case

To achieve this, we have to pass an argument to our fixture `scope="class"` such that it treats all the 
test cases as one entity and runs them once after running the before method then runs the after method once 
as well after running all the test cases