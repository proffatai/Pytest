import pytest

@pytest.fixture(params=[("chrome", "pifa","password"), ("firefox","Fatai"), "edge"]) # 3 params are passed
def crossBrowser(request):
    return request.param