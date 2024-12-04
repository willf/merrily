# test the hello function

from merrily.hello import hello


def test_hello():
    assert hello() == "Hello, world!"
