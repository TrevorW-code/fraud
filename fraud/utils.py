import string
from functools import singledispatch

@singledispatch
def find_placeholders(data):
    raise NotImplementedError(f'Unable to find placeholders for type: {type(data)}')

@find_placeholders.register(str)
def process_str(data):
    formatter = string.Formatter()
    return [field_name for _, field_name, _, _ in formatter.parse(data) if field_name]