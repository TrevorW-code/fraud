import abc
from typing import Dict, Any, TypeVar, Generic

T = TypeVar('T')

class Template(Generic[T]):
    def __init__(self, structure: T):
        """Initialize with a structure, which is the template."""
        self.structure = structure

    def __repr__(self) -> str:
        return f"Template({self.structure!r})"

class Templater:
    def __init__(self, template: Template[T]):
        """Templater takes a Template (string-based) to apply data to."""
        self.template = template

    def apply(self, data: Dict[str, Any]) -> str:
        """Apply the given data to the template, filling placeholders."""
        return self.template.structure.format(**data)

class IGenerator(abc.ABC):
    def __init__(self, template, value_map):
        self.template = template
        self.value_map = value_map

    @abc.abstractmethod
    def gen(self):
        pass

if __name__ == "__main__":
    dict_template = Template('Hello, {name}!')
    templater = Templater(dict_template)

    data = {'name': 'Alice'}
    print(templater.apply(data))
