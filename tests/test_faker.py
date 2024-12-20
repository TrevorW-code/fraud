import pytest
import faker
from unittest.mock import MagicMock
from fraud.plugins.faker import FakerTemplater, FakerGenerator, placeholder_to_faker_func
from fraud.core.base import Template

def test_placeholder_to_faker_func():
    """
    Tests if faker function can be fetched by string
    """
    
    mock_faker = MagicMock()
    mock_faker.name.return_value = 'John Doe'
    faker_func = placeholder_to_faker_func('name', mock_faker)
    assert faker_func() == 'John Doe'

def test_FakerTemplater():
    """
    Tests if FakerTemplate can take an arbitrary string with placeholders and return a value from faker generators.
    """
    mock_faker = MagicMock()
    mock_faker.name.return_value = 'random_name'

    temp = Template('{name} should meet {name}!')
    faker_templator = FakerTemplater(temp, mock_faker)

    out = faker_templator.apply()
    assert out == 'random_name should meet random_name!'

def test_FakerTemplater_invalid_placeholder():
    """
    Tests if invalid faker func raises a ValueError
    """
    real_faker = faker.Faker()

    temp = Template('{nameasd} should meet {nameasd}!')
    faker_templator = FakerTemplater(temp, real_faker)

    with pytest.raises(ValueError) as e_info:
        faker_templator.apply()
    
def test_FakerGenerator():
    mock_faker = MagicMock()
    mock_faker.name.return_value = 'random_name'
    mock_faker.time.return_value = 'random_time'

    temp = Template('Hey {name}, are you free for a call at {time}?')
    faker_generator = FakerGenerator(temp, mock_faker)
    out_one = faker_generator.make() # make one
    out_two = faker_generator.make(5) # make five
    
    assert out_one == 'Hey random_name, are you free for a call at random_time?'
    assert out_two == ['Hey random_name, are you free for a call at random_time?'] * 5

# def test_get_faker_value():
#     get_faker_value("name",mock_faker)

def test_FakerGenerator_invalid_placeholder():
    real_faker = faker.Faker()

    temp = Template('Hey {asd}, are you free for a call at {asd}?')
    faker_generator = FakerGenerator(temp, real_faker)

    with pytest.raises(ValueError) as e_info:
        faker_generator.make(5) # make five