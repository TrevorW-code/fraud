import abc
from typing import Dict, Any, TypeVar, Generic

T = TypeVar('T')

class Template(Generic[T]):
    def __init__(self, structure: T):
        self.structure = structure

    def __repr__(self) -> str:
        return f"Template({self.structure!r})"

class Templater:
    def __init__(self, template: Template[T]):
        self.template = template

    def apply(self, data: Dict[str, Any]) -> str:
        return self.template.structure.format(**data)

##### Generator #####

class IGenerator(abc.ABC):
    def __init__(self, template, templater):
        self.template = template
        self.templater = templater

    @abc.abstractmethod
    def make(self, samples_num: int = 1) -> str | list:
        pass

class BasicGenerator(IGenerator):
    def __init__(self, template, templater):
        super().__init__(template, templater)

    @abc.abstractmethod
    def make_fake(self):
        pass
    
    def make(self, samples_num: int = 1) -> str | list:
        if samples_num < 1:
            raise ValueError("Cannot generate less than 1 sample")
        elif samples_num == 1:
            return self.make_fake()
        else:
            samples_to_return = []
            for i in range(0,samples_num):
                samples_to_return.append(self.make_fake())
            return samples_to_return