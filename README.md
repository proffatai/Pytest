## Running tests with Markers @pytest.mark
To run only test that has the markerName
`pytest -m markerName -v -s`

To skip: Use the marker `@pytest.mark.skip` on the test case / function you wanna skip
`pytest -v -s` //runs all tests except the skipped one

If we dont want any error log even when there is a failed test case, use:
`# @pytest.mark.xfail` just before the test case