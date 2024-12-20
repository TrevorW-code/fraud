import string
from typing import TypeVar, List
from collections.abc import Callable
from functools import singledispatch

class PlaceholderMethodFailed(Exception):
    pass

### find placeholders ###

Template = TypeVar('T') # bind to template later or use annotated

### Find Placeholders

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
        # raise ValueError(f"method bad: {e}")
        return None

def replace_placeholders(template: str, methods: List[Callable]) -> dict: 
    value_mapping = {}
    placeholders = find_placeholders(template) # gets placeholders to keep as keys
    
    try:
        for placeholder in placeholders: # go through each placeholder
            for method in methods: # try each method
                new_placeholder_value = get_value_from_method(placeholder, method)
                if new_placeholder_value:
                    value_mapping[placeholder] = new_placeholder_value
                    break
            if not new_placeholder_value:
                raise PlaceholderMethodFailed(f'Could not fetch value for: {placeholder}')
        
    except PlaceholderMethodFailed as pe:
        raise pe
    except Exception as e:
        raise ValueError(f"Error: {e}")

    return value_mapping