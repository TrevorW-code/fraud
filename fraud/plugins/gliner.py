import gliner 
from fraud.utils._decorators import set_module
import warnings
warnings.filterwarnings("ignore") # warning from gliner about fast tokenizers

DEFAULT_MODEL = gliner.GLiNER.from_pretrained("urchade/gliner_medium-v2.1", use_fast=False)

@set_module('fraud')
def predict_template(
    sample: str,
    labels: list[str],
    model: gliner.model.GLiNER = DEFAULT_MODEL,
    threshold: float = 0.5
) -> str:

    predicted_entities = model.predict_entities(sample, labels, threshold)
    predicted_template = make_template_from_prediction(sample, predicted_entities)
    
    return predicted_template

def replace_word_at_indexes(sentence, start_index, end_index, new_word):
    return sentence[:start_index] + new_word + sentence[end_index:]

def make_template_from_prediction(string: str, predicted_entities: list[dict]):
    shift = 0
    for ent in predicted_entities:
        new = "{"+ent['label']+"}"
        old = ent['text']
        string = replace_word_at_indexes(
            string,
            ent['start'] - shift,
            ent['end'] -  shift,
            new
        )
        shift = shift + (len(old) - len(new))
    return string