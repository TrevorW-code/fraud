import pytest
from fraud.base import Template, Templater

def test_basic_template():
    temp = Template('hello, {name}')
    
    assert temp.structure == 'hello, {name}'

def test_basic_templater():
    temp = Template('hello, {name}')
    templater = Templater(temp)
    out = templater.apply({'name':"Trevor"})
    
    assert out == 'hello, Trevor'
    
# def test_basic_fail_templater():
#     temp = Template('hello, name')
#     templater = Templater(temp)
#     out = templater.apply({'name':"Trevor"})
#     assert out == 'hello, Trevor'