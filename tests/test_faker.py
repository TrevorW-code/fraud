import pytest
import faker
from unittest.mock import MagicMock
from fraud.faker import FakerTemplater, placeholder_to_faker_func
from fraud.base import Template

def test_placeholder_to_faker_func():
    mock_faker = MagicMock()
    mock_faker.name.return_value = 'John Doe'
    faker_func = placeholder_to_faker_func('name', mock_faker)
    assert faker_func() == 'John Doe'

def test_faker_func_to_dict():
    mock_faker = MagicMock()
    mock_faker.name.return_value = 'name'

def test_FakerTemplater():
    mock_faker = MagicMock()
    mock_faker.name.return_value = 'random_name'

    temp = Template('{name} should meet {name}!')
    faker_templator = FakerTemplater(temp, mock_faker)

    out = faker_templator.apply()
    assert out == 'random_name should meet random_name!'

def test_FakerTemplater_invalid_placeholder():
    real_faker = faker.Faker()

    temp = Template('{nameasd} should meet {nameasd}!')
    faker_templator = FakerTemplater(temp, real_faker)

    with pytest.raises(ValueError) as e_info:
        faker_templator.apply()
    