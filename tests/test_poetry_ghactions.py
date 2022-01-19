import poetry_ghactions


def test_version():
    assert poetry_ghactions.__version__ == "0.1.0"


def test_say_something():
    assert "something" == poetry_ghactions.say_something()
