import pytest
from unittest.mock import MagicMock
from fraud.plugins.gliner import (
    replace_word_at_indexes,
    make_template_from_prediction
)

def test_replace_word_at_indexes():
    inp_str = "This is silly!"
    expected_str = "This is cool!"
    out = replace_word_at_indexes(inp_str,8,13,"cool")
    assert out == expected_str

def test_make_template_from_prediction():
    sample = "My name is Trevor Ward and I am a Data Scientist. What are you doing this Monday?"
    entities = [
        {'start': 11, 'end': 22, 'text': 'Trevor Ward', 'label': 'name', 'score': 0.9245576858520508},
        {'start': 34, 'end': 48, 'text': 'Data Scientist', 'label': 'job', 'score': 0.9347354769706726},
        {'start': 74, 'end': 80, 'text': 'Monday', 'label': 'weekday', 'score': 0.9347354769706726}
    ]
    template = make_template_from_prediction(sample, entities)
    expected = "My name is {name} and I am a {job}. What are you doing this {weekday}?"
    assert template == expected
    print(expected)

def test_predict_template():
    import fraud as fr
    
    fake_model = MagicMock()
    fake_model.predict_entities.return_value = [
        {'start': 11, 'end': 22, 'text': 'Trevor Ward', 'label': 'name', 'score': 0.9245576858520508},
        {'start': 34, 'end': 48, 'text': 'Data Scientist', 'label': 'job', 'score': 0.9347354769706726},
        {'start': 74, 'end': 80, 'text': 'Monday', 'label': 'weekday', 'score': 0.9347354769706726}
    ]

    predicted_template = fr.predict_template(
        sample = "My name is Trevor Ward and I am a Data Scientist. What are you doing this Monday?",
        labels = ['name','job','weekday'],
        model = fake_model,
        threshold = 0.5,
    )

    assert predicted_template == "My name is {name} and I am a {job}. What are you doing this {weekday}?"