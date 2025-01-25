from fraud.utils._decorators import set_module
from typing import Callable, List
import functools
from fraud.core.utils import replace_placeholders
from fraud.core.base import Template, Templater, BasicGenerator
from fraud.plugins.faker import default_faker_instance, get_faker_value

@set_module("fraud")
def from_str(template_str: str, count: int, extra_methods: List[Callable]=None):
    # make template & methods
    output = []
    get_default_faker_val = functools.partial(get_faker_value, faker_instance=default_faker_instance)
    
    methods_to_apply = [get_default_faker_val]
    if extra_methods:
        methods_to_apply.extend(extra_methods)
    assert methods_to_apply, "Must apply methods"

    # make `count` number of times
    for i in range(count):
        fake_value_mapping = replace_placeholders(template_str, methods=methods_to_apply)
        template = Template(template_str)
        synthesized_sample = template.structure.format(**fake_value_mapping)
        output.append(synthesized_sample)

    return output

