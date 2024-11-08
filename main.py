from faker import Faker
faker = Faker()

class TemplateDataGenerator:
    def __init__(self, template: str, value_map: dict):
        self.template = template
        self.value_map = value_map

    def make_fake(self):
        replace_me = self.template
        for key, generator in self.value_map.items():
            replace_me = replace_me.replace(f"{{{key}}}", generator())
        
        return replace_me

    def gen(self, samples_num: int = 1) -> str | list:
        if samples_num < 1:
            raise ValueError("Cannot generate less than 1 sample")
        elif samples_num == 1:
            return self.make_fake()
        else:
            samples_to_return = []
            for i in range(0,samples_num):
                samples_to_return.append(self.make_fake())
            return samples_to_return
