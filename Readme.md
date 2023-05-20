## Working on different environments
Assuming we want to run our test script in different envs for example say in 
different browsers.

we can create a fixture and pass params=[env] as the argument. While creating 
the fixture method, we have to pass `request` which will be used to access each 
value inside the params via `request.param`