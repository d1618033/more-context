from more_context import safe_context_manager
import pytest


@safe_context_manager
def ctx():
    """Documentation"""
    x = {"start": True}
    yield x
    x["cleanup"] = True


def test_no_error():
    with ctx() as x:
        assert x["start"]
        x["middle"] = True
    assert x["middle"]
    assert x["cleanup"]


def test_error():
    with pytest.raises(ValueError, match="Failure"), ctx() as x:
        assert x["start"]
        x["middle"] = True
        raise ValueError("Failure")
    assert x["middle"]
    assert x["cleanup"]


def test_func_attributes_preserved():
    assert ctx.__doc__ == "Documentation"
    assert ctx.__name__ == "ctx"


def test_bad_func_two_yields():
    @safe_context_manager
    def ctx():
        yield 1
        yield 2

    with pytest.raises(RuntimeError, match="generator didn't stop"):
        with ctx():
            pass
