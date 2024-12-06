from faker import Faker
from typing import List
from .utils import find_placeholders
from .base import Templater
faker = Faker()

class FakerTemplater(Templater):
    def __init__(self, template, faker_instance=faker):
        self.faker = faker_instance
        super().__init__(template)
    
    def apply(self):

        # make faker data
        placeholders = find_placeholders(self.template.structure)
        faker_data = {}
        
        try:
            for placeholder in placeholders:
                faker_data[placeholder] = placeholder_to_faker_func(placeholder, self.faker)()
            
        except Exception as e:
            raise ValueError(f"Faker Function Mapping Missing: {e}")

        return super().apply(faker_data)

def placeholder_to_faker_func(placeholder: str, faker_instance=faker):
    faker_func = getattr(faker_instance, placeholder)
    return faker_func