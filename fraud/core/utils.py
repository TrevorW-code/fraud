import string
from typing import TypeVar, List
from collections.abc import Callable
from functools import singledispatch

class PlaceholderMethodFailed(Exception):
    pass

### find placeholders ###

Template = TypeVar('T') # bind to template later or use annotated

@singledispatch
def find_placeholders(data):
    raise NotImplementedError(f'Unable to find placeholders for type: {type(data)}')

@find_placeholders.register(str)
def process_str(data):
    formatter = string.Formatter()
    return [field_name for _, field_name, _, _ in formatter.parse(data) if field_name]

def get_value_from_method(placeholder, method):
    try:
        res = method(placeholder)
        return res
    except Exception as e:
        # raise PlaceholderMethodFailed(f'Method Failed: {e}')
        return None

def replace_placeholders(template: Template, methods: List[Callable]) -> dict: 
    value_mapping = {}
    placeholders = find_placeholders(template) # gets placeholders to keep as keys
    
    try:
        for placeholder in placeholders: # go through each placeholder
            for method in methods: # go through each method
                res = get_value_from_method(placeholder, method)
                if res:
                    value_mapping[placeholder] = res
                    break
        
    except Exception as e:
        raise ValueError(f"Function Mapping Missing: {e}")

    return value_mapping