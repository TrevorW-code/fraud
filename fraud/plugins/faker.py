from faker import Faker
from typing import Callable
from fraud.core.utils import find_placeholders
from fraud.core.base import Template, Templater, BasicGenerator
default_faker_instance = Faker()

class FakerTemplater(Templater):
    def __init__(self, template, faker_instance):
        self.faker = faker_instance
        super().__init__(template)
    
    def apply(self):
        placeholders = find_placeholders(self.template.structure)
        faker_data = {}
        
        try: # this applies the same value for different instances of a placeholder, for example "{name} meet {name}" = "John meet John"
            for placeholder in placeholders:
                faker_data[placeholder] = placeholder_to_faker_func(placeholder, self.faker)()
            
        except Exception as e:
            raise ValueError(f"Faker Function Mapping Missing: {e}")

        return super().apply(faker_data)

def placeholder_to_faker_func(placeholder: str, faker_instance) -> Callable:
    faker_func = getattr(faker_instance, placeholder)
    return faker_func

def get_faker_value(placeholder: str, faker_instance) -> str:
    """
    Fetches the appropriate faker generator and gets the value
    """
    return placeholder_to_faker_func(placeholder,faker_instance)()

class FakerGenerator(BasicGenerator):
    def __init__(self, template: Template, faker_instance=default_faker_instance):
        self.template = template
        self.templater = FakerTemplater(self.template,faker_instance)

    def make_fake(self):
        return self.templater.apply()