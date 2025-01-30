from fraud.core.api import from_str
print("Downloading Default Model...")
from fraud.plugins.gliner import predict_template
print("Download Complete!")

__all__ = [
    "from_str",
    "predict_template"
]