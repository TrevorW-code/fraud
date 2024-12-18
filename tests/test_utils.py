import pytest
from fraud.core.utils import find_placeholders
from fraud.utils._decorators import set_module

@set_module('fraud')
def fake_func():
    pass

def test_find_placeholders_str():
    sample = 'this is a test {placeholder}'
    assert find_placeholders(sample) == ['placeholder']

def test_find_placeholders_not_supported():
    sample = bytes([65, 66, 67])
    with pytest.raises(NotImplementedError) as e_info:
        find_placeholders(sample)

def test_module_func():
    assert fake_func.__module__ == 'fraud'