#
from merrily import hello


def test_hello():
    assert hello.hello() == "Hello, world!"
