import pytest
from fraud.utils import find_placeholders

def test_find_placeholders_str():
    sample = 'this is a sample {placeholder}'
    assert find_placeholders(sample) == ['placeholder']

def test_find_placeholders_not_supported():
    sample = 123
    with pytest.raises(NotImplementedError) as e_info:
        find_placeholders(sample)