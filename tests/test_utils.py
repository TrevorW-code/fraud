import pytest
import functools
from unittest.mock import MagicMock
from fraud.core.utils import find_placeholders, replace_placeholders
from fraud.utils._decorators import set_module
from fraud.plugins.faker import placeholder_to_faker_func, default_faker_instance

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

def test_replace_placeholders():
    mock_faker = MagicMock()
    mock_faker.name.return_value = 'John Doe'
    
    def custom_faker(x):
        return placeholder_to_faker_func(x, faker_instance=mock_faker)()
    
    def limited_fake_name(x):
        return 'Trevor' if x == 'fake_name' else None

    template = "{fake_name}, please meet {name}"
    out = replace_placeholders(template,methods=[limited_fake_name,custom_faker])
    print(out)
    assert out == {"name": "John Doe","fake_name":"Trevor"}

def test_module_func():
    assert fake_func.__module__ == 'fraud'